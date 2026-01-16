import subprocess
result = subprocess.run(
    "echo Hello World",
    shell=True,
    capture_output=True,
    text=True
)
print(result.stdout)

subprocess.run(("python","TC_Multiple_Abstract.py"))
subprocess.run(("python","TC_ABc_Constructor.py"))
