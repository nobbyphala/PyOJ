import sys
import subprocess
import os

def subprocess_cmd(command):
    process = subprocess.Popen(command,stdout=subprocess.PIPE, shell=True, preexec_fn=os.setsid)
    try:
        proc_stdout = process.communicate(timeout=5)[0].strip()
    except subprocess.TimeoutExpired:
        os.killpg(process.pid, signal.SIGINT)
        proc_stdout = process.communicate()[0].strip()

    return process.returncode
