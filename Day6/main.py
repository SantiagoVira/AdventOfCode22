with open("./Day6/input.txt") as f:
  data = f.read()

processed = ""
num = 0

for char in data:
  num += 1
  processed += char

  if len(set(processed[-14:])) == 14:
    break

print(len(data))
print(num)