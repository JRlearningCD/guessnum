import random

r = random.randint(1, 100)
print(r)
count = 0
while True:
	num = input("請輸入1~100以內的數字:")
	num = int(num)
	if num < 1 or num > 100: 
		print("輸入錯誤，請重新輸入1~100以內的數字")
	else:
		count += 1
		if num == r:
			print("恭喜猜對!!")
			print("你猜了", count, "次才猜對")
			break
		elif num < r:
			print("猜錯了，比答案小，請重新輸入")
		else:
			print("猜錯了，比答案大，請重新輸入")
		print("已猜錯", count, "次")