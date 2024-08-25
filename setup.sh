#!/bin/bash
# Setup developement environment

VENV_DIR=".venv"

create_venv() {
    echo "Creating python virtual environment"
    python3 -m venv .venv
    echo "Virtual environment created"
}

activate_venv() {
    echo "Activating the virtual environment"
    source "$VENV_DIR/bin/activate"
}

install_python_dependencies() {
    echo "Installing python dependencies."
    pip3 install -r requirements.txt
    echo "Python dependencies installed."
}

check_docker() {
    # Check if command is recognized by shell
    if command -v docker &> /dev/null; then
        echo "Docker already installed."
    else
        echo "Docker not installed, installing."
        ./setup_scripts/install_docker.sh
        echo "Docker installed."
    fi
}

# checking if the virtual environment exists.
if [ -d "$VENV_DIR" ]; then
    activate_venv
else
    create_venv
    activate_venv
fi

install_python_dependencies
check_docker
