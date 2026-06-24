with open("input.txt", "r", encoding="utf-8") as f:
    lines = f.readlines()

cleaned_lines = []

i = 0
while i < len(lines):
    line = lines[i].strip()

    # Muster für Zeit in Zahlen (z.B. 0:06 oder 2:10)
    if ":" in line and line.replace(":", "").isdigit():
        # nächsten Eintrag überspringen (Fließtext-Timestamp)
        i += 2
        continue

    cleaned_lines.append(lines[i])
    i += 1

with open("output.txt", "w", encoding="utf-8") as f:
    f.writelines(cleaned_lines)

print("Fertig!")