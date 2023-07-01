import random
X = 1
while X == 1:
	print("請輸入2組隨機數字來決定範圍")
	num1 = input("第一組:")
	num2 = input("第二組:")
	num1 = int(num1)
	num2 = int(num2)
	if num1 > num2:
		print("第一組數字要比第二組數字小")
	else:
		print("你所設定的範圍為:", num1, "~", num2, "。")
		r = random.randint(num1, num2)
		print(r)
		count = 0
		X = 2
while True:
	num = input("請輸入數字:")
	num = int(num)
	if num < num1 or num > num2: 
		print("輸入錯誤，請重新輸入", num1, "~", num2, "以內的數字")
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