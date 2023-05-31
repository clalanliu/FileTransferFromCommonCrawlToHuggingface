from retrying import retry
import os
import time


@retry(wait_exponential_multiplier=250, wait_exponential_max=32000)
def fetch_wet_s3(wet_path, save_path, log_filename="log"):
    aws = "aws s3"
    command = f"cp "
    src = f"s3://commoncrawl/{wet_path}"
    dst = save_path
    # argments = "--no-verify-ssl --cli-connect-timeout 6000"
    argments = " --cli-connect-timeout 6000"
    command = f"{aws} {command} {src} {dst} {argments}"
    command += f" > {log_filename}"

    os.system(command)
    t_upperbound = 1800
    t = time.time()
    while not os.path.exists(save_path) and time.time() - t < t_upperbound:
        time.sleep(0.2)

    if not os.path.exists(save_path):
        raise RuntimeError()
