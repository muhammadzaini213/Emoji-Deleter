import re

def filter_non_code_chars(text):
    allowed_pattern = re.compile(
        r"[^a-zA-Z0-9_"
        r"\s"
        r"\.\,\:\;\+\-\*\/\=\<\>\!\?\&\|\^\~"
        r"\(\)\[\]\{\}"
        r"\'\"\#\@\$\%\\]"
    )
    return allowed_pattern.sub("", text)

input_file = "input.py"
output_file = "output.py"

with open(input_file, "r", encoding="utf-8") as f:
    content = f.read()

filtered_content = filter_non_code_chars(content)

with open(output_file, "w", encoding="utf-8") as f:
    f.write(filtered_content)

print("Karakter non-kode berhasil difilter")


