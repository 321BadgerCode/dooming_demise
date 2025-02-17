import datetime

def get_birthday():
	print("Please enter your birthday in the following format: yyyy-mm-dd")
	birthday = input()
	return birthday

def calculate_days_left(birthday):
	birthday = datetime.datetime.strptime(birthday, '%Y-%m-%d')
	death_day = birthday + datetime.timedelta(days=29200)
	current_day = datetime.datetime.now()
	days_left = death_day - current_day
	return days_left

def percent_life_lived(birthday):
	birthday = datetime.datetime.strptime(birthday, '%Y-%m-%d')
	death_day = birthday + datetime.timedelta(days=29200)
	current_day = datetime.datetime.now()
	days_lived = current_day - birthday
	percent = days_lived.days/29200
	return percent

def display_loading_bar(percent):
	percent2 = percent/2
	loading_bar = "["
	if percent < 25:
		loading_bar += "\033[92m"
	elif percent < 50:
		loading_bar += "\033[93m"
	else:
		loading_bar += "\033[91m"
	for i in range(0, 50):
		if i < percent2:
			loading_bar += "#"
		else:
			loading_bar += " "
	loading_bar += "\033[0m]"
	print(loading_bar)

def display_message(percent):
	if percent < 10:
		print("You have a lot of life left to live! Enjoy it!")
	elif percent < 20:
		print("YOLO! LIVE IT UP LIKE THERE'S NO TOMORROW AND NO SCHOOL!!!")
	elif percent < 30:
		print("PARTY TIME!!! HAVE FUN!!! (While you still can. Lol, jk.)")
	elif percent < 40:
		print("Boooooooorrrrrriiiinnnnnnggggggggg")
	elif percent < 50:
		print("Mid-life crisis time! Buy a sports car!")
	elif percent < 60:
		print("You're getting old! Better start thinking about retirement!")
	elif percent < 70:
		print("RETIRE!!!")
	elif percent < 80:
		print("You're old. Like, really old. Like, you should be dead by now old.")
	elif percent < 90:
		print("You're still alive? How?")
	else:
		print("Still got few more years left in ya, huh?")

def main():
	birthday = get_birthday()
	days_left = calculate_days_left(birthday)
	print("You have {} years, {} months, {} weeks, {} days left.".format(days_left.days//365, (days_left.days%365)//30, (days_left.days%365)%30//7, (days_left.days%365)%30%7))
	print("Days: {}".format(days_left.days))
	percent = percent_life_lived(birthday)
	print("You have lived {}% of your life.".format(percent*100))
	display_loading_bar(percent*100)
	display_message(percent)

if __name__ == '__main__':
	main()