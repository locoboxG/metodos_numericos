import math
import os

class NewtRaps:
    M_J=[] 
    M_i=[]
    M_xk = []
    M_xl = []
    M_F=[]
    
    def __init__(self,cual) -> None:
        self.M_xk.clear()               # valores iniciales del problema 
        if cual==1:
            self.M_xk.append(5)
            self.M_xk.append(0)
        else :
            self.M_xk.append( 5)
            self.M_xk.append(-1)
        

    def InversaM (self) ->None:          # calculo de la matriz inversa mediante el metodo Gauss-Jordan
        cuan = len(self.M_xk)
        self.M_i.clear()
        for cx in range (cuan):          # creacion de la matriz identidad correspondiente 
            renglon=[]
            for cy in range (cuan):
                if cx==cy:
                    renglon.append(1)
                else:
                    renglon.append(0)
            self.M_i.append(renglon)        
    
        for cre in range (cuan):          #resolucion de la matriz original manipulando la matriz identidad al tiempo
            divi = self.M_J[cre][cre]
            for cx in range (cuan):
                self.M_J[cre][cx] /= divi
                self.M_i[cre][cx] /= divi
            for cy in range (cuan):
                if cre == cy:
                    continue
                multi = self.M_J[cy][cre]
                for cw in range (cuan):
                    self.M_J[cy][cw] -= self.M_J [cre][cw] * multi
                    self.M_i[cy][cw] -= self.M_i [cre][cw] * multi

    def MultiM (self) -> None:             #multiplicacion de matrices, resta del valor de x incluido
        cuan = len(self.M_xk)
        self.M_xl.clear()
        for cre in range (cuan):
            suma = 0;
            for cy in range (cuan):
                suma += self.M_i[cre][cy] * self.M_F[cy]
            self.M_xl.append(self.M_xk[cre]- suma)


    def calFuncion (self,renglon):                #calculo de la funcion original para matriz F
        if renglon == 0:
            return math.pow(self.M_xk[0],2) + self.M_xk[1] - 37         #x^2+y-37
        if renglon == 1:
            return self.M_xk[0] - math.pow(self.M_xk[1],2) - 5          #x-y^2-5 
    
    def calDerivada (self,renglon,columna):       # calculo de funciones derivadas parcialmente matriz J
        if renglon == 0:
            if columna == 0:
                return 2*self.M_xk[0]             #2x
            if columna == 1:
                return 1                          #1
        if renglon == 1:
            if columna == 0:
                return 1                          #1
            if columna == 1:
                return 2*self.M_xk[1]             #2y 
    
    def MatFuncion (self) -> None:                           # calculo matriz F
        cuan = len(self.M_xk)
        self.M_F.clear()
        for cre in range (cuan):
            self.M_F.append(self.calFuncion(cre))

    def MatDerivadas (self) -> None:                        # calculo matriz j
        cuan = len(self.M_xk)
        self.M_J.clear()
        for cre in range (cuan):
            renglon = []
            for cy in range (cuan):
                renglon.append (self.calDerivada(cre,cy))
            self.M_J.append (renglon)
            
    def calTolerancia (self):                               # calculo tolerancia 
        suma = 0
        cuan = len(self.M_xk)
        for cre in range (cuan):
            suma += math.pow(self. M_xk[cre]-self.M_xl[cre],2)
            self. M_xk[cre] = self.M_xl[cre]
        return math.sqrt(suma)    
    
    def ciclo (self) -> None:
        mlon = len(self.M_xk)          #control del numero de variables 
        
        print("Newton Rapson.".center((mlon+1)*13+6,"_"))
        titulo = "|_____X"
        for cr in range (mlon):
            titulo += "%1d"%(cr+1)
            if cr < mlon-1:
                titulo += "_____|_____X"
            else:
                titulo += "______|___Tolerancia___|"
        print (titulo)
        
        strikes = 0    #control de convergencia, si el error sube 8 veces consecutivas
        tole = 1;
        while tole > 0.0001 and strikes < 8:    
            antole = tole;
            #print("xK\n",self.M_xk)
            self.MatFuncion()                    # calculo F
            #print("F\n",self.M_F)
            self.MatDerivadas()                 # calculo J
            #print("J\n",self.M_J)
            self.InversaM()                     # obtengo la inversa de j   j-1
            #print("J-1\n",self.M_i)
            self.MultiM()                       # multiplico la inversa por F y resto las x 
            tole = self.calTolerancia()         # calculo la tolerancia
            #print("xk+1\n",self.M_xl)
            #print("tolerancia ", self.calTolerancia())
            marca = ""     
            if tole > antole:
                strikes +=1
                marca = " <-*"
            else:
                strikes = 0
                     
            renglon = ""
            for cr in range (mlon):
               renglon += "|%12.4f"%(self.M_xl[cr])
            print (renglon,"|-->%12.5f"%(tole),"|",marca)

        print("-".center((mlon+1)*13+6,"-"),"\n\n")
        if strikes >=8:
            print("Newton Rapson.(Resultado)-->No Converge".center((mlon+1)*13+6,"_"))         
        else:
            print("Newton Rapson.(Resultado)".center((mlon+1)*13+6,"_"))         
            print(titulo)
            print (renglon,"|-->%12.5f"%(tole),"|")
            print("-".center((mlon+1)*13+6,"-"),"\n\n")
        
os.system('cls' if os.name == 'nt' else 'clear')
print ("*****************************************************************")
print ("Problema 2 inciso a")
mn_NR = NewtRaps(1);
mn_NR.ciclo();

print ("*****************************************************************")
print ("Problema 2 inciso b")
mn_NR = NewtRaps(2);
mn_NR.ciclo();