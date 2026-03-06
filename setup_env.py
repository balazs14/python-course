#!/usr/bin/env python3
"""
Cross-platform Python environment setup script.

Creates a virtual environment called 'venv'
Upgrades pip
Installs requirements.txt if present
Registers a Jupyter kernel named 'venv'

Works on:
- Windows (cmd / PowerShell)
- macOS
- Linux
"""

import sys
import subprocess
import venv
from pathlib import Path


def check_python_version():
    """Ensure Python version is between 3.11.x and 3.14.x (inclusive)."""
    major = sys.version_info.major
    minor = sys.version_info.minor

    if major != 3 or minor < 11 or minor > 14:
        print("\n❌ ERROR: Unsupported Python version.")
        print(f"Detected: {sys.version.split()[0]}")
        print("Required: Python 3.11.x to 3.14.x (inclusive)")
        sys.exit(1)


def run(cmd):
    """Run a subprocess command and stop if it fails."""
    print(f"\n>>> Running: {' '.join(cmd)}")
    result = subprocess.run(cmd)
    if result.returncode != 0:
        print("\n❌ ERROR: Command failed.")
        sys.exit(result.returncode)


def main():
    check_python_version()

    project_root = Path(__file__).parent.resolve()
    venv_dir = project_root / "venv"
    requirements_file = project_root / "requirements.txt"

    print("=" * 40)
    print("Python Course Environment Setup")
    print("=" * 40)
    print(f"Project folder: {project_root}")
    print(f"Python version: {sys.version}")
    print("")

    # 1️⃣ Create virtual environment
    if not venv_dir.exists():
        print("Creating virtual environment 'venv'...")
        venv.create(venv_dir, with_pip=True)
    else:
        print("Virtual environment 'venv' already exists. rebuilding.")
        venv.create(venv_dir, with_pip=True)

    # 2️⃣ Determine correct Python executable inside venv
    if sys.platform == "win32":
        python_executable = venv_dir / "Scripts" / "python.exe"
    else:
        python_executable = venv_dir / "bin" / "python"

    if not python_executable.exists():
        print("\n❌ ERROR: Could not locate virtual environment Python executable.")
        sys.exit(1)

    print(f"Using virtual environment Python: {python_executable}")

    # 3️⃣ Upgrade pip
    print("\nUpgrading pip...")
    run([str(python_executable), "-m", "pip", "install", "--upgrade", "pip"])

    # 4️⃣ Install requirements if file exists
    if requirements_file.exists():
        print("\nInstalling packages from requirements.txt...")
        run([str(python_executable), "-m", "pip", "install", "-r", str(requirements_file)])
    else:
        print("\nNo requirements.txt found. Skipping package installation.")

    # 5️⃣ Ensure ipykernel is installed and register notebook kernel
    print("\nInstalling/ensuring ipykernel...")
    run([str(python_executable), "-m", "pip", "install", "ipykernel"])

    print("\nRegistering Jupyter kernel 'venv'...")
    run([
        str(python_executable),
        "-m",
        "ipykernel",
        "install",
        "--user",
        "--name",
        "venv",
        "--display-name",
        "venv",
    ])

    print("\n✅ Setup complete!")

    print("\nNext steps:")
    if sys.platform == "win32":
        print(r"  Activate with: venv\Scripts\activate")
    else:
        print("  Activate with: source venv/bin/activate")

    print("\nThen start working in VS Code.")


if __name__ == "__main__":
    main()
