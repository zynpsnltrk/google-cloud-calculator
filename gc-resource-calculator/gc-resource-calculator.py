import argparse
from googleapiclient import discovery
from oauth2client.client import GoogleCredentials


class GCResourceCalculator():
    instances = []
    compute = discovery.build('compute', 'v1')
    credentials = GoogleCredentials.get_application_default()
    service = discovery.build('compute', 'v1', credentials=credentials)
    machine_types = []

    def __init__(self, project, zone):
        self.project = project
        self.zone = zone
        self._get_instances()
        self._get_machine_types()

    def _get_instances(self):
        result = self.compute.instances().list(project=self.project, zone=self.zone).execute()
        for item in result['items']:
            self.instances.append(item['machineType'].split('machineTypes/')[1])

    def _get_machine_types(self):
        request = self.service.machineTypes().list(project=self.project, zone=self.zone)
        while request is not None:
            response = request.execute()
            for machine_types in response['items']:
                self.machine_types.append(machine_types)
            request = self.service.machineTypes().list_next(previous_request=request, previous_response=response)

    def get_resources(self, option):
        sum_resources = 0.0
        for instance in self.instances:
            for machine_type in self.machine_types:
                if instance == machine_type['name']:
                    sum_resources += float(machine_type[option])
                    break
                elif "custom" in instance:
                    if option == "memoryMb":
                        sum_resources += self._calculate_custom_memory(instance)
                    else:
                        sum_resources += self._calculate_custom_cpu(instance)
                    break
        return sum_resources

    def _calculate_custom_cpu(self, item):
        return float(item.split('-')[1])

    def _calculate_custom_memory(self, item):
        return float(item.split('-')[2])


if __name__ == "__main__":
    arg_parser = argparse.ArgumentParser()
    arg_parser.add_argument("-p", "--project", help="Google Cloud PROJECT_ID.", type=str, required=True)
    arg_parser.add_argument("-z", "--zone", help="Google Cloud ZONE.", type=str, required=True)
    arg_parser.add_argument("-m", "--memory", help="Returns total Memory by PROJECT_ID.", action="store_true")
    arg_parser.add_argument("-c", "--cpu", help="Returns total Cpu by PROJECT_ID.", action="store_true")
    args = arg_parser.parse_args()

    project = GCResourceCalculator(args.project, args.zone)
    if not (args.memory and args.memory):
        arg_parser.error('Returns as total memory or cpu only. Use [-m] and [-c] flags.')
    if args.cpu:
        cpu = round(project.get_resources("guestCpus"))
        print("The total cpu size in {} is {} cores.".format(args.project, cpu))
    if args.memory:
        memory = round(project.get_resources("memoryMb")/1000)
        print("The total memory size in {} is {} GB.".format(args.project, memory))

