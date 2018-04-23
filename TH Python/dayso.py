n=int(input('Nhap n: '))
def dayso(n):
	for i in range (1,n+1):	
		print(i)
dayso(n)
def sochan(n):
	tong=0
	for i in range(1,n+1):
		if(i%2==0):
			tong+=i
	print('Tong so chan = ',tong)
sochan(n)

