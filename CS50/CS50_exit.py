import sys

if len(sys.argv) < 2:
    sys.exit("too few arguents")
if len(sys.argv)>2:
    sys.exit("to many arguents")

print("my name is",sys.argv[1])