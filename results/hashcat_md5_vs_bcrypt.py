import pandas as pd
import matplotlib.pyplot as plt

result = pd.read_csv("results.csv")

# Filters results only for Hashcat
hashcat = result[result.tool == "hashcat"]
# Each policy is a row, each hashing algorithm is column
hc_hash_comp = hashcat.pivot(index="policy", columns="hash_type", values="crack_rate")
# Re-order policies to len8 -> len12 -> composition -> blocklist
hc_hash_comp = hc_hash_comp.reindex(["len8", "len12", "composition", "blocklist"])
# Re-order to put MD5 first then bcrypt
hc_hash_comp = hc_hash_comp[["md5", "bcrypt"]]
# Change bar colours to not conflict other categories from different graphs (MD5= red, bcrypt = green)
hash_colour = hc_hash_comp.plot(kind="bar", color=["red", "green"])
plt.ylabel("Crack rate (%)")
plt.title("Hashcat crack rate: MD5 vs bcrypt")
plt.xticks(rotation=0)
for container in hash_colour.containers:
    hash_colour.bar_label(container, fmt="%.2f")
plt.tight_layout()
plt.savefig("hashcat_md5_vs_bcrypt.png", dpi=300)
