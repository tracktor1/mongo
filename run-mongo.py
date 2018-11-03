#!/usr/bin/env python
import argparse

parser = argparse.ArgumentParser()

parser.add_argument("-u", "--user", help='create user only', default="no_arg")
args = parser.parse_args()

if args.user == "no_arg":
    print ("I can tell that no argument was given and I can deal with that here.")
elif args.user == 'user':
    print ("You nailed it!")
else:
    print ("Wrong Parameter, only option is -u user")