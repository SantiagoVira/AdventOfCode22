from string import ascii_letters
with open("./Day3/input.txt") as f:
  data = f.readlines()
  total = 0
  # for line in data:
  #   half_idx = len(line) // 2
  #   half_1, half_2 = line[:half_idx], line[half_idx:]
  #   for char in half_1:
  #     if char in half_2:
  #       total += ascii_letters.index(char) + 1
  #       break
  for i in range(len(data) // 3):
    lines = data[3 * i : 3 * i + 3]
    for char in lines[0]:
      if char in lines[1] and char in lines[2]:
        total += ascii_letters.index(char) + 1
        break
  print(total)
    

