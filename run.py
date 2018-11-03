#!/usr/bin/env python
import os
import sys
import subprocess
import argparse

playbook_path = './mongo.yml'
if not os.path.exists(playbook_path):
    print ('[INFO] The playbook does not exist in path', playbook_path)
    sys.exit()

	
subprocess.call(["ansible-playbook", "-K", "./mongo.yml"])
#subprocess.call(["ping", "-c 2", "8.8.8.8"])