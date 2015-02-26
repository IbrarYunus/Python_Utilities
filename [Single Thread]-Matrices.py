"""Matrix Utility
Ibrar Yunus
BSCS-2
SEECS
National University of Sciences and Technology
"""

class Matrix:
	"""Constructor for intilizing dyanmic matrix with specified rows and columns"""
	def __init__(self, rows, cols):
		self.rows = rows;
		self.cols =cols;
		self.matrix = [[0 for x in  range(rows)] for x in range(cols)]

	"""Utility method for printing matrix dimensions, in format aa x bb"""	
	def _dimensionCheck(self):
		print "Your matrix> %s x %s" % (self.rows, self.cols)

	"""method to take values from user"""
	def _enterValues(self):
		print "Enter Values for your Matrix"
		for i in range(0, self.rows):
			for j in range(0, self.cols):
				num = raw_input()
				float(num)
				self.matrix[i][j] = num

	"""method to print the matrix to stdout in a human readable format"""			
	def _printValues(self):
		#print "Your Matrix is: "
		for i in range(0, self.rows):
			for j in range(0, self.cols):
				print self.matrix[i][j], 
			print " "	

	"""overloads the + operator to perform matrix multiplication"""		
	def __add__(self, second):
		#ans.rows = self.rows
		#ans.cols = self.cols
		#ans.matrix = [[0 for x in  range(self.rows)] for x in range(self.cols)]
		ans = Matrix(self.rows, self.cols)
		for i in range(0, self.rows):
			for j in range(0, self.cols):
				ans.matrix[i][j] = float(self.matrix[i][j]) + float(second.matrix[i][j]) 
					
		return ans	

	"""overloads the - operator to perform matrix subtraction"""	
	def __sub__(self, second):

		ans = Matrix(self.rows, self.cols)
		for i in range(0, self.rows):
			for j in range(0, self.cols):
				ans.matrix[i][j] = float(self.matrix[i][j]) - float(second.matrix[i][j]) 
					
		return ans

	"""overloads the ** operator to perform scalar matrix multiplication"""		
	def __pow__(self, second):
		ans = Matrix(self.rows, self.cols)
		for i in range(0, self.rows):
			for j in range(0, self.cols):
				ans.matrix[i][j] = float(self.matrix[i][j]) * float(second.matrix[i][j]) 
					
		return ans

	"""overloads the * operator to perform matrix multiplication"""		
	def __mul__(self, second):
		ans = Matrix(self.rows, second.cols)
		for i in range(self.rows):
			for j in range(second.cols):
				for k in range(second.rows):
					ans.matrix[i][j] += float(self.matrix[i][k]) * float(second.matrix[k][j])
		return ans		

	"""overloads the / operator to perform scalar matrix division"""		
	def __div__	(self, second):
		ans = Matrix(self.rows, self.cols)
		for i in range(0, self.rows):
			for j in range(0, self.cols):
				ans.matrix[i][j] = float(self.matrix[i][j]) / float(second.matrix[i][j]) 				
		return ans	

	"""method to transpose a matrix"""	
	def ___transpose__ (self):
		ans = Matrix(self.cols, self.rows)
		ans.matrix = zip(*self.matrix)
		return ans
		
"""Testing Starts here"""
"""
A= Matrix(3,3)
A._enterValues()
print "Your Matrix is:"
A._printValues()

B = Matrix(3,3)
B._enterValues()
print "Your Matrix is:"
B._printValues()

print "\nAddition Test, C = A + B\n\n"
C = A + B
print "Answer:"
C._printValues()

print "\nSubtraction Test, D = A + B\n\n"
D = A - B
print "Answer:"
D._printValues()

print "\nScalar Multiplication Test, E = A ** B\n\n"
E = A ** B
print "Answer:"
E._printValues()

print "\nScalar Division Test, F = A / B\n\n"
F = A / B
print "Answer:"
F._printValues()

print "\nMatrix Multiplication Test, G = A * B\n\n"
G = A * B
print "Answer:"
G._printValues()

print "\nAssignment Test, C=G"
C = G
C._printValues()

print "\nTranpose Test, C'"
H = C.___transpose__()
H._printValues()

"""