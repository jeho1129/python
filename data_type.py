# 1단부터 9단까지의 구구단 코드
a = 0
for x in range(1, 10):      # range(a, b)의 경우 a ~ b-1 까지의 범위를 지정한다.
    for i in range(1, 10):
        a = x * i
        print(x, 'X', i, "=", a)
    if x == 5:      # 5단의 경우 SPECIAL LINE을 출력
        print("********************")
    else:
        print("--------------------")

# n의 나머지 값을 판단하여 홀수인지, 짝수인지 판단하는 코드
n = 10
if n % 2 == 0:
    print("짝수")
else:
    print("홀수")

# elif문을 활용하여 3개 이상의 조건을 판단하여 해당 조건에 맞는 결과를 출력하는 코드
# elif문을 활용할 때는 조건에 따른 순서를 잘 파악하는 것이 중요
m = 200
if m >= 200:
    print("200 이상")
elif m >= 100:      # n >= 100 and n < 200 == 100 <= n < 200
    print("100 이상")
else:
    print("100 미만")

# z가 짝수인지, 홀수인지 판단하는 코드 + 0인지 판단하는 코드
z = 4
if z == 0:
    print(z)
elif n % 2 == 1:
    print("홀수")
else:
    print("짝수")