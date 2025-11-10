# create_os_test.py
# Create os_test.txt from t.txt by selecting 5 videos per class
# that are NOT in os_train.txt or os_val.txt

from collections import defaultdict

t_file = "t.txt"
train_file = "os_train.txt"
val_file = "os_val.txt"
test_file = "os_test.txt"

# Load existing train and val entries
existing_videos = set()

for fname in [train_file, val_file]:
    with open(fname, "r") as f:
        for line in f:
            line = line.strip()
            if line:
                existing_videos.add(line)

# Prepare counters
class_counts = defaultdict(int)

with open(t_file, "r") as infile, open(test_file, "w") as outfile:
    for line in infile:
        line = line.strip()
        if not line:
            continue

        if line in existing_videos:
            continue  # skip videos already used in train/val

        class_name = line.split('/')[0]
        if class_counts[class_name] < 5:
            outfile.write(line + "\n")
            class_counts[class_name] += 1

print("✅ os_test.txt created successfully!")
print(f"→ Saved in {test_file}")
