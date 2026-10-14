import os
import platform
import shutil
import subprocess


def _run(cmd):
    try:
        return subprocess.run(cmd, capture_output=True, text=True, timeout=5).stdout.strip()
    except (OSError, subprocess.SubprocessError):
        return ""


def retrieve_system_info():
    """Describe the host machine so the model can tune the generated C++ for it."""
    info = {
        "os": platform.platform(),
        "machine": platform.machine(),
        "processor": platform.processor(),
        "cpu_count": os.cpu_count(),
        "python": platform.python_version(),
    }
    if platform.system() == "Darwin":
        info["cpu_brand"] = _run(["sysctl", "-n", "machdep.cpu.brand_string"])
    for compiler in ("clang++", "g++"):
        if shutil.which(compiler):
            info[compiler] = _run([compiler, "--version"]).splitlines()[0]
    return info
