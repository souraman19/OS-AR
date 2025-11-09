t1_file = "t1.txt"
t2_file = "t2.txt"
t3_file = "t3.txt"

# Read all lines from t1 and t2
with open(t1_file, "r") as f1:
    t1_lines = [line.strip() for line in f1 if line.strip()]

with open(t2_file, "r") as f2:
    t2_lines = {line.strip() for line in f2 if line.strip()}  # use a set for fast lookup

# Keep only lines in t1 that are not in t2
t3_lines = [line for line in t1_lines if line not in t2_lines]

# Write to t3
with open(t3_file, "w") as f3:
    f3.write("\n".join(t3_lines))

print(f"t3.txt created with {len(t3_lines)} lines (t1 - t2).")
