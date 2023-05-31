import os
import logging

from huggingface_hub import create_repo
from huggingface_hub import HfApi
from retrying import retry

logger = logging.Logger(__name__)


# @retry(wait_exponential_multiplier=250, wait_exponential_max=32000)
def upload_to_huggingface(repo_id, file_path):
    try:
        create_repo(f"repo_id", repo_type="dataset", private=True)
    except:
        logger.info(f"{repo_id} exists!")
    api = HfApi()
    api.upload_file(
        path_or_fileobj=file_path,
        path_in_repo=file_path,
        repo_id=repo_id,  # "MediaTek-Research/test",
        repo_type="dataset",
    )


if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)
    upload_to_huggingface(
        repo_id="MediaTek-Research/test", file_path="requirements.txt"
    )
