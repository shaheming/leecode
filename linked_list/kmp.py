
t = "abcabcababc"
s = "abcabcabcabcababc"
Next = [0 for _ in range(len(t))]
nt = len(t)
j = 0
i = 1
while i < nt:
    if t[j] == t[i]:
        while j < nt and i < nt and t[j] == t[i]:
            Next[i] = j+1
            j += 1
            i += 1
        j = 0
        i -= 1
    else:
        i += 1
j, i = 0, 0
while i < len(s) and j < len(t):
  if t[j] == s[i]:
    while i < len(s) and j < len(t) and t[j] == s[i]:
        j += 1
        i += 1
    if j == len(t):
      print(i)
      exit(0)
    i = i - j + Ne·xt[j]
  i+=1

print("end")


print(Next)
# [0, 0, 0, 0, 1, 2, 3, 4, 5, 1, 2, 3]
