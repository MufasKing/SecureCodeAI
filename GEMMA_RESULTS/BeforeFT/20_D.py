import re
import sys

def main():
    if len(sys.argv) != 2:
        print("Usage: %s <target>" % sys.argv[0])
        sys.exit(1)

    target = sys.argv[1]

    if re.match(r"example\.com", target):
        print("Redirecting to %s" % target)
        sys.exit(0)

    print("Redirecting to /")
    sys.exit(0)

if __name__ == "__main__":
    main()