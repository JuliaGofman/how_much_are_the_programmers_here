c = int(input())
n = c // 10
t = [1, 11, 21, 31, 41, 51, 61, 71, 81, 91]
if  n not in t and c==(n * 10 + 1) or c == 1:
  print(c, 'программист')
elif n not in t and (n * 10 + 2) <= c <= (n * 10 + 4):
  print(c, 'программиста')
else:
  print(c, 'программистов')