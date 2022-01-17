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
sudo cp notes.png /usr/bin/notes.png
cd ~
rm -rf "~/Desktop/temp/"
```

- Run from source (Fast + Lightweight)

```bash
cd "~/Desktop/"
mkdir temp && cd temp
git clone https://github.com/hirusha-adi/Notes-QT.git
cd Notes-QT
sudo mv notes.py /usr/bin/notes
sudo cp notes.png /usr/bin/notes.png
cd ~
rm -rf "~/Desktop/temp/"
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

pyinstaller notes.py --onefile --noconfirm
# or
python3 -m PyInstaller notes.py --onefile --noconfirm

cd ./dist
sudo cp notes /usr/bin/notes
sudo cp notes.png /usr/bin/notes.png
cd ~
rm -rf "~/Desktop/temp/"
```

- Run from source (Fast + Lightweight)

```bash
cd "~/Desktop/"
mkdir temp && cd temp
git clone https://github.com/hirusha-adi/Notes-QT.git
cd Notes-QT
sudo mv notes.py /usr/bin/notes
sudo cp notes.png /usr/bin/notes.png
cd ~
rm -rf "~/Desktop/temp/"
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

# Screenshots (on Arch Linux with KDE Breeze Dark)

![image](https://user-images.githubusercontent.com/36286877/149811059-71a4d02d-cee7-4145-ae10-a1be8c0d519b.png)

<br>

- Change Font
<br>

![image](https://user-images.githubusercontent.com/36286877/149810619-1b4782b9-9c36-437a-a74d-58958f9f80f3.png)

- Print
<br>

![image](https://user-images.githubusercontent.com/36286877/149810774-8e3759ff-8933-49e7-8e69-3ec3e157c699.png)

- Print Preview
<br>

![image](https://user-images.githubusercontent.com/36286877/149810906-439d0591-c7d3-40e3-99ed-cfded510d54a.png)

- Save As
<br>

![image](https://user-images.githubusercontent.com/36286877/149810966-29d2522d-8713-4b61-8638-e67d80389be8.png)

