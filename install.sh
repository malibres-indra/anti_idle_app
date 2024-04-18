#!/bin/bash

check_virtual_environment_exists() {
    venv_name=$1
    venv_dir="./${venv_name}"
    
    # Check if the venv folder or a specific file exists
    if [ -d "${venv_dir}" ] || [ -f "${venv_dir}/pyvenv.cfg" ]; then
        return 0
    else
        return 1
    fi
}

# Specify the name of the virtual environment to check
venv_name="venv"
# Specify the path and name for the virtual environment
venv_path="./venv"

# Check if the virtual environment exists
if check_virtual_environment_exists "${venv_name}"; then
    source "${venv_path}/bin/activate" 
    echo "The virtual environment '${venv_name}' exists."
else
    # # Create the virtual environment
    python3 -m venv "${venv_path}"

    # Activate the virtual environment
    # source "${venv_path}/Scripts/activate"  # For Windows
    source "${venv_path}/bin/activate"     # For Unix/Linux

    # Install packages in the virtual environment using pip
    pip install -r requirements.txt

fi
