dust = 1

if dust > 150:
    print("매우 나쁨")
elif dust > 80:
    print("나쁨")
elif dust > 30:
    print("보통")
elif dust >= 0:
    print("좋음")
else:
    print("올바르지 않은 값")