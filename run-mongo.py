#!/usr/bin/env python
import os
import sys
import subprocess
import argparse


parser = argparse.ArgumentParser()
parser.add_argument("-u", "--user", help='create user only', default="no_arg")
args = parser.parse_args()

playbook_path = './mongo.yml'

if args.user == "no_arg":
    if not os.path.exists(playbook_path):
    print ('[INFO] The playbook does not exist in path', playbook_path)
    sys.exit()
	subprocess.call(["ansible-playbook", "-K", "./mongo.yml"])
elif args.user == 'user':
    print ("You nailed it!")
else:
    print ("Wrong Parameter, only option is -u user")