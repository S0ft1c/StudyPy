# 3-d task Informatics 1-st part predprof
# s = "0123456789ABC"
# for x in s:
#   if int(x+"1418", 13) + int("1"+x+"037", 14) == int("2"+x+"209", 19):
#     print(x)
#     break

# 1-st task Informatics 2-nd part predprof
# arr = list(map(int, input().split()))
# k = int(input())
# maximSum = -1
# for i in range(len(arr)-k+1):
#   nowSum = 0
#   for j in range(i, i+k):
#     nowSum += arr[j]
#   if nowSum > maximSum:
#     maximSum = nowSum
# print(maximSum)

# 2-nd task Informatics 2-nd part predprof
# arr = list(map(int, input().split()))
# ans = False
# for i in range(len(arr)):
#   if ans:
#     break
#   canBe = True
#   arrNew = arr.copy()
#   arrNew.pop(i)
#   for j in range(len(arrNew)-1):
#     if not canBe:
#       break
#     if arrNew[j] >= arrNew[j+1]:
#       canBe = False
#   if canBe == True:
#     ans = canBe
# if ans:
#   print("true")
# else:
#   print("false")