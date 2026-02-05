# shraddha-zagade-final-task
# 📘 Text Processing Toolkit

## 📌 Project Overview

This project contains three simple Python utilities for cleaning and
processing text and JSON data.\
It is useful for beginners learning **text preprocessing, data cleaning,
and basic NLP tasks**.

### Tools Included

-   Text Cleaner
-   JSON Preprocessor
-   Tokenizer

------------------------------------------------------------------------

## ⚙️ Requirements

-   Python 3.x
-   Only built-in libraries (no external packages)

------------------------------------------------------------------------

## 📂 Project Files

### 1. text_cleaner.py

Cleans and formats text: - Removes extra spaces - Removes special
characters - Converts text to lowercase

### 2. json_preprocessor.py

Cleans JSON-like data: - Normalizes dictionary keys - Converts keys to
lowercase - Replaces spaces/dashes with underscores - Removes `None`
values

### 3. tokenizer.py

Analyzes text: - Splits text into words - Counts words - Creates word
frequency map

------------------------------------------------------------------------

# ▶️ How to Run the Programs

Open terminal inside the project folder and run:

``` bash
python text_cleaner.py.py
python json_preprocessor.py.py
python tokenizer.py.py
```

------------------------------------------------------------------------

# 🧹 Text Cleaner

## Methods

-   `remove_extra_space(text)` → removes spaces
-   `remove_special_characters(text)` → keeps only letters & numbers
-   `normalize_case()` → converts to lowercase

## Example

Input:

    Hello  World!! Welcome@123

Output:

    helloworldwelcome123

## Usage

``` python
from text_cleaner import text_cleaner

cleaner = text_cleaner()
cleaner.remove_extra_space(text)
cleaner.remove_special_characters(text)
cleaner.normalize_case()
```

------------------------------------------------------------------------

# 🗂️ JSON Preprocessor

## Methods

-   `normalize_keys(json_obj)` → cleans keys
-   `strip_nulls(json_obj)` → removes None values

## Example

Input:

``` python
{
 " User Name ": "Alice",
 "Age": None
}
```

Output:

``` python
{'user_name': 'Alice'}
```

## Usage

``` python
from json_preprocessor import JsonPreprocessor

processor = JsonPreprocessor()
result = processor.strip_nulls(processor.normalize_keys(data))
print(result)
```

------------------------------------------------------------------------

# 🔤 Tokenizer

## Methods

-   `tokenize(text)` → split into words
-   `word_count(text)` → count words
-   `frequency_map(text)` → count occurrences

## Example

Input:

    hello world hello

Output:

    Tokenize: ['hello', 'world', 'hello']
    Word Count: 3
    Frequency Map: {'hello': 2, 'world': 1}

## Usage

``` python
from tokenizer import TextTools

tools = TextTools()
print(tools.tokenize(text))
print(tools.word_count(text))
print(tools.frequency_map(text))
```

------------------------------------------------------------------------

# 🎯 Use Cases

-   Cleaning user input
-   Preparing API/JSON data
-   Text analysis
-   Beginner NLP practice
-   Academic mini-projects

------------------------------------------------------------------------

# 🚀 Future Improvements

-   File input/output support
-   Better punctuation handling
-   Stop-word removal
-   Combine all tools into one package

------------------------------------------------------------------------

## 👩‍💻 Author

Created for learning and practice in Python text processing.
