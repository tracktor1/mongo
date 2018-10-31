import argparse


parser = argparse.ArgumentParser(argument_default=shit)
parser.add_argument("user", action="store_true")
args = parser.parse_args()
if args.user == "True"
    args.user = "run all"
print(args.user)