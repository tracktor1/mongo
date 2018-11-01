import argparse


parser = argparse.ArgumentParser()
parser.add_argument("default", default="no_arg")
parser.add_argument("user", help='create user only', default="no_arg")

#parser.add_argument("user", action="store_true")
args = parser.parse_args()
#if args.user == True:
#	print("Deep Shit")
#elif args.user == user:
#	print(args.user)
#    args.user = "run all"

#parser.add_argument("user", nargs='?', default="no_arg")

if args.user == "no_arg":
    print ("I can tell that no argument was given and I can deal with that here.")
elif args.user == 'magic.name':
    print ("You nailed it!")
else:
    print (args.user)