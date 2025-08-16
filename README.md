# Xcommand
📌 Overview

The Command Executor Tool is a cross-platform command execution application built with Python (Tkinter).
It provides a graphical interface for entering and running system commands, while displaying real-time output logs inside the app.

This tool can detect the current operating system (Windows, Linux, or macOS) and only allows execution of commands that match the current platform, preventing misuse across incompatible systems.

⚙️ Key Features

Cross-Platform Support

Detects whether you are on Windows, Linux, or macOS.

Provides a dropdown menu to select the target system.

Command Execution

Input system commands directly into the GUI.

Executes them using Python’s subprocess.run() function.

Captures both standard output and error messages.

Error Handling & Safety

Prevents execution if the selected system does not match the current one.

Logs warnings (e.g., trying to run Linux commands on Windows).

Catches runtime errors during command execution.

User-Friendly Interface

Built with Tkinter for simplicity.

Includes:

Dropdown menu for system selection.

Text entry box for entering commands.

Execute button to run commands.

Scrollable text area for displaying logs and outputs.

🖥️ How It Works

System Detection

At startup, the app checks the OS using sys.platform.

Maps the result to "Windows", "Linux", or "macOS".

Sets this as the default target system in the dropdown menu.

Command Input

User types a command into the entry field (e.g., dir on Windows or ls -l on Linux).

Command Execution

When "Execute Command" is clicked, the app:

Compares the selected system with the current system.

If they match → executes the command with subprocess.run().

If not → logs a warning and does not run the command.

Output Logging

Standard output (stdout) is displayed in the scrollable text box.

Error messages (stderr) are also displayed, highlighted as errors.

📖 Example Usage

On Windows

Select system: Windows.

Enter command: dir.

Output: lists files in the current directory.

On Linux/macOS

Select system: Linux or macOS.

Enter command: ls -l.

Output: detailed file listing.

If mismatch occurs

Current system: Windows.

Selected system: Linux.

Command: ls -l.

Result:

Warning: Current system is Windows, cannot execute Linux commands.

📂 Project Structure
command.py        # Main application file

🚀 Summary

The Command Executor Tool is a simple yet powerful cross-platform utility for running system commands through a graphical interface.
It’s especially useful for:

Beginners learning system commands.

Developers testing commands in a safe, controlled way.

Quickly executing shell commands without leaving a GUI environment.
