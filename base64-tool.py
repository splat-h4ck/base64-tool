#!/usr/bin/python3
import sys
import argparse
import base64

parser = argparse.ArgumentParser(description='This is a handy tool that will Encode/Decode simple Base64 strings')

# Create groups for encode/decode
encoders = parser.add_mutually_exclusive_group()
decoders = parser.add_mutually_exclusive_group()

# Add arguments
encoders.add_argument("-e", "--encode", help="Encode a string into Base64")
decoders.add_argument("-d", "--decode", help="Decode a string from Base64")

args = parser.parse_args()

if args.decode is not None and args.encode is not None:
        print("\n\nI'm good, but I'm not THAT good! Please use either 'Encode' or 'Decode' - not both! Now - try again :)")
        parser.print_help()
        sys.exit()

if args.encode is not None:
        print(base64.standard_b64encode(args.encode))
if args.decode is not None:
        print(base64.b64decode(args.decode))
