# Installation

If you want to work on your game projects at home, follow this guide to ensure your computer is setup with the necessary software.

This tutorial will walk you through installing:

- Python
- Visual Studio Code
- and pygame

---

## **Step 1: Install Python**

Python is the most popular programming language and was designed to be easy to use and learn. It is used in every industry, including game development.

### **Download and Install Python**
1. Go to the official Python website: [https://www.python.org/downloads/](https://www.python.org/downloads/)
2. Download the latest version for your operating system (Windows/Mac/Linux).
3. Open the installer and check the box that says **"Add Python to PATH"** before clicking **Install Now**.

![Python Installer with Add to PATH Checked](placeholder-python-installer.png)
*Alt text: Screenshot of the Python installer with the "Add Python to PATH" option checked.*

:::info
If you forget to check "Add Python to PATH," you may have trouble running Python from the command line. The easiest fix is to reinstall Python and check the box that adds Python to the PATH.
:::

---

## **Step 2: Install Visual Studio Code**

Visual Studio Code is the most popular text editor for software and game developers.

### **Download and Install VS Code**
1. Go to the official VS Code website: [https://code.visualstudio.com/](https://code.visualstudio.com/)
2. Download the installer for your operating system.
3. Run the installer and follow the setup instructions.

![Visual Studio Code Download Page](placeholder-vscode-download.png)
*Alt text: Screenshot of the VS Code download page with options for different operating systems.*

### **Enable Python Extension in VS Code**
Once VS Code is installed:
1. Open VS Code.
2. Go to the **Extensions Marketplace** (Ctrl+Shift+X or Cmd+Shift+X on Mac).
3. Search for **Python** and install the **Python extension** by Microsoft.

![VS Code Extensions Marketplace](placeholder-vscode-extensions.png)
*Alt text: Screenshot of the VS Code Extensions Marketplace with the Python extension selected.*

:::tip
The Python extension provides syntax highlighting and type-ahead suggestions, making it easier to write and debug Python code inside Visual Studio Code.
:::

---

## **Step 3: Using the Terminal in Visual Studio Code**

A "terminal" is just a place where you can type commands for your computer to run. It may look a little scary at first, but don't worry—it’s just like giving your computer instructions!

### **Opening the Terminal**
Instead of using a separate terminal window, always use the terminal inside **Visual Studio Code**:
1. Open **VS Code**.
2. Click on **Terminal** in the top menu.
3. Select **New Terminal**.
4. A panel will open at the bottom where you can type commands.

![Opening the Terminal in VS Code](placeholder-vscode-terminal.png)
*Alt text: Screenshot of Visual Studio Code with the terminal panel open.*

This is where you will type commands to install Pygame and run your code!

---

## **Step 4: Validate Your Python Installation**

In the **VS Code Terminal**, type:

#### **Windows**
```bash
py --version
```

#### **Mac/Linux**
```bash
python --version
```

:::tip
On some Macs, your Python command might be `python3`. If you are having trouble, try `python3 --version`.
:::

If Python is installed correctly, you should see the version number displayed.

---

## **Step 5: Install Pygame**

Python is a general-purpose programming language. To create games, we need to install a module called `pygame`. This module makes it easy to write games using Python!

### **Installing Pygame**

In the **VS Code Terminal**, type:

#### **Windows (using `py`)**
```cmd
py -m pip install pygame
```

#### **Mac/Linux**
```bash
pip install pygame
```

:::tip
On some Macs, your `pip` command might be `pip3`. If you are having trouble, try `pip3 install pygame`.
:::

### **Verify Installation**
To check if Pygame is installed correctly, type this command in the **VS Code Terminal**:

#### **Windows**
```cmd
py -m pygame.examples.aliens
```

#### **Mac/Linux**
```bash
python -m pygame.examples.aliens
```

If Pygame is installed correctly, a game window should appear.

:::tip
If you encounter errors, try these troubleshooting steps:
- **Check Pygame installation:** Run `py -m pip show pygame` or `pip show pygame`.
- **Reinstall Pygame:** Run `py -m pip install --upgrade pygame` or `pip install --upgrade pygame`.
:::

---



