from FCL import FCL

class FUZZIFY(FCL):
    def __init__(self, SeccionF, EmotionF,TermF, NeutralF, LowF, HighF):
	    super().__init__(SeccionF, EmotionF,TermF,NeutralF,LowF,HighF)

    def descripcion(self):
        super().descripcion()
        print("END_FUZZIFY")
		

    
