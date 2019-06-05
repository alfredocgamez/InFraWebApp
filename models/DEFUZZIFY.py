from FCL import FCL

class DEFUZZIFY(FCL):
	def __init__(self, SeccionD, EmotionD,TermD, NeutralD, LowD, HighD, Method,Default):
		super().__init__(SeccionD, EmotionD,TermD,NeutralD,LowD,HighD)
		self.Method=Method
		self.Default=Default
		
		
	def descripcion(self):
		super().descripcion()
		print(" METHOD : ",self.Method, "\n", "DEFAULT : ",self.Default)
		print("END_DEFUZZIFY" )