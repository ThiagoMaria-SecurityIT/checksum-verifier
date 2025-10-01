# SHA256 Checksum Verifier  

![Python Version](https://img.shields.io/badge/python-3.6%2B-blue)
![Platform](https://img.shields.io/badge/platform-windows-lightgrey)
![License](https://img.shields.io/badge/license-MIT-green)
![Status](https://img.shields.io/badge/status-stable-brightgreen)
![Made with AI Assistance](https://img.shields.io/badge/made_with-AI_assistance-8A2BE2)

A simple Python application with graphical interface to verify file integrity using SHA256 checksums. This tool helps ensure your downloaded files are authentic and not corrupted.  

<img width="1372" height="752" alt="image" src="https://github.com/user-attachments/assets/a204ee93-689a-4e96-a04c-24cef9c7b41f" />  

## What is Checksum Verification?

Checksum verification is a method to confirm that a file hasn't been tampered with or corrupted during download. It compares the cryptographic hash of your downloaded file with the official hash provided by the software developer.

## Features

- Calculate SHA256 hash of any file
- Three ways to get expected hash:
  - Manual input (copy-paste)
  - Download from official checksum URL
  - Load from local checksum file
- User-friendly graphical interface
- Supports large files
- Clear verification results

## Installation

### Prerequisites
- Python 3.6 or higher
- Windows operating system

### Steps
1. Download or clone this repository
2. Install required packages:
   ```bash
   pip install -r requirements.txt
   ```

## How to Use

### Basic Verification Process

1. **Start the application**:
   ```bash
   cd checksum-verifier
   python main.py
   ```

2. **Select your file**:
   - Click "Browse" and navigate to your downloaded file
   - Typically in your Downloads folder

3. **Calculate hash**:
   - Click "Calculate SHA256" to generate the file's hash

4. **Get expected hash** (choose one method):

   **Method 1: Manual Input**
   - Select "Manual input"
   - Copy the official hash from the developer's website
   - Paste it into the text field

   **Method 2: From URL**
   - Select "From URL"
   - Enter the checksum file URL (e.g., VirtualBox's SHA256SUMS)
   - Click "Load"
   - Select the correct filename from the list

   **Method 3: From File**
   - Select "From file"
   - Browse to select a downloaded checksum file
   - Click "Load"
   - Select the correct filename from the list

5. **Verify**:
   - Click "Verify Checksum"
   - Green background = successful verification
   - Red background = verification failed

## Example: Verifying VirtualBox Download

Let's verify a VirtualBox installation file:

1. Download VirtualBox from [official site](https://www.virtualbox.org/)
2. Run the checksum verifier
3. Select your downloaded file: `VirtualBox-7.2.2-170484-Win.exe`
4. Choose "From URL" method
5. Enter: `https://download.virtualbox.org/virtualbox/7.2.2/SHA256SUMS`
6. Click "Load"
7. From the list, select: `VirtualBox-7.2.2-170484-Win.exe`
8. Click "Verify Checksum"

The application will show whether your download matches the official checksum.

## Understanding the Results

- **Verification Successful**: Your file matches the official version exactly
- **Verification Failed**: The file may be corrupted, tampered with, or you selected the wrong checksum

## Common Issues

- **File not found**: Ensure the file path is correct
- **URL loading fails**: Check your internet connection and the URL
- **No checksums in file**: The loaded file may not contain valid checksum entries
- **Wrong checksum selected**: Make sure to select the filename that matches your downloaded file

## Technical Details

- Uses SHA256 cryptographic hash function
- Handles files of any size efficiently
- Supports standard checksum file formats
- Built with Python and tkinter

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Learning Resources

- [Understanding checksums](https://www.howtogeek.com/363735/what-is-a-checksum-and-why-should-you-care/)
- [Python hashlib documentation](https://docs.python.org/3/library/hashlib.html)
- [Tkinter GUI guide](https://docs.python.org/3/library/tkinter.html)

## 🤖 AI Transparency & Development Process

### Development Approach:
- **AI-Assisted Generation**: The initial code structure and implementation were generated with AI assistance
- **Human Oversight**: All generated code was reviewed, tested, and refined by a human developer
- **Educational Design**: The project was structured specifically for learning purposes
- **Quality Assurance**: The application has been tested to ensure it works as intended

### Why AI Transparency Matters:
We believe in being transparent about how software is created. While AI assisted in generating the initial code, human judgment was essential for:
- Code review and validation
- Testing and bug fixes
- Documentation and educational content
- Project structure decisions

### Verification:
This checksum verifier has been tested with real-world files and checksums to confirm it produces accurate results.

