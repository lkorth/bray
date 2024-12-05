import command_functions

from argparse import ArgumentParser

parser = ArgumentParser()
parser.add_argument("command")
args = parser.parse_args()

if args.command == "load":
    command_functions.load()
elif args.command == "retrieve":
    command_functions.retrieve()
else:
    print(f"{args.command} is not a valid command")
    sys.exit(1)
