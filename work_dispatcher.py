import sys
import os
import gzip
import argparse
from multiprocessing import Pool
import tqdm
from aws_downloader import fetch_wet_s3
from huggingface_uploader import upload_to_huggingface
from file_checker import is_file_downloaded, is_file_on_huggingface, get_start_idx

parser = argparse.ArgumentParser()
parser.add_argument("--snapshot", "-s", type=str, default='2021-17')
parser.add_argument("--pool", "-p", type=int, default=4)
parser.add_argument("--repo_id", "-r", type=str, default="MediaTek-Research")
args = parser.parse_args()

SNAPSHOT = args.snapshot
repo_id = os.path.join(args.repo_id, f"cc{SNAPSHOT}")
p = Pool(args.pool)


def func(wet_filepath):
    save_filename = os.path.join("wets", wet_filepath)
    log_filename = os.path.join("wets", "logs", wet_filepath + ".log")
    if not os.path.exists(os.path.dirname(log_filename)):
        os.makedirs(os.path.dirname(log_filename))

    if not is_file_on_huggingface(repo_id=repo_id, file_path=save_filename):
        if not os.path.exists(save_filename):
            fetch_wet_s3(wet_filepath, save_filename, log_filename)

        upload_to_huggingface(repo_id, save_filename)
        os.system(f"rm {save_filename}")
    else:
        print(f"{wet_filepath} exists")


wet_path_gz = os.path.join("wets", "wet_path", SNAPSHOT, "wet.paths.gz")
with gzip.open(wet_path_gz, "r") as fin:
    lines = fin.readlines()
    lines = [line.decode("utf-8").strip() for line in lines]

start_idx = get_start_idx(repo_id=repo_id, paths=lines)
lines = lines[start_idx:]
print(f"Start from {start_idx}")

for i, line in tqdm.tqdm(enumerate(lines)):
    if i > 0:
        func(line)
