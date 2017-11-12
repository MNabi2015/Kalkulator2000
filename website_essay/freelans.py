import json
import os
import time

composition = open('essay.txt', 'w')

print('Write an composition\n')
theme = input('The theme of the composition ')
essay = ("\n" + theme + '\n' + input('') + '\n')
composition.write(essay)

composition.close()

print("Wait message is moderated!")
time.sleep(6)
print("20%")
time.sleep(6)
print("40%")
time.sleep(6)
print("60%")
time.sleep(6)
print("80%")
time.sleep(6)
print("100%")
word = "True"

website = open('website.txt', 'a')
file1 = open('essay.txt', 'r+')
if word in file1.read():
	def reg():
		file = open('users_info.txt', 'w')

		new_user = {}
		new_user['first_name'] = input('Enter your first_name:')
		new_user['last_name'] = input('Enter your last_name:')
		new_user['number'] = input('Enter your phone number:')
		new_user['qiwi'] = input('Enter your Qiwi or WB address:')
		uObj = json.dumps(new_user)
		file.write(uObj)
		file.write(("\nTo replenish the balance on " + str(money) +'$'))
		website.write(new_user['first_name'] + "_" + new_user['last_name'] + ":")
		website.write(essay)
		file.close()

		print("Thank for your composition!")

	money = 0
	text_info = os.stat('essay.txt')

	print('Composition size:', text_info.st_size)

	if text_info.st_size <= 50:
		print('\n :( :( :( :(\nBoys you wrote quite a few words\nYou dont get any of that!')
	elif 50 < text_info.st_size <= 150:
		print('\n :| :| :| :|\nYou re doing great but this is still not enough\nSo you earned 5 $ but keep trying you will succeed')
		money += 5
		reg()
	elif 150 < text_info.st_size <= 300:
		print('\n :) :) :) :)\nBut thats exactly what I am talking about\nGood work your balance recharged for 15 $\nBut as we all know, "to infinity and beyond" so you can try again!')
		money += 15
		reg()
	elif text_info.st_size >= 300:
		print('\n ;) ;) ;) ;)\nYou re a genius you deservedly get all 25 $')
		money += 25
		reg()
	else:
		print('>>>Error<<<')

	print("\nYour balance is replenished on the " + str(money) +'$')

else:
	print("Your essay has not passed moderation!")
file1.close()
website.close()
