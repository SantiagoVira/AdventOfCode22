with open("./Day1/input.txt", "r") as f:
  data = f.read().split("\n\n")
  groups = [[int(num) for num in group.split("\n")] for group in data]
  print(max([sum(group) for group in groups]))
  print(sum(sorted([sum(group) for group in groups], reverse=True)[:3]))
  # print(groups)
