from collections import defaultdict

# Input file containing your videos
input_file = "t.txt" 
t1_file = "t1.txt"
t2_file = "t2.txt"

# Dictionaries to track counts per class
class_counts_t1 = defaultdict(int)
class_counts_t2 = defaultdict(int)

# Keep track of first and second video per (class, g_num)
category_seen = {}

t1_list = []
t2_list = []

with open(input_file, "r") as f:
    for line in f:
        line = line.strip()
        if not line:
            continue

        path, label = line.split()
        parts = path.split("/")
        class_name = parts[0]

        # Extract g_num from filename
        filename = parts[1]
        g_idx = filename.find("_g")
        if g_idx == -1:
            continue
        g_num = filename[g_idx+2:g_idx+4]  # "08", "09", etc.

        # Only consider g_num 08-14
        if int(g_num) < 8 or int(g_num) > 14:
            continue

        category_key = (class_name, g_num)

        if category_key not in category_seen:
            # first video → t1
            if class_counts_t1[class_name] < 6:
                t1_list.append(line)
                class_counts_t1[class_name] += 1
            category_seen[category_key] = 1
        elif category_seen[category_key] == 1:
            # second video → t2
            if class_counts_t2[class_name] < 6:
                t2_list.append(line)
                class_counts_t2[class_name] += 1
            category_seen[category_key] = 2
        else:
            # already taken 2 videos, ignore
            continue

# Write outputs
with open(t1_file, "w") as f:
    f.write("\n".join(t1_list))

with open(t2_file, "w") as f:
    f.write("\n".join(t2_list))

print(f"t1.txt contains {len(t1_list)} videos")
print(f"t2.txt contains {len(t2_list)} videos")
