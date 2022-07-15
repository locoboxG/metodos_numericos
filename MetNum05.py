import os
class raices:
    M_pun = []
    M_fdp = []
    
    def __init__(self,p,v) -> None:
        self.M_pun = p
        self.M_fdp = v
        
    def factores (self, r):            #calcula los factores que multiplican una ecuacion. 
        M_fact = [1]
        if len(r) == 2:                #x^2+ (a+b)x + ab --> ecuacion de segundo grado   (x+a)(x+b)
            M_fact.append(r[0]+r[1])   #(a+b)x  
            M_fact.append(r[0]*r[1])   #ab
        if len(r) == 3:                #x^3+ (a+b+c)x^2 + (ab+ac+bc)x + abc --> ecuacion de tercer grado (x+a)(x+b)(x+c)
            M_fact.append(r[0]+r[1]+r[2])                   
            M_fact.append(r[0]*r[1]+r[0]*r[2]+r[1]*r[2])
            M_fact.append(r[0]*r[1]*r[2])    
        if len(r) == 4:                #x^4+ (a+b+c+d)x^3 + (ab+ac+ad+bc+bd+cd)x^2 + (abc+abd+acd+bcd)x +abcd --> ecuacion de cuarto grado (x+a)(x+b)(x+c)(x+d)
            M_fact.append(r[0]+r[1]+r[2]+r[3])                                 
            M_fact.append(r[0]*r[1]+r[0]*r[2]+r[0]*r[3]+r[1]*r[2]+r[1]*r[3]+r[2]*r[3])
            M_fact.append(r[0]*r[1]*r[2]+r[0]*r[1]*r[3]+r[0]*r[2]*r[3]+r[1]*r[2]*r[3]) 
            M_fact.append(r[0]*r[1]*r[2]*r[3])           
        if len(r) == 5:                #x^5+ (a+b+c+d+e)x^4 + (ab+ac+ad+ae+bc+bd+be+cd+ce+de)x^3 + (abc+abd+abe+acd+ace+ade+bcd+bce+bde+cde)x^2 + (abcd+abce+acde+bcde)x +abcde --> ecuacion de quinto grado (x+a)(x+b)(x+c)(x+d)(x+e)
            M_fact.append(r[0]+r[1]+r[2]+r[3]+r[4])
            M_fact.append(r[0]*r[1]+r[0]*r[2]+r[0]*r[3]+r[0]*r[4]+r[1]*r[2]+r[1]*r[3]+r[1]*r[4]+r[2]*r[3]+r[2]*r[4]+r[3]*r[4])
            M_fact.append(r[0]*r[1]*r[2]+r[0]*r[1]*r[3]+r[0]*r[1]*r[4]+r[0]*r[2]*r[3]+r[0]*r[2]*r[4]+r[0]*r[3]*r[4]+r[1]*r[2]*r[3]+r[1]*r[2]*r[4]+r[1]*r[3]*r[4]+r[2]*r[3]*r[4]) 
            M_fact.append(r[0]*r[1]*r[2]*r[3]+r[0]*r[1]*r[2]*r[4]+r[0]*r[1]*r[3]*r[4]+r[0]*r[2]*r[3]*r[4]+r[1]*r[2]*r[3]*r[4])
            M_fact.append(r[0]*r[1]*r[2]*r[3]*r[4])
        return M_fact    

    def lagrange (self):
        M_vals = []
        M_lang = []
        M_divs = []
        mlon = len(self.M_pun)
        for cx in range(mlon):
            ren=[]
            for cy in range (mlon):
                divi = 0;
                if cx==cy:
                    varf = self.M_pun[cy]
                    continue
                ren.append(self.M_pun[cy])
            divis = 1    
            for cy in range (len(ren)):
                divis *= varf - ren[cy]
                ren[cy] *=-1
            M_vals.append(ren)
            M_divs.append(divis)
        #print (M_vals)
        #print (M_divs)
        linea = "| /  "  
        linea += self.RenMat(M_divs,6)
        print (linea)
        print ("-".center(mlon*13+6,"-"),"\n")
        
        for cx in range(mlon): 
            M_lang.append (self.factores(M_vals[cx]));
        
        self.showLagrangiano(M_lang)
        
        M_rsl = []
        for cc in range(mlon):             
            sumando = 0
            for cr in range(mlon): 
                sumando += self.M_fdp[cr]/M_divs[cr]*M_lang[cr][cc]
            M_rsl.append(sumando)    
        
        linea = self.RenMat(M_rsl,7)
        print (linea)    
        print ("-".center((mlon)*15+1,"-"),"\nPolinomio Interpolador : ")
        print (self.RenPoli(M_rsl),"\n")
        
             
    def RenMat (self, fila, decimales):
        renglon = ""
        for cr in range (len(fila)):
            if decimales == 4:
                renglon += "|%12.4f"%(fila[cr])
            if decimales == 6:
                renglon += "|%12.6f"%(fila[cr])
            if decimales == 7:
                renglon += "|%14.7f"%(fila[cr])    
        renglon += "|"
        return renglon    
    
    def RenPoli (self, fila):
        renglon = ""
        mlon = len(fila)
        for cr in range (mlon):
            renglon += "%f"%(fila[cr])
            if cr < mlon-1: 
                renglon += " x^%1d "%(len(fila)-cr-1)
                if (fila[cr+1])>=0:
                    renglon += "+"
        renglon += " = 0"            
        return renglon 
     
    def showDatosInicio (self) -> None:
        mlon = len(self.M_pun)
        print("Datos".center((mlon)*13+6,"_"))
        linea = "|____|_____P"
        for cr in range (mlon):
            linea += "%1d"%(cr) + "_____|"
            if cr< mlon-1:
                linea+= "_____P"
        print (linea)
        linea = "| x  "  
        linea += self.RenMat(self.M_pun,4)
        print (linea)
        linea = "|f(x)"  
        linea += self.RenMat(self.M_fdp,4)
        print (linea)
        print("-".center((mlon)*13+6,"-"))
    
    def showLagrangiano (self, M_lang):
        mlon = len(self.M_pun)
        print("Lagrangiano".center((mlon)*15+1,"_"))
        linea = "|_____X^"
        for cr in range (mlon):
            linea += "%1d"%(mlon-cr-1) + "______|"
            if cr< mlon-1:
                linea+= "_____X^"
        print (linea)       
        for cx in range(mlon):     
            linea = self.RenMat(M_lang[cx],7)
            print (linea)        
        print ("-".center(mlon*15+1,"-"))   
        
os.system('cls' if os.name == 'nt' else 'clear')
print ("Polinomio Interpolador forma de Lagrange\n")
mn_lag = raices([0,0.25,0.5,0.75,1],[0.9135,0.8109,0.6931,0.5596,0.4055]);
mn_lag.showDatosInicio();
mn_lag.lagrange();       