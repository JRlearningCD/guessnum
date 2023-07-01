import random

r = random.randint(1, 100)
print(r)
while True:
	num = input("請輸入1~100以內的數字:")
	num = int(num)
	if num < 1 or num > 100: 
		print("輸入錯誤，請重新輸入1~100以內的數字")
	else:
		if num > r:
			print("猜錯了，數字太大")
			print("請重新輸入")
		elif num < r:
			print("猜錯了，數字太小")
			print("請重新輸入")
		else:
			print("恭喜猜對!!")
			break