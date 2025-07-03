import os
import subprocess

def run_python_file(working_directory, file_path):
    
    abs_working_directory = os.path.abspath(working_directory)
    abs_file_path = os.path.abspath(os.path.join(working_directory, file_path))

    if not abs_file_path.startswith(abs_working_directory):
        return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'

    if not os.path.exists(abs_file_path):
        return f'Error: File "{file_path}" not found.'

    if not abs_file_path.endswith(".py"):
        return f'Error: "{file_path}" is not a Python file.'

    try:
        result = subprocess.run(
                ["python", abs_file_path],
                capture_output=True,
                text=True,
                timeout=30,
                cwd=abs_working_directory
        )

        stdout_output = result.stdout
        stderr_output = result.stderr
        return_code = result.returncode

        if result.stdout == "" and result.stderr == "":
            return "No output produced."

        formatted_string = f"STDOUT: {stdout_output}\nSTDERR: {stderr_output}"

        if return_code != 0:
            return f"{formatted_string}\nProcess exited with code {return_code}"

        return formatted_string

    except Exception as e:
        return f"Error: executing Python file: {e}"
