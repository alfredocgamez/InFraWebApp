from FCL import FCL
class RULES():
	def __init__(self,Numero_Regla,AND,ACT,ACCU,RULE_0,RULE_1,RULE_2):
		self.AND=AND
		self.ACT=ACT
		self.ACCU=ACCU
		self.RULE_0=RULE_0
		self.RULE_1=RULE_1
		self.RULE_2=RULE_2
		self.Numero_Regla=Numero_Regla
	
	

	def reglas(self):
		print("RULEBLOCK : ", self.Numero_Regla,"\n","AND : ",self.AND,"\n","ACT : ",self.ACT, "\n","ACCU : ",self.ACCU,"\n","RULE_0: ",self.RULE_0,"\n",
			"RULE_1 : ", self.RULE_1,"\n","RULE_2 : ", self.RULE_2)
		print("END_RULEBLOCK ")
		print("END_FUNCTION_BLOCK")