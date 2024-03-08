# SearchUtils

SearchUtils is a Python utility for searching strings in files within a specified directory.

## Features

- Search for a specific string within files in a directory.
- Display matched lines along with file paths and line numbers.
- Support for searching both text and binary files.
- Optional quiet mode to suppress detailed output.

## Installation

Install SearchUtils using pip:

```bash
pip install SearchUtils
```


## Basic Usage

1 - To search for a string within files in a directory, use the following command:

```bash
$ search-utils --indir /path/to/directory --text "your_search_string"
```
2 - To search for a string in a file, use the following command:

```bash
$ search-utils --indir /path/to/directory/file.txt --text "your_search_string"
```
3 - To search for a string and only get the return code, use the following command:

```bash
$ search-utils --indir /path/to/directory --text "your_search_string"
```

Options
* **--indir**: Specify the directory to search.
* **--text**: Specify the search string.
* **--quiet**: Optional. Suppress detailed output.

