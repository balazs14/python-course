Python Virtual Environment Setup
================================

This project uses a virtual environment (venv) to isolate dependencies.
Follow the steps below to create and activate the environment, then install the required packages.

1. Create a virtual environment
-------------------------------

macOS / Linux::

    python3 -m venv .venv

Windows (PowerShell)::

    python -m venv .venv

2. Activate the virtual environment
-----------------------------------

macOS / Linux::

    source .venv/bin/activate

Windows (PowerShell)::

    .\.venv\Scripts\Activate.ps1

Windows (cmd.exe)::

    .\.venv\Scripts\activate.bat

3. Install required dependencies
--------------------------------

With the venv activated::

    pip install -r requirements.txt

4. Deactivate the environment
-----------------------------

When done::

    deactivate

5. Reactivate later
-------------------

macOS / Linux::

    source .venv/bin/activate

Windows (PowerShell)::

    .\.venv\Scripts\Activate.ps1
