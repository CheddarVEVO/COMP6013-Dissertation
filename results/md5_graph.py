import pandas as pd
import matplotlib.pyplot as plt

result = pd.read_csv("results.csv")

# Filter to only show MD5 results
md5 = result[result.hash_type == "md5"]
# Each policy is a row, each tool is column
tool_comparison = md5.pivot(index="policy", columns="tool", values="crack_rate")
# Re-order policies to len8 -> len12 -> composition -> blocklist
tool_comparison = tool_comparison.reindex(["len8", "len12","composition", "blocklist"])
# Creates bar chart 
percentage = tool_comparison.plot(kind="bar")
plt.ylabel("Crack rate (%)")
plt.title("MD5 Crack rate: legacy (John the Ripper) vs modern (Hashcat)")
plt.xticks(rotation=0)
for container in percentage.containers:
    percentage.bar_label(container, fmt="%.2f")
plt.tight_layout()
plt.savefig("md5_modern_vs_legacy.png", dpi=300)
