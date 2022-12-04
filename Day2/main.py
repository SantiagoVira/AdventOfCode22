def getWinner(userChoice, computerChoice):
    diff = userChoice - computerChoice;
    if (diff == 0):
      return 3
    if (diff == 1 or diff == -2):
      return 6
    return 0

with open("./Day2/input.txt") as f:
  data = f.readlines()
  total = 0

  # num_vals = {"A": 1, "B" : 2, "C": 3, "X": 1, "Y": 2, "Z": 3}
  # total = 0
  # for round in data:
  #   [opp, me] = [num_vals[letter.replace("\n", "")] for letter in round.split(" ")]
  #   total += me + getWinner(me, opp)
  # print(total)

  num_vals = {"A": 1, "B" : 2, "C": 3, "X": 1, "Y": 2, "Z": 3}
  outcome = {
    "X" : 0,
    "Y" : 3,
    "Z" : 6,
  }
  to_defeater = {
    "A" : 2,
    "B" : 3,
    "C" : 1
  }
  to_beater = {
    "A": 3,
    "B": 1,
    "C": 2
  }

  for round in data:
    [opp, verdict] = [letter.replace("\n", "") for letter in round.split(" ")]
    me = to_defeater[opp] if verdict == "Z" else num_vals[opp] if verdict == "Y" else to_beater[opp]
    total += me + outcome[verdict]
    
  print(total)
