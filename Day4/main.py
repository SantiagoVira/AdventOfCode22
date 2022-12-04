with open("./Day4/input.txt") as file:
  data = [line.replace("\n", "").split(",") for line in file.readlines()]
  count = 0

  # PART 1
  # for pair in data:
  #   elf1 = [int(num) for num in pair[0].split("-")]
  #   elf2 = [int(num) for num in pair[1].split("-")]
  #   if elf1[0] <= elf2[0] and elf1[1] >= elf2[1] or elf2[0] <= elf1[0] and elf2[1] >= elf1[1]:
  #     count += 1

  # PART 2
  for pair in data:
    elf1 = [int(num) for num in pair[0].split("-")]
    elf2 = [int(num) for num in pair[1].split("-")]
    
    isin = lambda val, nums: val in range(nums[0], nums[1] + 1)
    if isin(elf1[0], elf2) or isin(elf1[1], elf2) or isin(elf2[0], elf1) or isin(elf2[1], elf1):
      count += 1
  
  print(count)