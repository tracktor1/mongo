#!/usr/bin/env python
import os
import sys
import subprocess
import argparse


parser = argparse.ArgumentParser()
parser.add_argument("-u", "--user", help='create user only', default="no_arg")
args = parser.parse_args()


if args.user == "no_arg":
    playbook_path = './mongo.yml'
    #if not os.path.exists(playbook_path):
    #    print ('[INFO] The playbook does not exist in path', playbook_path)
    #    sys.exit()
    print (playbook_path)
    subprocess.call(["ansible-playbook", "-K", "playbook_path"])
elif args.user == 'user':
    print ("You nailed it!")
else:
    print ("Wrong Parameter, only option is -u user")