# 📋 Paste Box CLI

A simple command-line tool for managing and retrieving reusable text snippets. Paste Box lets you quickly store, copy, and list chunks of content via the terminal. Ideal for developers, writers, or anyone who works with repeated text.

---

## Features

- Add content with a title  
- Copy content to your clipboard by title  
- List all saved entries with timestamps  
- Automatically saves and loads content from a local `data.json` file

---

## Requirements

- Python 3.7+
- [pyperclip](https://pypi.org/project/pyperclip/)  
  Install with:

  ```bash
  pip install pyperclip
  ```
  
---
## Installation
Clone the repo or copy script.py to your local machine:

 ```bash
git clone https://github.com/stevenrobertsdev/pastebox-cli.git
cd pastebox-cli
```
Install the required dependency:

 ```bash
pip install pyperclip
```
---

## Usage
Run the script from your terminal using Python:
```bash
python script.py [action]
```
Where [action] is one of the following:

### Paste new content
Prompts you to paste content directly into the terminal and then provide a title.

```bash
python script.py p
````
Paste multiple lines.

On Windows, press Ctrl + Z then Enter to finish pasting.

On Mac/Linux, press Ctrl + D.

You'll then be asked to enter a unique title. The content will be saved under this title.

### Copy content to clipboard
```bash
python script.py c
```
Prompts you to enter the title of the saved content.

If found, the associated content will be copied to your clipboard.

### List all stored content
```bash
python script.py l
```
Outputs a list of all saved entries, including their title, content, and date.

---

## Data Storage
All content is stored locally in a file named data.json in the same directory as the script.

Each entry includes:
```bash
{
  "title": "Example Title",
  "content": "Your saved text content...",
  "date": "2025-07-26"
}
```
## Notes
Titles must be unique — you'll be prompted to choose another if a duplicate is found.

If data.json does not exist, it will be created automatically the first time you add content.

---


## To Do
Add support for deleting entries

Add filtering/search functionality

Export to markdown or CSV

Enhance clipboard compatibility for multiline content

---

## Licence
This project is released under the MIT Licence.

---

Made with ☕ by Steven