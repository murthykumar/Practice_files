#!/usr/bin/python3
import re;
'''
n1 = int(input("Enter the first number : "));
n2 = int(input("Enter the second number : "));
def ret (x1,x2):
				s = 0;
				if((x1 * x2) > 1000 ):
								s = x1+x2;
				else :
								s = x1 * x2;
				return s;


r = ret(n1,n2);
print("return : {}".format(r));
s = 0;
for i in range(10):
						t = s + i;
						print("current Number : {} previous Number :{} sum :{}".format(i,s,t));
						s = i;

str = "pynative";
lis = list(str);
#print(len(lis));
for i in range(len(lis)):
				if (i%2 == 0 ):
							print(lis[i]);			
print(lis);
def removeChar (strin,n):
							del strin[:n];
							return(strin);
				

rr = removeChar(lis[:],4);
print(rr);
print(lis);


l1 = [10, 20, 30, 40, 10];

if(l1[0] == l1[-1] ):
				print("True");


for i in l1:
				if(i%5 == 0):
							print(i);
'''
s1 = "Emma is good developer. Emma is a writer";
l3 = re.findall("Emma",s1);
print("Emma : {}".format(len(l3)));


for i in range(1,6):
				s = str(i);
				print(i * s);


























