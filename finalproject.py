import random
text = ['A','B','C','D']
qoptions = [0,0,0,0]
score = 0 

for i in range(10):
	print('Question',i+1,':')
	num1 = random.randint(0,50)
	num2 = random.randint(0,50)
	num3 = random.randint(0,50)
	correct = num1 + num2 + num3
	print(num1,'+',num2,'+',num3,'= ?')
	
	for y in range(3):
		qoptions[y] = random.randint(correct-20,correct+20)
	qoptions[3] = correct
	random.shuffle(qoptions)
	temp = qoptions.index(correct)

	for z in range(4):
		print(text[z],qoptions[z])

	b = input("Enter the option which you chose: ")
		
	if b == text[temp]:
		score+=10
		print('Your answer is true. Your score =', score)

	else:
		print('Your answer is wrong') 

if score <= 50: 
	print('You are failed.')
else:
	print('You passed it.') 