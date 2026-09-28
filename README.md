# Password Policy Effectiveness Against Modern Offline Attacks

## Requirements
- Python 3
- [Hashcat](https://hashcat.net/hashcat/) 7.1.2 or later (GPU with OpenCL or CUDA support)
- [John the Ripper Jumbo](https://github.com/openwall/john) 1.9.0 or later
Python dependencies:
 
```bash
pip install bcrypt pandas matplotlib
```
 
## Usage
 
### Filtering the corpus into policy-compliant subsets
 
```bash
python policies.py --corpus <path_to_corpus.txt> --blocklist <path_to_blocklist.txt> --output <output_directory>
```
 
Produces four deduplicated (case-sensitive) subsets: `len8`, `len12`, `composition`, `blocklist`.
 
### Hashing subsets
 
```bash
python hashing.py --input <subset_directory> --algorithm md5|bcrypt --output <output_directory>
```
Passwords are truncated to 72 bytes prior to bcrypt hashing to comply with bcrypt's input length limit.

## Data sources and licensing 
- **Fortinet 2021 breach corpus** — sourced via [SecLists](https://github.com/danielmiessler/SecLists) (MIT licence)
- **NCSC 100k most-used passwords** — sourced via SecLists (MIT licence)
- **RockYou wordlist** — sourced via [Weakpass](https://weakpass.com) (CC BY 4.0)
- **Dic-0294 dictionary** — sourced from [trapd00r/Documentation](https://github.com/trapd00r/Documentation/blob/master/wordlists/dic-0294.txt) on GitHub, no explicit licence restrictions
  
All resources were used solely for academic research purposes.
