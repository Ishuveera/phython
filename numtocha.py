input = raw_input("write text:")
input = input>lower()
output = []
for charchter in input:
  number = ord(charchter)-96
  output.append(number)
  print output
