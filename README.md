# YT-dlp-GUI

Welcome to **YT DLP GUI**,the easiest GUI for yt-dlp.

## Supported Platforms

- **Operating System:** Windows 10/11

## Build Guide

### Prerequisites:

1. **Python**: Ensure Python is installed on your system. You can download it from [python.org](https://www.python.org/downloads/release/python-31011/) and follow the installation instructions for your operating system.

2. **Git**: Install Git if you haven't already. You can download Git from [git-scm.com](https://git-scm.com/downloads) and follow the installation instructions.

### Steps to Clone and Build the Project:

1. **Clone the Repository**:
   Open a terminal or command prompt and clone the repository using Git:

   ```bash
   git clone https://github.com/diamond261/YT-DLP-GUI.git
   ```

2. **Navigate to the Project Directory**:
   Change into the directory of the cloned repository:

   ```bash
   cd YT-DLP-GUI
   ```

3. **Install Poetry and Pyinstaller**:
   It's will help you to esay to build:

   ```bash
   pip install poetry pyinstaller
   ```

4. **Configure with Poetry**:
   Run Poetry to configure the build environment. :

   ```bash
   poetry install
   ```

   This command generates the necessary build files based on the Poetry configuration.

5. **Build the Project**:
   Once Poetry has configured the build files successfully, you can build the project using a suitable build tool (like Pyinstaller, nuitka and flet):
   > > > > > > > my-feature
