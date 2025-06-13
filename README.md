# Zettl CLI App

**Version 0.7.1**

This is a command-line interface (CLI) app for Zettelkasten-style note-taking and knowledge management. With this app, you can easily create, organize, and review notes using a simple and intuitive commands.

## Features

- Create new notes or folders with a specified title
- Update the index of all notes to ensure they are properly linked and organized
- Generate a list of review dates for all notes based on the spaced repetition method

## Installation

To install the app, first clone this repository to your local machine. Then, navigate to the root directory of the app in your terminal and run the following command to install it:
```
pip install .
```
This will install the app and all of its dependencies. After installation, you can use the zettl command to run the app from anywhere in your terminal.

## Usage

To use the app, open a terminal window and navigate to the root directory of your choice. Then, run the `zettl` command followed by one of the following subcommands:

- `init`: Initializes the app by creating a new Zettelkasten-style note-taking system.
- `new note`: Creates a new note and adds it to the notes directory. The user can specify the folder path and the title of the note.
- `new folder`: Creates a new folder and adds it to the directory. The user can specify the title of the folder.
- `update-index (upind)`: Updates the index of all notes to ensure that they are properly linked and organized.
- `update-review-schedule (uprev)`: Generates a list of review dates for all notes based on the spaced repetition method.

For more information on how to use each command, run the command followed by the `--help` option.

## License

This app is released under the MIT license. See `LICENSE` for more information.

