# Setup

This folder contains instructions on how to install Pygame and test if everything is working correctly.

## Installing Pygame
### **Windows Users**
If you are using Windows, you should use the `py` command to ensure you install Pygame for the correct Python version:
```cmd
py -m pip install pygame
```
### **Mac/Linux Users**
Mac and Linux users can use:
```bash
pip install pygame
```

## Running the Test Script
### **Windows Users**
To check if Pygame is installed correctly, navigate to this folder and run:
```cmd
py test_pygame.py
```
### **Mac/Linux Users**
```bash
python test_pygame.py
```
If everything is set up correctly, you should see:
```
Pygame is working!
```

If you encounter errors, ensure:
- **Python is installed** (`py --version` or `python --version`)
- **Pygame is installed correctly** (`py -m pip show pygame` or `pip show pygame`)
- **You try reinstalling** (`py -m pip install --upgrade pygame` or `pip install --upgrade pygame`)