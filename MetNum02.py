import math
import os
class metodos2:
    m_A = [[]];
    m_B = [];
    m_K = [[]];  
    
    def __init__(self) -> None:
        pass    
    
    def matrices(self, cual) -> None:
        if cual == 1:                  # caso de estudio, ejemplo usado
            self.m_A = [[10, 1, 2],
                        [ 4, 6,-1],
                        [-2, 3, 8]]
            self.m_B = [3,9,51]
            self.m_K = [[0,0],
                        [0,0],
                        [0,0]]
        if cual == 2:                 # problema 1 de la tarea   <-----------------
            self.m_A = [[98,   9,  2,   1,   0.5 ],
                        [11, 118,  9,   4,   0.88],
                        [27,  27, 85,   8,   2   ],
                        [ 1,   3, 17, 142,  25   ],
                        [ 2,   4,  7,  17, 118   ]]
            self.m_B = [0.11,0.2235,0.28,0.3,0.14]
            self.m_K = [[0,0],
                        [0,0],
                        [0,0],
                        [0,0],
                        [0,0]]
        if cual == 3:                # problema 2 de la tarea   <---------------------
            self.m_A = [[ 5,-1,-1],
                        [ 1,-1, 2],
                        [ 3,-1, 2]]
            self.m_B = [3,0,4]
            self.m_K = [[0,0],
                        [0,0],
                        [0,0]]    

    def jacobi (self)-> None:  # <--------------------------
        mlon = len(self.m_A)
        print("Jacobi.".center((mlon+1)*13+5,"_"))
        titulo = "|_____X"
        for cr in range (mlon):
            titulo += "%1d"%(cr+1)
            if cr < mlon-1:
                titulo += "_____|_____X"
            else:
                titulo += "______|___Tolerancia___|"
        print (titulo)
        ##################################################### metodo
        tole = 1
        strikes = 0
        while tole > 0.00000005 and strikes < 8:
            tole_ant = tole
            anexo = ""
            tole = 0
            for cr in range (mlon):
                suma = 0
                divi = 0
                renglon = ""
                for cc in range (mlon):
                    if cr == cc:
                        divi = self.m_A[cr][cc]
                        continue
                    suma += self.m_A[cr][cc] * self.m_K[cc][0]
                    #renglon += "+ %12.6f * %12.6f"%(self.m_A[cr][cc],self.m_K[cc][0])
                self.m_K[cr][1] = (self.m_B[cr]-suma)/divi
                #print("((",self.m_B[cr]," - (",renglon," ) / ", divi)
                 
            for cr in range (mlon):
                tole += math.pow (self.m_K[cr][1] - self.m_K[cr][0],2)
                self.m_K[cr][0] = self.m_K[cr][1] 
                renglon += "|%12.6f"%(self.m_K[cr][0])
                
            tole = math.sqrt(tole)  
            if (tole_ant < tole): 
                strikes += 1          #<------------
                anexo = " <-*"
            else:
                strikes = 0       #<-- control de iteraciones que la toleracia o error sube
            print(renglon,"|-->%12.8f"%(tole),"|",anexo)  # renglon de datos
        ################################################### Linea final de tabla, tabla de resultados
        if strikes < 8:
            print("-".center((mlon+1)*13+5,"-"),"\n\n","Jacobi-->Resultado".center((mlon+1)*13+5,"_"))
            print(titulo)
            print(renglon,"|-->%12.8f"%(tole),"|\n","-".center((mlon+1)*13+5,"-")) 
        else:    
            print("-".center((mlon+1)*13+5,"-"),"\n\n","Jacobi-->Sin Resultado, No convergente".center((mlon+1)*13+5,"_"),"\n\n")

    def GaussSeidel (self)-> None:
        iteK = 0
        mlon = len(self.m_A)
        print("Gauss-Seidel.".center((mlon+1)*13+5,"_"))
        titulo = "|_____X"
        for cr in range (mlon):
            titulo += "%1d"%(cr+1)
            if cr < mlon-1:
                titulo += "_____|_____X"
            else:
                titulo += "______|___Tolerancia___|"
        print (titulo)
        ##################################################### metodo
        tole = 1
        strikes = 0
        while tole > 0.00000005 and strikes < 8:
            tole_ant = tole
            tole = 0
            anexo = ""
            for cr in range (mlon):                
                suma = 0
                divi = 0
                renglon = ""
                for cc in range (mlon):
                    if cr == cc:
                        divi = self.m_A[cr][cc]
                        continue
                    
                    if iteK == 0:  # diferencia con jacobi toma los valores recien calculados.
                        suma += self.m_A[cr][cc] * self.m_K[cc][0]
                    else:
                        if cc<cr:
                            suma += self.m_A[cr][cc] * self.m_K[cc][1]
                        else: 
                            suma += self.m_A[cr][cc] * self.m_K[cc][0]
                            
                    #renglon += "+ %12.6f * %12.6f"%(self.m_A[cr][cc],self.m_K[cc][0])
                self.m_K[cr][1] = (self.m_B[cr]-suma)/divi
                #print("((",self.m_B[cr]," - (",renglon," ) / ", divi)
                 
            for cr in range (mlon):
                tole += math.pow (self.m_K[cr][1] - self.m_K[cr][0],2)
                self.m_K[cr][0] = self.m_K[cr][1] 
                renglon += "|%12.6f"%(self.m_K[cr][0])
                
            tole = math.sqrt(tole)
            if (tole_ant < tole): 
                strikes += 1   
                anexo = " <-*"  
            else:
                strikes = 0                
            print(renglon,"|-->%12.8f"%(tole),"|",anexo)  # renglon de datos
            iteK += 1
        ################################################### Linea final de tabla, tabla de resultados
        if strikes < 8:
            print("-".center((mlon+1)*13+5,"-"),"\n\n","Gauss-Seidel-->Resultado".center((mlon+1)*13+5,"_"))
            print(titulo)
            print(renglon,"|-->%12.8f"%(tole),"|\n","-".center((mlon+1)*13+5,"-")) 
        else:    
            print("-".center((mlon+1)*13+5,"-"),"\n\n","Gauss-Seidel-->Sin Resultado, No convergente".center((mlon+1)*13+5,"_"),"\n\n")    

os.system('cls' if os.name == "nt" else 'clear')
mn_mat = metodos2()

print("Problema I \n")                
mn_mat.matrices(2)   #cargo los valores del problema 
mn_mat.jacobi()      #calculo del metodo
mn_mat.matrices(2)   #cargo los valores del problema para reiniciar las variables
mn_mat.GaussSeidel() #calculo del metodo

print("\n","*".center(60,"*"),"\nProblema II \n")
mn_mat.matrices(3)
mn_mat.jacobi()
mn_mat.matrices(3)
mn_mat.GaussSeidel()