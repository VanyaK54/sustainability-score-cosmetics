import os

def ensure_dir(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)

def save_to_csv(df, path):
    ensure_dir(os.path.dirname(path))
    df.to_csv(path, index=False)

def log_message(message, logfile="../outputs/logs/pipeline_run_log.txt"):
    ensure_dir(os.path.dirname(logfile))
    with open(logfile, "a") as f:
        f.write(f"{message}\n")
