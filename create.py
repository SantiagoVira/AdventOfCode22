import os

for i in range(10, 26):
  day_str = f"Day{i}"

  os.mkdir(day_str)
  os.chdir(day_str)
  with open('input.txt', "x") as f:
    pass
  with open('main.py', 'w') as f:
    f.write(f'with open("./{day_str}/input.txt") as f:\n  data = f.readlines()\n')
  
  os.chdir("../")