# File Sorter

**File Sorter is a simple Python script designed to automatically clean up and organize clutter in your folders.**

It scans a directory of your choice, identifies file extensions, and moves files into organized subfolders like `IMAGES`, `DOCUMENTS`, `VIDEO`, `CODE`, and more. If a file format is not recognized, it goes straight to an `UNKNOWN` folder. Additionally, if two files share the same name, the script safely renames the new one to prevent overwriting your data.

---

## Features
* **Automatic Categorization:** Groups files into 15+ predefined categories (Images, Audio, Documents, Archives, etc.).
* **No Overwriting:** Automatically adds numbers to duplicate filenames to keep all your files safe.
* **Cross-Platform:** Works seamlessly on Windows, macOS, and Linux.
* **Lightweight:** Uses only built-in Python modules (`os` and `shutil`), so no external libraries are needed.

---

## Prerequisites

Before running the script, make sure you have Python installed on your system.
* You can check your Python version by running:
  ```bash
  python --version
  ```
  *(Note: On macOS and Linux, you might need to use `python3 --version` instead).*

---

## How to Install and Run

### 🛠️ For Windows

1. **Download the Script:**
   Clone this repository or download the `main.py` file directly.
2. **Open Command Prompt:**
   Press `Win + R`, type `cmd`, and press Enter. Navigate to the folder where you saved the script:
   ```cmd
   cd path\to\your\downloaded\script
   ```
3. **Run the Script:**
   ```cmd
   python main.py
   ```

### 🍏 For macOS

1. **Download the Script:**
   Clone the repository or download the `main.py` file.
2. **Open Terminal:**
   Press `Cmd + Space`, type `Terminal`, and press Enter. Navigate to the folder with the script:
   ```bash
   cd path/to/your/downloaded/script
   ```
3. **Run the Script:**
   ```bash
   python3 main.py
   ```

### 🐧 For Linux

1. **Download the Script:**
   Clone the repository or download `main.py` via your terminal.
2. **Open Terminal and Navigate:**
   ```bash
   cd path/to/your/downloaded/script
   ```
3. **Run the Script:**
   ```bash
   python3 main.py
   ```

---

## How to Use

1. Launch the script using the instructions above.
2. The terminal will display a greeting message: `- hello, this is SORTER`.
3. Paste or type the **full path** of the directory you want to clean up when prompted:
   ```text
   What folder do you want to sort (insert full path): 
   ```
4. Press Enter. Your files will be instantly sorted into structured folders!

