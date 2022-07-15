import math
import os

class metodos3:
    m_K = []
 
    def __init__(self) -> None:
        pass 
    def funciones (self, cual, reng, vx) :
        
        if cual == 1 :  # ecuaciones del problema 1 de la tarea
            if reng == 0:       
                return math.sqrt(-2*math.pow(vx[1],2)+ vx[1]+ 2* vx[2])         #x^2+2y^2-y-2z = 0   --> x = raiz(-2y^2+y+2z)
            if reng == 1:
                return math.sqrt((-0.0001 + math.pow(vx[0],2) + 10* vx[2])/8)   #x^2-8y^2+10z=0.0001 --> y = raiz((-0.0001+x^2+10z)/8)
            if reng == 2:
                return math.pow(vx[0],2) / (7*vx[1])                            #x^2/7yz-1= 0        --> z = x^2/7y
        if cual == 2 :   ## caso de estudio para el desarrollo del programa
            if reng == 0:
                return (math.cos(vx[1] * vx[2]) + 0.5)/3
            if reng == 1:
                return vx[0] / 25
            if reng == 2:
                return -(math.exp(-vx[0]*vx[1])+ 10*math.pi/3 - 1)/20
  
    def matriz (self, cual):     
        if cual == 1:                               # problema 1
            self.m_K = [[0.5, 0.3, 0.1],[0,0,0]]    # valores de inicio del problema 1   x = indice 0, y indice 1,  z indice 2 en arreglo 
        if cual == 2:                               ## --------------> caso de estudio 
            self.m_K = [[0, 0, 0],[0,0,0]]    
            
    def PuntoFijoMultiVar (self,cual):   #iterativo secuencial
        mlon = len(self.m_K[0])
        
        print("Punto Fijo MultiVariable.(Paralelo)".center((mlon+1)*13+5,"_"))
        titulo = "|_____X"
        for cr in range (mlon):
            titulo += "%1d"%(cr+1)
            if cr < mlon-1:
                titulo += "_____|_____X"
            else:
                titulo += "______|___Tolerancia___|"
        print (titulo)
        
        tole = 1
        while tole > 0.0000014:             #tolerancia dle problema 1.4*10^-6
            valores = []
            renglon = ""
            tole = 0
            for cr in range(mlon):
                valores.append(self.m_K[0][cr])                            # llenan los valores para iteracion y calculo de cada renglon
            for cr in range(mlon):
                self.m_K[1][cr] = self.funciones (cual,cr,valores)         # se obtiene cada valor 
                renglon += "|%12.6f"%(self.m_K[1][cr])  
                tole +=  math.pow (self.m_K[1][cr] - self.m_K[0][cr],2)    #calculo de la tolerancia o error. sumando por sumando
                    
                self.m_K[0][cr] = self.m_K[1][cr]                          #nuevos puntos reemplazan a los viejos
                    
            tole = math.sqrt(tole)                                         #calculo de la tolerancia raiz cudarada
            print(renglon,"|-->%12.8f"%(tole),"|")

        print("-".center((mlon+1)*13+5,"-"),"\n\n","Punto Fijo Multivariable (Paralelo)-->Resultado".center((mlon+1)*13+5,"_"))
        print(titulo)
        print(renglon,"|-->%12.8f"%(tole),"|\n","-".center((mlon+1)*13+5,"-")) 

    def PuntoFijoMultiVarSimul (self,cual):
        mlon = len(self.m_K[0])
        
        print("Punto Fijo MultiVariable.(Simultaneo)".center((mlon+1)*13+5,"_"))
        titulo = "|_____X"
        for cr in range (mlon):
            titulo += "%1d"%(cr+1)
            if cr < mlon-1:
                titulo += "_____|_____X"
            else:
                titulo += "______|___Tolerancia___|"
        print (titulo)
        
        tole = 1
        while tole > 0.0001:
            valores = []
            renglon = ""
            tole = 0
            for cr in range(mlon):
                valores.append(self.m_K[0][cr]) 
            for cr in range(mlon):
                self.m_K[1][cr] = self.funciones (cual,cr,valores)
                valores[cr] = self.m_K[1][cr]                                 #instruccion que hace el avance simultaneo
                
                renglon += "|%12.6f"%(self.m_K[1][cr])  
                tole +=  math.pow (self.m_K[1][cr] - self.m_K[0][cr],2)
                                    
                self.m_K[0][cr] = self.m_K[1][cr]
                    
            tole = math.sqrt(tole)
            print(renglon,"|-->%12.8f"%(tole),"|")

        print("-".center((mlon+1)*13+5,"-"),"\n\n","Punto Fijo Multivariable (Simultaneo)-->Resultado".center((mlon+1)*13+5,"_"))
        print(titulo)
        print(renglon,"|-->%12.4f"%(tole),"|\n","-".center((mlon+1)*13+5,"-")) 

os.system('cls' if os.name == 'nt' else 'clear')
mn_muchas = metodos3 ();
mn_muchas.matriz(1);
print ("**************************************************************************************")
print (" Prblema 1  punto fijo multivariable avance simultaneo")
mn_muchas.PuntoFijoMultiVar(1)
#mn_muchas.matriz(1);
#mn_muchas.PuntoFijoMultiVarSimul(1);
                              