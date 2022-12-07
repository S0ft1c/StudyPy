def sortSwap(a):
  n = len(a)
  for i in range(n - 1):
    b = []
    b = a[i:n]
    index = b.index(min(b)) + i
    a[index], a[i] = a[i], a[index]
  return a


# ppo_10_11915
# pepXUFb3Rm

upSpd, downSpd, need = int(input()), int(input()), int(input())
now = 0
idx = 0

while now != need:
  idx += 1
  now += upSpd
  if now >= need:
    break
  now -= downSpd
print(idx)
    