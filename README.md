# python-clipboard-stack

A simple Python CLI app that simulates copy-paste (clipboard) functionality using a stack data structure. Copy multiple pieces of text, view them, delete specific ones, or clear everything — all from the terminal.

## What is this?

This project mimics a clipboard manager: instead of your system clipboard holding just one item, this stack can hold **multiple copied items** at once, and lets you manage them (view, paste, delete individually or all at once).

## Features

- **Copy** — save any text you type into the stack
- **Paste** — view the most recently copied item
- **Delete** — pick a specific item from the list and remove it
- **Show all items** — list everything you've copied so far
- **Delete all** — clear the entire list (with a yes/no confirmation)
- **Clipboard** — pick any item from the list and paste it (not just the last one)
- **Paste all** — print every copied item at once, separated by commas

## How to run it

1. Make sure you have Python 3 installed.
2. Download or clone the repository:
   ```bash
   git clone https://github.com/soshjant/python-clipboard-stack.git
   ```
3. Run the script:
   ```bash
   python stack_clipboard.py
   ```

## How to use it

Once running, you'll see a menu like this:

```
what do you want to do ?

1.copy
2.paste
3.delete
4.show_all_items
5.delete_all
6.clipboardl
7.paste_all
8.exit
answer :
```

Type the number of the action you want and press Enter. The program keeps running in a loop until you choose **8** to exit.

### Example session

```
answer : 1
write anything that you want to copy:
Hello World
['Hello World'] HAS BEEN COPIED

answer : 1
write anything that you want to copy:
Second item
['Hello World', 'Second item'] HAS BEEN COPIED

answer : 4
1.Hello World
2.Second item

answer : 3
all your items that you copied :
1. Hello World
2. Second item
which one you want to delete ? 1
item has been deleted : Hello World

answer : 8
the work has been finished
```

## Menu reference

| Option | Action |
|---|---|
| 1 | Copy a new text and add it to the list |
| 2 | Paste (show) the last copied item |
| 3 | Show all items and delete a chosen one by its number |
| 4 | Show all items currently saved |
| 5 | Delete all items (asks for confirmation) |
| 6 | Show all items and paste a chosen one by its number |
| 7 | Paste (print) all items at once |
| 8 | Exit the program |

## Notes

- All data is stored **in memory only** — once you exit the program, the copied items are lost. There is no file-saving feature (yet).
- This project was built as an exercise to practice classes, loops, and basic data validation in Python.

## License

Feel free to use, modify, and learn from this code.
