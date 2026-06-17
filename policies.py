import os
import argparse
output_dir = "subsets"

def count_char_type(password):
    # Returns the amount of characters in each password.
    has_lowercase = any(character.islower() for character in password)
    has_uppercase = any(character.isupper() for character in password)
    has_digit = any(character.isdigit() for character in password)
    # Special characters (!,@,#, etc.)
    has_schar = any(not character.isalnum() for character in password)
    return has_lowercase, has_uppercase, has_digit, has_schar

def load_blocklist(blocklist):
    # Load blocklist into set
    blocked_passwords = set()
    with open(blocklist, "r") as f:
        for line in f:
            blocked_passwords.add(line.rstrip("\r\n"))
        return blocked_passwords

def main():
    # Command line parsing to filter corpus into policy subsets
    parser = argparse.ArgumentParser()
    parser.add_argument("--corpus", required=True, help="Path to corpus")
    parser.add_argument("--blocklist", required=True, help="Path to Blocklist")
    parser.add_argument("--len8", type=int, default=8, help="Composition policy of 8 characters")
    parser.add_argument("--len12", type=int, default=12, help="Composition policy of 12 characters")
    args = parser.parse_args()

    os.makedirs(output_dir, exist_ok=True)
    blocked = load_blocklist(args.blocklist)
    # Test to check the blocklist loaded
    print ("Blocklist entries:", len(blocked))

    output_files = {
        "len8": open(os.path.join(output_dir, "len8.txt"), "w"),
        "len12": open(os.path.join(output_dir, "len12.txt"), "w"),
        "composition": open(os.path.join(output_dir, "composition.txt"), "w"),
        "blocklist": open(os.path.join(output_dir, "blocklist.txt"), "w"),
    }

    # Counts total passwords that meets the policies
    counter = {i: 0 for i in output_files}
    total = 0

    with open(args.corpus, "r") as f:
        for line in f:
            password = line.rstrip("\r\n")
            if not password:
                continue
            total += 1

            if len(password) >= args.len8:
                output_files["len8"].write(password + "\n")
                counter["len8"] += 1
            
            if len(password) >= args.len12:
                output_files["len12"].write(password + "\n")
                counter["len12"] += 1
            
            if len(password) >= args.len8:
                lowercase, uppercase, digit, schar = count_char_type(password)
                if lowercase and uppercase and digit and schar:
                    output_files["composition"].write(password + "\n")
                    counter["composition"] += 1

            if len(password) >= args.len8 and password not in blocked:
                output_files["blocklist"].write(password + "\n")
                counter["blocklist"] += 1

    for o in output_files.values():
        o.close()

    print ("Total passwords read:", total)
    for policy, n in counter.items():
        percentage = (n / total * 100) if total else 0
        print (policy, ":", n, ("(") + str(round(percentage, 1)), "% of corpus)")

if __name__ == "__main__":
    main()