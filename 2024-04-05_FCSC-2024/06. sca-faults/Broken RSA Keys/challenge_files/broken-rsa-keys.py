import sys
import json
import hashlib

if __name__ == "__main__":

    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} <key file>")
        exit(1)

    keys = json.load(open(sys.argv[1]))
    flag = hashlib.sha256()
    for i, key in enumerate(keys):
        locals().update(key)
        s = f"{p}{q}{iq}{dp}{dq}"
        flag.update(s.encode())
        assert check == hashlib.sha256(s.encode()).hexdigest(), f"Error: key #{i} is wrongly corrected: {key}."

    print(f"FCSC{{{flag.hexdigest()}}}")
