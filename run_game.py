import os
import subprocess
import sys

# Check if the script path is provided as an argument
if len(sys.argv) != 2:
    print("Usage: python3 run_script.py <full-path-to-script>")
    sys.exit(1)

# Get the full path to the script to run from the command line argument
script_path = sys.argv[1]

# Ensure the script exists
if not os.path.isfile(script_path):
    print(f"Error: The file {script_path} does not exist.")
    sys.exit(1)

# Get the directory of the script (so we can change to it)
script_dir = os.path.dirname(os.path.abspath(script_path))

# Change the working directory to where the script is located
os.chdir(script_dir)

# Run the Python script
subprocess.run(['python3', os.path.basename(script_path)])
