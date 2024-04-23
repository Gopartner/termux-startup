import os
import subprocess

def run_command(command):
    subprocess.run(command, shell=True)

def is_package_installed(package_name):
    result = subprocess.run(f"pkg list-installed {package_name}", shell=True, capture_output=True, text=True)
    return result.returncode == 0

def install_package(package_name):
    if not is_package_installed(package_name):
        run_command(f"pkg install {package_name} -y")
        print(f"{package_name} installed")
    else:
        print(f"{package_name} is already installed")

def setup_termux():
    print("TERMUX SETUP")

    run_command("termux-setup-storage")

    # Cek pembaruan hanya jika diperlukan
    run_command("pkg update")
    run_command("pkg upgrade")

    essential_packages = [
        "python",
        "neovim",
        "nodejs",
        "git",
        "curl",
        "openssh",
        "wget",
        "ruby",
        "php",
        "golang",
        "rust",
        "clang",
        "vim",
        "tmux",
        "sqlite",
        "httpie",
        "tree",
        "jq",
        "ffmpeg",
        "imagemagick",
        "neofetch",
        "ncurses-utils",
        "figlet"
    ]
    for package in essential_packages:
        install_package(package)

def setup_neovim():
    print("NEOVIM SETUP")

    packer_nvim_dir = os.path.expanduser("~/.local/share/nvim/site/pack/packer/start/packer.nvim")
    if not os.path.exists(packer_nvim_dir):
        run_command("git clone --depth 1 https://github.com/wbthomason/packer.nvim ~/.local/share/nvim/site/pack/packer/start/packer.nvim")

    user_input = input("Do you want to set Neovim as the default editor in Termux? [Y|N]: ").lower()
    if user_input == "y":
        termux_file_editor_path = os.path.expanduser("~/bin/termux-file-editor")
        if os.path.exists(termux_file_editor_path):
            print("Neovim is already the default editor.")
        else:
            os.symlink("/data/data/com.termux/files/usr/bin/nvim", termux_file_editor_path)
            print("Neovim is now the default editor.")

def apply_termux_customizations():
    print("APPLYING TERMUX CUSTOMIZATIONS")

    beautify_input = input("Do you want to add customizations to Termux? [Y|N]: ").lower()
    if beautify_input == "y":
        os.chdir(os.path.expanduser("~"))
        run_command("git clone https://github.com/remo7777/T-Header.git")
        os.chdir("T-Header")
        run_command("bash t-header.sh")
        print("Termux customization applied")

def run_python_script():
    print("RUNNING PYTHON SCRIPT")

    # Tambahkan kode Python di sini
    print("Hello from Python!")

def main():
    try:
        setup_termux()
        setup_neovim()
        apply_termux_customizations()
        run_python_script()  # Panggil fungsi untuk menjalankan kode Python

        print("Happy hacking! 😊🚀")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()

