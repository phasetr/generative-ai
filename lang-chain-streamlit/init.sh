curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh -s -- -y
export PATH=${PATH}:${HOME}/.cargo/bin
pip install --upgrade pip
pip install -r requirements.txt
