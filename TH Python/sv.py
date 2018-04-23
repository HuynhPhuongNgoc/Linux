class sv:
	mssv=""
	Hoten=""
	khoa=""
	def __init__(self,mssv,Hoten,khoa):
		self.mssv=mssv
		self.Hoten=Hoten
		self.khoa=khoa
	def toString(self):
		print(self.mssv,self.Hoten,self.khoa)
	def getmssv(self):
		return self.mssv
	def getHoten(self):
		return self.Hoten
	def getkhoa(self):
		return self.khoa 
class khoa:
	makhoa=""
	tenkhoa=""
	def __init__(self,makhoa,tenkhoa):
		self.makhoa=makhoa
		self.tenkhoa=khoa
	def toString(self):
		print(self.makhoa,self.tenkhoa)
	def getmakhoa(self):
		return self.makhoa
	def gettenkhoa(self):
		return self.tenkhoa 
	
l=[]
l.append(sv(001,'MaiA',57))
l.append(sv(002,'TranB',58))
l.append(sv(003,'LeC',57))
l.append(sv(004,'PhamQ',57))
l.append(sv(005,'NgoM',59))
for i in l:
	i.toString()
v=[]
v.append(khoa(56,'khoa 56 CNTT'))	
v.append(khoa(57,'khoa 57 CNTT'))
v.append(khoa(58,'khoa 58 CNTT'))
v.append(khoa(59,'khoa 59 CNTT'))

for i in l:
	if(i.getkhoa() == 57):
		i.toString()

