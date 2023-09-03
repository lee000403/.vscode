# arr = []
# N, M = map(int, input().split(" "))
# for arr_apd in range(N):
#     arr.append(0)
# for a in range(M):
#     i, j, k = map(int, input().split(" "))
#     for b in range(i-1, j):
#         arr[b] = k

# for c in range(N):
#     print(arr[c], end=" ")

# arr=[]
# for i in range(1, 31):
#     arr.append(i)
# std = []
# sn =[]
# for all_student in range(28):
#     student_number = input()
#     sn.append(student_number)
# for first in range(30):
#     if str(arr[first]) not in sn:
#         std.append(arr[first])

# for a in range(2):
#     if std[a] == min(std):
#         print(std[a])
#     else:
#         print(std[a])

# arr = []
# for num in range(10):
#     a = input()
#     cul = int(a) % 42
#     arr.append(cul)
# result = list(set(arr))
# print(len(result))

# s = input()
# a = []
# sum = 0
# dial = [[1],
#         [2,"A", "B", "C"],
#         [3, "D", "E", "F"],
#         [4, "G", "H", "I"],
#         [5, "J", "k", "L"],
#         [6, "M", "N", "O"],
#         [7, "P", "Q", "R", "S"],
#         [8, "T", "U", "V"],
#         [9, "W", "X", "Y", "Z"]
#         ]
# for i in range(len(s)):
#     for d in range(len(dial)):
#         if s[i] in dial[d]:
#             a.append(dial[d][0])
# print(a)
# for k in range(len(a)):
#     sum += int(a[k]) + 3
# print(sum)

# dial = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']
# a = input()
# ret = 0
# for j in range(len(a)):
#     for i in dial:
#         if a[j] in i:
#             ret += dial.index(i)+3
# print(ret)

# print("         ,r\'\"7")
# print("r`-_   ,'  ,/")
# print(" \\. \". L_r'")
# print("   `~\/")
# print("      |")
# print("      |")

# white_count = input().split()
# arr = []
# black_count = [["king" , 1],
#                ["queen", 1],
#                ["look", 2],
#                ["bishop", 2],
#                ["night", 2],
#                ["porn", 8]]
# for i in range(6):
#     a = black_count[i][1] - int(white_count[i])
#     arr.append(a)
# for j in range(len(arr)):
#     print(arr[j], end=" ")

def solution(s):
    arr = []
    arr_mi = []
    a = 1
    for i in range(len(s)):
        arr.append(s[i:i+1])
        if i+1 == len(s):
            break
    for j in range(len(s)):
        try:
            if arr[j] == " ":
                arr.remove(" ")
        except:
            break
    if "-" not in arr:
        print(min(arr), max(arr))
    elif "-" in arr : 
        for k in range(0,len(arr),2):
            try:
                arr_mi.append(arr[k] + arr[k+1])
            except:
                break
        print(min(arr_mi), max(arr_mi))
    return arr

solution("-1 -2 -3 -4")
