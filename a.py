import os

ucf_root = "data/ucf101"
split_root = "data/ucfTrainTestlist"

# Read class index mapping
class_map = {}
with open(os.path.join(split_root, "classInd.txt"), "r") as f:
    for line in f:
        idx, cls = line.strip().split()
        class_map[cls] = int(idx) - 1  # make it 0-based

def convert_split(in_file, out_file):
    lines_out = []
    missing = 0
    with open(in_file, "r") as f:
        for line in f:
            video_path = line.strip().split()[0]  # e.g. ApplyEyeMakeup/v_ApplyEyeMakeup_g01_c01.avi
            full_path = os.path.join(ucf_root, video_path)
            if not os.path.exists(full_path):
                missing += 1
                continue
            cls_name = video_path.split("/")[0]
            label = class_map[cls_name]
            lines_out.append(f"{video_path} {label}\n")

    with open(out_file, "w") as f:
        f.writelines(lines_out)
    print(f"✅ Wrote {out_file} ({len(lines_out)} videos, skipped {missing} missing files)")

# Convert both train/test lists
convert_split(os.path.join(split_root, "trainlist01.txt"), "data/ucf101/train.txt")
convert_split(os.path.join(split_root, "testlist01.txt"), "data/ucf101/val.txt")
