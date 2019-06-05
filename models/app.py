import json
from FUZZIFY import FUZZIFY 
from DEFUZZIFY import DEFUZZIFY
from RULES import RULES


class FUNCTION():
	def __init__(self,pleasantness,conduciveness,unfairness,adjustment):
		self.pleasantness=pleasantness
		self.conduciveness=conduciveness
		self.unfairness=unfairness
		self.adjustment=adjustment

	def funciones(self):
		print("FUNCTION_BLOCK_PAD")
		print("VAR_INPUT")
		print(" pleasantness : ",self.pleasantness,"\n","conduciveness : ",self.conduciveness,"\n","unfairness : ", self.unfairness,"\n","adjustment : ",self.adjustment)
		print("VAR_OUTPUT")
      


	
def jsonDefault(object):
	return object.__dict__		     

funcion=FUNCTION("REAL","REAL","REAL","REAL")
funcion.funciones()
jsonfuncion=json.dumps(funcion, default=jsonDefault,sort_keys=True, indent=4)
var_unfairness=FUZZIFY("FUZZIFY","unfairness","TRIAN",0.7,1.0,1.0)
var_unfairness.descripcion()
jsonUnFairness = json.dumps(var_unfairness, default=jsonDefault,sort_keys=True, indent=4)
var_adjustment=DEFUZZIFY("DEFUZZIFY","adjustment","TRIAN",0.7,1.0,1.0,"COG",0)
var_adjustment.descripcion()
jsonAdjustment = json.dumps(var_adjustment, default=jsonDefault,sort_keys=True, indent=4)
RULEBLOCK= RULES(1,"MIN","MIN","MAX","IF (pleasantness IS neutral) AND (conduciveness IS high) AND (unfairness IS low) AND (adjustment IS high) THEN pleasure IS neutral",
	"IF (pleasantness IS low) AND (conduciveness IS low) AND (unfairness IS low) AND (adjustment IS low) THEN pleasure IS low","IF (pleasantness IS high) AND (conduciveness IS high) AND (unfairness IS neutral) AND (adjustment IS high) THEN pleasure IS high")
RULEBLOCK.reglas()
jsonRule=json.dumps(RULEBLOCK, default=jsonDefault,sort_keys=True, indent=4)


print(jsonUnFairness,"\n"+jsonAdjustment,"\n"+jsonRule,"\n"+jsonfuncion) #imprime los dos objetos creados en formato json 

file = jsonUnFairness+"\n"+jsonAdjustment,"\n"+jsonRule,"\n"+jsonfuncion #Guarda los objetos creados en una variable unica.

#Crea el archivo JSON
with open('gea.json','w') as outfile:
	json.dump(file,outfile)

