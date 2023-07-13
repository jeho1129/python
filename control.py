
n = [1, 2, 4, 5, 6, 0, 1, 0, 2]
cnt = 0
for i in n:
    if i == 0:
        print(cnt)
        break
    cnt = cnt + 1

# while문을 이용하여 hello를 5번만 출력하는 코드
t = 0
while t < 5:
    print("hello")
    t = t + 1

# While문을 이용하여 Array에서 첫 번째 0의 위치를 출력하는 코드
n = [1, 2, 4, 5, 6, 0, 1, 0, 2]
i = 0
while n[i] != 0:
    i = i + 1
print(i)
