import os
from pathlib import Path
import subprocess

def format_markdown(filepath):
    """Formats a markdown file using prettier.

    Args:
        filepath: The path to the markdown file.
    """

    try:
        # Check if prettier is installed.  A more robust check might involve
        # trying to execute prettier with --version and checking the return code.
        subprocess.check_output(["prettier", "--version"]) 

        # Format the file in place
        subprocess.run(
            ["prettier", "--write", filepath],
            check=True,  # Raise an exception if prettier fails
            capture_output=True, # Capture output for debugging if needed
            text=True # Ensure we can decode output as text
        )

        print(f"Successfully formatted {filepath}")

    except FileNotFoundError:
        print("Error: prettier not found. Please install prettier (e.g., npm install -g prettier)")
    except subprocess.CalledProcessError as e:
        print(f"Error formatting {filepath}:")
        print(e.stderr)  # Print prettier's error message
    except Exception as e: # Catch any other potential errors
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    filepath = Path("/data/format.md")  # Use Path for better cross-platform compatibility

    if filepath.exists():
        format_markdown(str(filepath)) # prettier expects a string path
    else:
        print(f"Error: File not found: {filepath}")