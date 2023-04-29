data = input().split(chr(92))
splitting = data[-1].split(".")

print(f"File name: {splitting[0]}\nFile extension: {splitting[1]}")
