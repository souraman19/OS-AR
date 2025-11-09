# split_t_limit4.py
# Read from t.txt and create t1.txt and t2.txt
# Take first video -> t1, next 4 -> t2

input_file = "t.txt"
t1_file = "t1.txt"
t2_file = "t2.txt"

from collections import defaultdict

class_counts = defaultdict(int)

with open(input_file, "r") as infile, \
     open(t1_file, "w") as t1, \
     open(t2_file, "w") as t2:

    for line in infile:
        line = line.strip()
        if not line:
            continue

        class_name = line.split('/')[0]
        class_counts[class_name] += 1
        count = class_counts[class_name]

        if 1 <= count <= 5:
            t1.write(line + "\n")          # first line → t1
        elif 6 <= count <= 10:
            t2.write(line + "\n")          # next 4 lines → t2
        # ignore lines after 5th occurrence

print("Split complete!")
print(f"→ saved in {t1_file}")
print(f"→ saved in {t2_file}")
