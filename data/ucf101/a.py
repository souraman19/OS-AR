# split_equal_t1_t2.py
# Divide videos per class equally between t1.txt and t2.txt

from collections import defaultdict

input_file = "t.txt"
t1_file = "t1.txt"
t2_file = "t2.txt"

# Read all videos
class_to_videos = defaultdict(list)

with open(input_file, "r") as f:
    for line in f:
        line = line.strip()
        if not line:
            continue
        class_name = line.split('/')[0]
        class_to_videos[class_name].append(line)

# Write equal split to t1 and t2
with open(t1_file, "w") as t1, open(t2_file, "w") as t2:
    for class_name, videos in class_to_videos.items():
        total = len(videos)
        half = total // 2

        # Split equally (if odd, t2 will get one extra)
        t1_videos = videos[:half]
        t2_videos = videos[half:]

        for v in t1_videos:
            t1.write(v + "\n")
        for v in t2_videos:
            t2.write(v + "\n")

print("Split complete!")
print(f"→ Saved {t1_file} and {t2_file} with equal class-wise splits.")