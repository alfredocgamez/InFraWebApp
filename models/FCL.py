import json

class FCL(object):
	
	def __init__(self,Seccion,Emotion,Term,Neutral,Low,High):
		
		self.Emotion=Emotion
		self.Neutral=Neutral
		self.Low=Low
		self.High=High
		self.Term=Term
		self.Seccion=Seccion
		
	def descripcion(self):
		print( self.Seccion, " : ", self.Emotion ,"\n", "TERM Neutral : ",self.Term, self.Neutral,"\n","TERM Low : ",self.Term ,self.Low,"\n","TERM High : ",self.Term, self.High )

