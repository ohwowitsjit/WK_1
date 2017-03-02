base_no = int(input("Enter the base number: "));
exp_value = int(input("Enter the exponent value: "));
answer=0;

for i in range(0, exp_value):
	if answer==0:
		answer=base_no;
		continue;
	else:
		answer=answer * base_no;
	
print("Answer is:", str(answer));