## Emoji & Non-Code Character Filter

A simple Python script for people who get in trouble because of emojis.

This script removes emojis and other non-code Unicode characters from a Python source file, keeping only characters commonly used in programming.

### Why this exists

Sometimes you are just using AI for assignments.
Sometimes the code works perfectly.
Sometimes an emoji shows up and causes unnecessary questions from your lecturer.

This script fixes that.

### Requirements

* Python 3.x
* No external libraries required

### How to Use

1. Put your source file in the same directory as the script
   Rename it to:

   ```
   input.py
   ```

2. Run the script:

   ```
   python antiemoji.py
   ```

3. The cleaned result will be saved as:

   ```
   output.py
   ```

### What Gets Removed

* Emojis
* Non-ASCII Unicode characters
* Invisible or stray characters from copy-paste
* Any character not commonly used in programming

### What Stays Safe

* Letters and numbers
* Whitespace
* Operators and symbols
* Brackets and quotes
* Valid Python syntax

### Notes

* This is a **character-level filter**, not a parser.
* Use it for cleanup, preprocessing, or peace of mind.
* Ideal for fun projects, AI-generated code, or last-minute sanity checks.

### Disclaimer

Use responsibly.
This script removes characters, not your responsibility as student.

---