## Emoji & AI Trace Cleaner

A simple Python CLI tool for people who get in trouble because of emojis, comments, or obvious AI traces.

This tool cleans source code by removing emojis, non-ASCII characters, comments, docstrings, and excessive blank lines, while keeping valid programming syntax intact.

Designed for students, small projects, and anyone who wants their code to look clean, human, and boring in a good way.

---

### Why This Exists

Sometimes you are just using AI for assignments.
Sometimes the code works perfectly.
Sometimes an emoji, comment, or weird spacing raises unnecessary questions.

This tool fixes that.

---

### Features

* Remove emojis and non-ASCII characters
* Remove single-line comments
* Remove multi-line comments
* Remove Python docstrings and triple-quote blocks
* Normalize excessive blank lines with configurable tolerance
* Clean an entire folder recursively
* Language-aware behavior with safe presets

---

### Supported Languages

Grouped for safety and simplicity.

**Python**

* `.py`
* `#` comments
* `''' '''` and `""" """` docstrings

**C-Style Languages**

* C / C++ / Java / C# (Unity)
* `//` single-line comments
* `/* */` multi-line comments

**Script Languages**

* JavaScript / TypeScript / PHP / Go / Rust
* `//` and `/* */`

---

### Requirements

* Python 3.x
* No external libraries required

---

### How to Use

1. Place the script anywhere you like.

2. Run it from terminal:

   ```
   python antiemoji.py
   ```

3. Follow the interactive prompts:

   * Choose language category
   * Choose what to remove
   * Set maximum allowed consecutive blank lines
   * Select target folder (default is current folder)

4. Files are cleaned **in place**.

---

### Blank Line Normalization

You can control how many consecutive blank lines are allowed.

Examples:

* `0` → no blank lines
* `1` → compact but readable
* `2` → relaxed formatting

Leading and trailing blank lines are always removed.

---

### What Gets Removed

* Emojis
* Non-ASCII Unicode characters
* AI-style comments and docstrings
* Multi-line comment blocks
* Excessive blank lines
* Copy-paste artifacts

---

### What Stays Safe

* Code structure
* Indentation
* Keywords and identifiers
* Operators and symbols
* Valid syntax for supported languages

---

### Notes

* This is **not a parser**, it is a controlled text cleaner.
* Designed to be predictable and deterministic.
* Best used before submission, review, or version control.

---

### Disclaimer

Use responsibly.
This script removes characters, not your responsibility.

---