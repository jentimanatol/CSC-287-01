# Open the file and read everything in one big gulp.
with open('./test.txt', encoding="utf-8") as f:
    content = f.read()

print(content)
