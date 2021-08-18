meraki = 0;
non_meraki = 0;
def meraki_helper(n):
	global meraki;
	global non_meraki;
	if n < 11:
		print("Yes -",n,"is a Meraki number");
		meraki += 1;
		return;
	else:
		flag = 0;
		x = n;
		while n >= 10:
			digit = int(n%10);
			if flag:
				if(abs(prevdigit-digit)!=1):
					print("No -",x,"is not a Meraki number");
					non_meraki += 1;
					return;
			flag = 1;
			prevdigit = digit;
			n = int(n/10);

		if(abs(prevdigit-n)!=1):
			print("No -",x,"is not a Meraki number");
			non_meraki += 1;
			return;

		print("Yes -",x,"is a Meraki number");
		meraki += 1;
		return;
	"""This will detect meraki number"""


# input = [12, 14, 56, 78, 98, 54, 678, 134, 789, 0, 7, 5, 123, 45, 76345,
# 987654321,101]

input = [int(elements) for elements in input("Enter the elements : ").split()] 
for x in input :
	meraki_helper(x);
	
print("The input list contains",meraki,"meraki and",non_meraki,"non meraki numbers.");
