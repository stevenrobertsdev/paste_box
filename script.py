import sys
import pyperclip
import os
import json
import datetime

file = 'data.json'

def load_data():
    if os.path.exists(file):
        with open(file, 'r') as f:
            try:
                return json.load(f)
            except json.JSONDecodeError:
                return []
    return None


def check_for_duplicates(dt, t):
    for e in dt:
        if e['title'] == t:
            return True
    return None


def add_content(dt, t, c):
    dt.append({"title": t, "content": c, "date": datetime.datetime.now().date().isoformat()})
    with open(file, "w") as fl:
        json.dump(dt, fl, indent=4)
    print(f"Title: {t}\nContent: {c}\nhas been added to paste box")


def list_entries(dt):
    print("List all entries")
    for e in dt:
        print(e)


def paste_entry(dt):
    print("Paste your content (Ctrl+Z then Enter to end on Windows):")
    content = sys.stdin.read().strip()

    title = input("Enter a title:\n> ").strip()

    while check_for_duplicates(dt, title):
        title = input(f"Title '{title}' already exists. Try another:\n> ").strip()

    add_content(dt, title, content)


def copy_entry(dt):
    title = input("Enter title to copy:\n> ").strip()
    while True:
        for e in dt:
            if e['title'] == title:
                pyperclip.copy(e['content'])
                print(f"✅ Copied '{title}' to clipboard.")
                return
        title = input(f"Not found. Try another title:\n> ").strip()


def main():
    if len(sys.argv) < 2:
        print("Usage: python script.py [p|c|l]")
        return

    action = sys.argv[1]
    data = load_data()

    if action == 'l':
        list_entries(data)
    elif action == 'c':
        copy_entry(data)
    elif action == 'p':
        paste_entry(data)
    else:
        print(f"Unknown action: {action}")


if __name__ == "__main__":
    main()




