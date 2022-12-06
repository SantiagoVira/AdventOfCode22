import numpy as np, re

# Part 1 - RFFFWBPNS
# Part 2 - CQQBBJFCS

with open("./Day5/input.txt") as f:
  data = f.readlines()

new_arr = []
for row in data[:8]:
  new_row = [row[4*i+1] for i in range(9) ]
  new_arr.append(new_row)

clean_arr = lambda a: [[val for val in row if val != ' '] for row in a]

arr = np.array(new_arr).transpose()
new_arr = clean_arr(arr)

for cmd in data[10:]: 
  # move 2 from 7 to 2
  # ^ move 2 boxes from row 7 to 2
  [count, from_, to] = [int(num) for num in re.findall("\d+", cmd)]
  from_ -= 1
  to -= 1
  new_arr[to] = new_arr[from_][:count] + new_arr[to]
  new_arr[from_] = new_arr[from_][count:]

print("".join([row[0] if row[0] else " " for row in new_arr]))
