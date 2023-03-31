# Question 10

s = input()
I_r = 2
M_r = 1
C_r = 3
W_r = 1

for i in range(len(s)):
  if s[i] == "I":
    I_r -= 1
  elif s[i] == "M":
    M_r -= 1
  elif s[i] == "C":
    C_r -= 1
  else:
    W_r -= 1

if I_r != 0:
  print("I")
elif M_r != 0:
  print("M")
elif C_r != 0:
  print("C")
else:
  print("W")
