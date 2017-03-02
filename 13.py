num = int(input("Enter your number: "));
ans=True;

for i in (2, num):
	if num == 2:
		ans = True;
		break;
	elif num&i ==0:
		ans = False;
		break;

print("The statement that", str(num), "is a prime number is ", str(ans))
