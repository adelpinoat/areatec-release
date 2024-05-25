import json
import os
import sys

def main():
    try:
        json_file = sys.argv[1]
        with open(json_file, 'r') as file:
            data = json.load(file)
            print(json.dumps(data))
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()
