from random import randint

if __name__ == '__main__':

	# Both the persons will be agreed upon the
	# public keys G and P
	# A prime number P is taken
	P = int(input("Enter the Prime Number:- "))
	
	# A primitive root for P, G is taken
	G = int(input("Enter the G value :- "))
	
	
	print('\nThe Value of P is :%d'%(P))
	print('The Value of G is :%d'%(G))
	
	# Alice will choose the private key a
	a = 4
	print('\nThe Private Key a for Alice is :%d'%(a))
	
	# gets the generated key
	x = int(pow(G,a,P))
	
	# Bob will choose the private key b
	b = 3
	print('The Private Key b for Bob is :%d'%(b))
	
	# gets the generated key
	y = int(pow(G,b,P))
	
	
	# Secret key for Alice
	ka = int(pow(y,a,P))
	
	# Secret key for Bob
	kb = int(pow(x,b,P))
	
	print('\nSecret key for the Alice is : %d'%(ka))
	print('Secret Key for the Bob is : %d'%(kb))
  
#   output
#   Enter the Prime Number:- 19
# Enter the G value :- 15

# The Value of P is :19
# The Value of G is :15

# The Private Key a for Alice is :4
# The Private Key b for Bob is :3

# Secret key for the Alice is : 7
# Secret Key for the Bob is : 7

'''
p=int(input("The value of p: "))
q=int(input("The value of q: "))
a=int(input('The Private Key a for Alice is: '))
b=int(input('The Private Key b for Bob is: '))
print("Generated key for Alice: ",pow(q,a)%p)
R=pow(q,a)%p
print("Generated key for Bob: ",pow(q,b)%p)
S=pow(q,b)%p
print("Secret key for the Alice is: ",pow(S,a)%p)
Rk=pow(S,q)%p
print("Secret Key for the Bob is: ",pow(R,b)%p)
Sk=pow(R,b)%p
'''
