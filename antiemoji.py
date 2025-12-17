import re
import os

LANGUAGE_GROUPS = {
    "python": {
        "ext": [".py"],
        "single": [r"#.*"],
        "multi": [],
        "has_triple": True
    },
    "cstyle": {
        "ext": [".c", ".cpp", ".h", ".java", ".cs"],
        "single": [r"//.*"],
        "multi": [r"/\*[\s\S]*?\*/"],
        "has_triple": False
    },
    "script": {
        "ext": [".js", ".ts", ".php", ".go", ".rs"],
        "single": [r"//.*"],
        "multi": [r"/\*[\s\S]*?\*/"],
        "has_triple": False
    }
}

def remove_non_ascii(text):
    return re.sub(r"[^\x09\x0A\x0D\x20-\x7E]", "", text)

def remove_single_line_comments(text, patterns):
    for p in patterns:
        text = re.sub(p, "", text)
    return text

def remove_multiline_comments(text, patterns):
    for p in patterns:
        text = re.sub(p, "", text)
    return text

def remove_top_level_triple_quotes_python(text):
    lines = text.replace("\r\n", "\n").replace("\r", "\n").split("\n")
    result = []
    inside = False

    for line in lines:
        stripped = line.lstrip()
        indent = len(line) - len(stripped)

        if indent == 0 and (
            stripped.startswith("'''") or stripped.startswith('"""')
        ):
            inside = not inside
            continue

        if not inside:
            result.append(line)

    return "\n".join(result)

def normalize_blank_lines_smart(text, max_blank):
    lines = text.replace("\r\n", "\n").replace("\r", "\n").split("\n")
    result = []
    blank_count = 0

    for line in lines:
        if line.strip() == "":
            blank_count += 1
            if blank_count <= max_blank:
                result.append("")
            continue
        blank_count = 0
        result.append(line)

    while result and result[0] == "":
        result.pop(0)

    while result and result[-1] == "":
        result.pop()

    return "\n".join(result) + "\n"


def remove_all_triple_quotes_python(text):
    return re.sub(
        r'(?s)(\'\'\'|""").*?\1',
        "",
        text
    )


def clean_folder(folder, category, options):
    rules = LANGUAGE_GROUPS[category]

    for root, _, files in os.walk(folder):
        for file in files:
            if any(file.endswith(ext) for ext in rules["ext"]):
                process_file(os.path.join(root, file), category, rules, options)

def process_file(path, category, rules, options):
    with open(path, "r", encoding="utf-8", errors="ignore") as f:
        content = f.read()

    if options["emoji"]:
        content = remove_non_ascii(content)

    if category == "python" and options["triple"]:
        content = remove_all_triple_quotes_python(content)

    if options["multiline"]:
        content = remove_multiline_comments(content, rules["multi"])

    if options["single"]:
        content = remove_single_line_comments(content, rules["single"])

    content = normalize_blank_lines_smart(content, options["blank_lines"])

    with open(path, "w", encoding="utf-8") as f:
        f.write(content)


def main():
    print("=== Anti Emoji & AI Trace Cleaner ===")
    print("1. Python")
    print("2. C / C++ / Java / C# (Unity)")
    print("3. JS / TS / PHP / Go / Rust")

    choice = input("Select language category (1-3): ").strip()

    category_map = {
        "1": "python",
        "2": "cstyle",
        "3": "script"
    }

    category = category_map.get(choice)
    if not category:
        print("Invalid choice")
        return

    options = {
        "emoji": input("Remove emojis and non-ASCII characters? (y/n): ").lower() == "y",
        "triple": input("Remove top-level triple-quote blocks? (y/n): ").lower() == "y",
        "multiline": input("Remove multiline comments? (y/n): ").lower() == "y",
        "single": input("Remove single-line comments? (y/n): ").lower() == "y"
    }

    try:
        options["blank_lines"] = int(
            input("Max blank lines to keep (default 1): ").strip() or 1
        )
    except ValueError:
        options["blank_lines"] = 1

    folder = input("Folder to clean (default current): ").strip() or "."

    clean_folder(folder, category, options)
    print("Done. Cleaned safely.")

if __name__ == "__main__":
    main()
