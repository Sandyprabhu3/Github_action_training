"""Countdown App:

Input: Accept user input of goal and a deadline.
Output: How much time remains until that deadline?"""

import datetime
#inputs
user_input = input("Enter your goal with a deadline seperated by colon\n")
input_list = user_input.split(":")

goal = input_list[0]
deadline = input_list[1]

deadline_date = datetime.datetime.strptime(deadline,"%d.%m.%Y")
current_date = datetime.datetime.today()

#deadline calculation
time_remaining = deadline_date - current_date

print(f"Dear user, Time remaining for your goal '{goal}' is {time_remaining.days} days")