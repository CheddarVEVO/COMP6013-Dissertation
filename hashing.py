import os
import argparse
import hashlib

def main():
    # CLI arguments to parse subset file as an input and then output it as a hash file (currently MD5)
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", required =True, help="Plaintext subset file")
    parser.add_argument("--output", required =True, help="Output hash file")
    args = parser.parse_args()

    out_dir = os.path.dirname(args.output)
    if out_dir:
        os.makedirs(out_dir, exist_ok=True)

    # Verifying that all passwords have been successfully hashed (mainly for testing)
    total = 0
    written = 0

    with open(args.input, "r", encoding="latin-1") as fin:
        with open(args.output, "w", encoding="latin-1") as fout:
            for line in fin:
                password = line.rstrip("\r\n")
                if not password:
                    continue
                total += 1

                # MD5 encoding
                hash = hashlib.md5(password.encode("latin-1")).hexdigest()
                fout.write(hash + "\n")
                written += 1
    
    print ("Passwords read: ", total)
    print ("Passwords hashed: ", written)

if __name__ == "__main__":
    main()
