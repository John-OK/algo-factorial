def factorial(num):
	## recursive version ##
	# if num == 0:
	# 	return 1
	# elif num == 1:
	# 	return 1
	# else:
	# 	return num * factorial(num - 1)

	## linear version ##
	answer = num
	i = num

	if num == 0:
		return 1
	else:
		while i > 1:
			answer *= i - 1
			i -= 1

	return answer