from pascal_validator import *
import argparse
parser = argparse.ArgumentParser()
parser.add_argument('path', help='path to the file')
args = parser.parse_args()

pascal_validator(args.path)