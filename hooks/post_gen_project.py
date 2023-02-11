import subprocess

subprocess.run(["git", "init"])
subprocess.run(["git", "add", "*"])
subprocess.run(["git", "add", "-f", "{{cookiecutter.project_name}}/data/.gitkeep"])
subprocess.run(["git", "add", "-f", "notebooks/00_experiments.ipynb"])
subprocess.run(
    ["git", "commit", "-a", "-m", "Initial commit from cookiecutter template"]
)

if "{{cookiecutter.remote_url}}":
    subprocess.run(["git", "checkout", "main"])
    subprocess.run(["git", "remote", "add", "origin", "{{cookiecutter.remote_url}}"])
    subprocess.run(["git", "remote", "-v"])
    subprocess.run(["git", "push", "origin", "main"])

subprocess.run(["virtualenv", "venv"])
subprocess.run(["powershell.exe", ".\\venv\\Scripts\\activate"])
subprocess.run(["pip", "install", "-e", ".[dev]"])
