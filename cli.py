#!/usr/bin/env python3

import os
import subprocess
import inquirer

from dotenv import load_dotenv

def list_python_scripts(directory="."):
    files = os.listdir(directory)
    python_files = [os.path.splitext(f)[0] for f in files if f.endswith(".py") and "cli" not in f]
    return python_files

def main():
    load_dotenv()

    python_scripts = list_python_scripts()

    if not python_scripts:
        print("No Python scripts found in the current directory.")
        return

    questions = [
        inquirer.List(
            "selected_script",
            message="Choose a Python script to run:",
            choices=python_scripts,
        )
    ]

    answers = inquirer.prompt(questions)

    selected_script = answers["selected_script"]

    # Add the ".py" extension back to the selected script filename
    selected_script_filename = f"{selected_script}.py"
    subprocess.run(["python", selected_script_filename])

    print("Process successfully finished.")

if __name__ == "__main__":
    main()
