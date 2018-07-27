import subprocess

completed = subprocess.run('echo $HOME', shell=True)
print('returncode:', completed.returncode)

