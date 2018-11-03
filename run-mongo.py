#!/usr/bin/env python
import os
import sys
import subprocess
import argparse


parser = argparse.ArgumentParser()
parser.add_argument("-u", help='create user only', default="no_arg")
args = parser.parse_args()


if args.user == "no_arg":
    subprocess.call(["ansible-playbook", "-K", "./mongo.yml"])
elif args.user == 'user':
    subprocess.call(["ansible-playbook", "-K", "./mongo.yml",  "--tags", "user"])
else:
    print ("Wrong Parameter, only option is -u user")