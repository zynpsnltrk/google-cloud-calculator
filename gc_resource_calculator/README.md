GC Compute Engine Resource Calculator
===================

This script calculates and returns total memory and total cpu 
including Google Cloud Compute Engine based on 
the specified PROJECT_ID and ZONE.
```
usage: python gc-resource-calculator.py [-h] -p PROJECT_ID -z ZONE [-m] [-c] 
```
```
options:
    -h, --help                Print this message.
    -p, --project             Google Cloud PROJECT_ID.  
    -z, --zone                Google Cloud ZONE.
    -m, --memory              Returns total Memory by PROJECT_ID.
    -c, --cpu                 Returns total Cpu by PROJECT_ID.
```

# Dependencies

None

# Requirements

```
requirements.txt 
```

# Example usage
Create virtualenv and install requirements
```
$ virtualenv -p python3 venv
$ source venv/bin/activate
$ pip install -r requirements.txt
$ deactivate 
```
Example usage for gc-project-id
```
venv/bin/python gc-resource-calculator.py -p gc-project-id -z europe-west1-d -m -c
```
