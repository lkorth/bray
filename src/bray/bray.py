import command_functions
import logging

from argparse import ArgumentParser

parser = ArgumentParser()
parser.add_argument("command")
parser.add_argument('--log', default='ERROR', help='Set the logging level (DEBUG, INFO, WARNING, ERROR, CRITICAL)')
args = parser.parse_args()

logging.basicConfig(level=args.log.upper(), format='%(levelname)s: %(message)s')

if args.command == "load":
    command_functions.load()
elif args.command == "retrieve":
    command_functions.retrieve()
else:
    print(f"{args.command} is not a valid command")
    sys.exit(1)
