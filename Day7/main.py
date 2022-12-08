import re

with open("./Day7/input.txt") as f:
  data = f.readlines()

class Dir:
  def __init__(self, name, size = 0, parent = None):
    self.name = name
    self.size = size
    self.parent = parent
    self.children = []
  
  def add_child(self, name):
    self.children.append(Dir(name, parent=self))
    return self.children[-1]
  
  def update_size(self, size):
    self.size += size
    if self.parent:
      self.parent.update_size(size)

  def __str__(self):
    return f"{self.name} (size: {self.size})"

root = Dir("/")
current = root

for cmd in data[1:]:
  if cmd.startswith("$ cd"):
    if ".." in cmd:
      current = current.parent
    else:
      current = current.add_child(cmd[4:].strip())
  elif (size := re.search("^\d+", cmd)):
    # file
    current.update_size(int(size.group(0)))

def print_tree(dir, depth=0):
  print("  " * depth + str(dir) )
  for child in dir.children:
    print_tree(child, depth + 1)

total = 0
def calculate_total(dir):
  global total
  total += dir.size if dir.size < 100000 else 0

  for child in dir.children:
    calculate_total(child)

best = -1
def calculate_best(dir):
  global best
  if best == -1 or dir.size > root.size - 40000000 and dir.size < best:
    best = dir.size

  for child in dir.children:
    calculate_best(child)

calculate_total(root)
print(total)
calculate_best(root)
print(best)