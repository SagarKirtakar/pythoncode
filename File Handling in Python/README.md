# 🐍 File Handling in Python

A beginner-friendly Python project demonstrating file handling operations including creating, reading, writing, appending, renaming, and deleting files.

---

## 👤 Author

**Sagar Kirtakar**
📅 Date: 2026-06-14

---

## 📋 Table of Contents

- [About](#about)
- [Features](#features)
- [File Modes](#file-modes)
- [Getting Started](#getting-started)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [What I Learned](#what-i-learned)

---

## 📖 About

This project covers the basics of File Handling in Python — one of the most essential skills in programming. It demonstrates how to open, read, write, append, rename, and delete files using Python's built-in functions.

---

## ✨ Features

- ✅ Write data to a file
- ✅ Append data to an existing file
- ✅ Read data from a file
- ✅ Rename a file using os.rename()
- ✅ Delete a file using os.remove()
- ✅ Error handling with try/except for FileNotFoundError
- ✅ Uses with statement for safe file handling (auto-close)

---

## 📂 File Modes

| Mode | Description |
|------|-------------|
| r    | Read — opens file for reading (default) |
| w    | Write — creates or overwrites the file |
| a    | Append — adds content to end of file |
| r+   | Read & Write — file must exist |
| w+   | Write & Read — creates or overwrites |
| a+   | Append & Read |

---

## 🚀 Getting Started

### Prerequisites

- Python 3.x installed
- VS Code (recommended)

### Installation

1. Clone the repository:

git clone https://github.com/SagarKirtakar/pythoncode.git

2. Navigate to the project folder:

cd pythoncode

3. Run the script:

python first.py

---

## 💻 Usage

# Write to a file
write_to_file('file1.txt', name)

# Append to a file
append_to_file('file1.txt', name)

# Read from a file
read_from_file('file1.txt')

# Rename a file
os.rename('file1.txt', 'file2.txt')

# Delete a file
os.remove('file2.txt')

---

## 📁 Project Structure

File Handling In Python/
│
├── first.py        # Main Python script
├── file1.txt       # Generated file (after running script)
└── README.md       # Project documentation

---

## 📚 What I Learned

- How to open and close files in Python
- Different file opening modes (r, w, a)
- Using the with statement for safe file handling
- Handling FileNotFoundError using try/except
- Renaming and deleting files using the os module

---

## 🛠️ Built With

- Python 3
- VS Code
- Git & GitHub

---

"The best way to learn programming is by writing code every day!"