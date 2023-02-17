import subprocess


subprocess.run(["git", "init"], check=True)
subprocess.run(["git", "add", "*"], check=True)
subprocess.run(
    ["git", "add", "-f", "{{cookiecutter.project_name}}/data/.gitkeep"], check=True
)
subprocess.run(
    ["git", "commit", "-a", "-m", "Initial commit from cookiecutter template"],
    check=True,
)

if "{{cookiecutter.remote_url}}":
    subprocess.run(["git", "checkout", "main"], check=True)
    subprocess.run(
        ["git", "remote", "add", "origin", "{{cookiecutter.remote_url}}"], check=True
    )
    subprocess.run(["git", "remote", "-v"], check=True)
    subprocess.run(["git", "push", "origin", "main"], check=True)

if "{{cookiecutter.create_venv}}" == "yes":
    subprocess.run(["python", "-m", "venv", "venv"], check=True)
    subprocess.run(["venv/bin/pip", "install", "-e", ".[dev]"], check=True)
