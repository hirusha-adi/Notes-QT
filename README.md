# KQ-Pad

- Current Version: **v0.1**

Notepad knockoff made with Python and QT (PySide2).

# Compile or Run from Source

## Ubuntu/Debian

1. Run the commands below (line by line) to install the dependencies

```bash
sudo apt update && sudo apt upgrade
sudo apt install python3 python3-pip git -y
pip3 install -U PyInstaller PySide2
```

- Run the commands below to compile the software (SLOW + Resource Heavy)

```bash
cd "~/Desktop/"
mkdir temp && cd temp
git clone https://github.com/hirusha-adi/Notes-QT.git
cd Notes-QT

pyinstaller notes.py --onefile --noconfirm
# or
python3 -m PyInstaller notes.py --onefile --noconfirm

cd ./dist
sudo cp notes /usr/bin/notes
cd ~
rm -rf "~/Desktop/temp"
```

- Run from source (Fast + Lightweight)

```bash
cd "~/Desktop/"
mkdir temp && cd temp
git clone https://github.com/hirusha-adi/Notes-QT.git
cd Notes-QT
sudo mv notes.py /usr/bin/notes
cd ~
rm -rf "~/Desktop/temp"
```

## Arch Linux

1. Run the commands below (line by line) to install the dependencies

```bash
sudo pacman -Syyuu python python-pip git --noconfirm
pip install PySide2 PyInstaller
```

- Run the commands below to compile the software (SLOW + Resource Heavy)

```bash
cd "~/Desktop/"
mkdir temp && cd temp
git clone https://github.com/hirusha-adi/Notes-QT.git
cd Notes-QT
```

- Run from source (Fast + Lightweight)

```bash
cd "~/Desktop/"
mkdir temp && cd temp
git clone https://github.com/hirusha-adi/Notes-QT.git
cd Notes-QT
sudo mv notes.py /usr/bin/notes
cd ~
rm -rf "~/Desktop/temp"
```

## Microsoft Windows

1. Download and install Python3. Make sure to check "Add to PATH" on the first screen of installation
2. Open `cmd` and run the command below to install the requirements

```bash
pip install -U PyInstaller PySide2
```

3. Clone the repository and `cd` into it OR download the source code as `.zip` or `.tar.gz` and extract it. Open a `cmd` in the extracted folder.
4. Run the commands below to to compile

```bash
pyinstaller --noconfirm --onefile notes.py
```

5. Open the `.\dist` folder and you will find your compiled executable file (`.\dist\notes.exe`)
6. Copy the `notes.exe` to the `%system32%` folder with the `notes.png` (this file is optional) or add the current folder to PATH
7. Run `notes` in the `cmd` or `RUN` (`Win+R`) to start the program

# Credits

- Images

  1. Logo taken from [Wikimedia](https://upload.wikimedia.org/wikipedia/commons/thumb/7/71/Notepad_icon.svg/768px-Notepad_icon.svg.png)

- Sending me images of Notepad
  1. Discord user `OLIVER`
  2. Discord user `OkSheBroken`
  3. Discord user `key`
