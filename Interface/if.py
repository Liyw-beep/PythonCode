n = 1       # 定义猜测的次数
while n < 4:    # 猜测的次数少于4次
	a = input("请输入一个数字：")
	if a == '1':
		print("Monday")
		print("恭喜猜对了,程序退出")
		break
	elif a == '2':
		print("Tuesday")
		print("恭喜猜对了,程序退出")
		break
	elif a == '3':
		print("Wednesday")
		print("恭喜猜对了,程序退出")
		break
	elif a == '4':
		print("Thursday")
		print("恭喜猜对了,程序退出")
		break
	elif a == '5':
		print("Friday")
		print("恭喜猜对了,程序退出")
		break
	elif a == '6':
		print("Saturday")
		print("恭喜猜对了,程序退出")
		break
	elif a == '7':
		print("Sunday")
		print("恭喜猜对了,程序退出")
		break
	else:
		print("错误的输入，请重新输入1-7之间的数字！")
	n = n + 1
else:
	print('错误的输入超过3次，程序退出')
	