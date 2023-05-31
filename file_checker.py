from huggingface_hub import list_files_info
import requests
import logging
import os

logger = logging.Logger(__name__)


def is_file_on_huggingface(repo_id, file_path):
    files_info = []
    try:
        files_info = list(list_files_info(
            repo_id, [file_path], repo_type="dataset"))
        # r = requests.get("https://huggingface.co/datasets/{repo_id}/blob/main/{path}")
    except:
        return False
    if len(files_info) > 0:
        # logger.info(f"File {files_info} exists in {repo_id}")
        # print(f"File {files_info} exists in {repo_id}")
        return True
    else:
        return False


def is_file_downloaded(path):
    return os.path.exists(path)


def get_start_idx(repo_id, paths):
    left = 0
    right = len(paths) - 1
    while left <= right:
        mid = (left + right) // 2
        if not is_file_on_huggingface(repo_id, os.path.join('wets', paths[mid])):
            right = mid - 1
        else:
            left = mid + 1
    return left


if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)
    is_file_on_huggingface(
        repo_id="MediaTek-Research/test", file_path=".gitattributes")
    is_file_on_huggingface(
        repo_id="MediaTek-Research/test", file_path="requirements.txt"
    )
