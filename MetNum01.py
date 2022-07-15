import math
        
class metodos :
    def __init__(self) -> None:
        pass
 
    def f_d_x (self, cual,vx): 
        if (cual==1):
            return math.cos(vx)-3*vx
        if (cual==2):
            return math.log(vx)-0.2*vx*vx+1
        if (cual==3):
            return vx*vx-0.9*vx-1.52
        if (cual==4):
            return math.cos(vx)-math.pow(vx,3)
        
    def f_p_d_x (self, cual,vx): 
        if (cual==3):
            return 2*vx-0.9    

    def biseccion(self,x_iz,x_de,cual) -> None:
        ########################################## encabezado de la tabla
        print("Biseccion.".center(78,"_"))
        fxr = -1;
        print ("|","Xi".center(10,"_"),"|","F(Xi)".center(10,"_"),"|","Xd".center(10,"_"),
               "|","F(Xd)".center(10,"_"),"|","Xr".center(10,"_"),"|","F(Xr)".center(10,"_"),"|")
        ########################################## metodo
        while abs(fxr) > 0.0001:
            xr = (x_iz + x_de)/2          #calculo nuevo punto por bisecciion 
            fxi = self.f_d_x(cual,x_iz)   
            fxd = self.f_d_x(cual,x_de)
            fxr = self.f_d_x(cual,xr)
            print ("|%12.4f|%12.4f|%12.4f|%12.4f|%12.4f|%12.4f|" %(x_iz,fxi,x_de,fxd,xr,fxr))
            if fxr * fxi > 0:            # revisando si se sustituye xi (izquierda)    
                x_iz = xr
            if fxr * fxd > 0:            # revisando si se sustituye xd (derecha)    
                x_de = xr    
        
        ########################################## pie de la tabla y resultado
        print("".center(78,"-"))
        print ("Xr = %.6f    Error f(Xr) = %.6f \n" %(xr,fxr))
              
    def ReglaFalsa(self,x_iz,x_de,cual) -> None:
        ########################################## encabezado de la tabla
        print("Regla Falsa.".center(78,"_"))
        fxr = -1;
        print ("|","Xi".center(10,"_"),"|","F(Xi)".center(10,"_"),"|","Xd".center(10,"_"),
               "|","F(Xd)".center(10,"_"),"|","Xr".center(10,"_"),"|","F(Xr)".center(10,"_"),"|")
        ########################################## Metodo
        while abs(fxr) > 0.0001:
            fxi = self.f_d_x(cual,x_iz)
            fxd = self.f_d_x(cual,x_de)
            xr = (fxd * x_iz - fxi * x_de)/(fxd - fxi)    # calculo de punto por regla falsa
            fxr = self.f_d_x(cual,xr)
            print ("|%12.4f|%12.4f|%12.4f|%12.4f|%12.4f|%12.4f|" %(x_iz,fxi,x_de,fxd,xr,fxr))
            if fxr * fxi > 0:
                x_iz = xr
            if fxr * fxd > 0:
                x_de = xr             
       
        ########################################## pie de la tabla y resultado
        print("".center(78,"-"))
        print ("Xr = %.6f    Error f(Xr) = %.6f \n" %(xr,fxr))
    
    def NewtonRapson(self,xi,cual) -> None:
        ########################################## encabezado de la tabla
        print("Newton Rapson.".center(54,"_"))
        fx = self.f_d_x(cual,xi);
        print ("|","Xi".center(10,"_"),"|","f(Xi)".center(10,"_"),"|","f'(Xi)".center(10,"_"),
               "||","Xi+1".center(10,"_"),"|")
        ########################################## Metodo
        while abs(fx) > 0.0001:
            fx  = self.f_d_x(cual,xi)
            fpx = self.f_p_d_x(cual,xi)
            xj =  xi - fx / fpx            # calculo de punto por Newton Rapson
            print ("|%12.4f|%12.4f|%12.4f||%12.4f|" %(xi,fx,fpx,xj))
            if abs(fx) > 0.0001:
                xi = xj
                   
        ########################################## pie de la tabla y resultado
        print("".center(54,"-"))
        print ("Xi = %.6f    Error f(Xi) = %.6f \n" %(xi,fx))

    def secante(self,xh,xi,cual) -> None:
        ########################################## encabezado de la tabla
        print("Secante.".center(80,"_"))
        fxj = -1;
        print ("|","Xn-1".center(10,"_"),"|","f(Xn-1)".center(10,"_"),
               "|","Xn".center(10,"_"),  "|","f(Xn)".center(10,"_")  ,
              "||","Xn+1".center(10,"_"),"|","f(Xn+1)".center(10,"_"),"|")
        ########################################## Metodo
        while abs(fxj) > 0.0001:
            fxh = self.f_d_x(cual,xh)
            fxi = self.f_d_x(cual,xi)
            xj  = xi - ((xi - xh)/(fxi - fxh)) * fxi    # calculo de punto por Secante
            fxj = self.f_d_x(cual,xj)
            print ("|%12.4f|%12.4f|%12.4f|%12.4f||%12.4f|%12.4f|" %(xh,fxh,xi,fxi,xj,fxj))
            xh = xi
            xi = xj
                   
        ########################################## pie de la tabla y resultado
        print("".center(80,"-"))
        print ("Xn = %.6f    Error f(Xn) = %.6f \n" %(xj,fxj))
        
met_num = metodos();
met_num.biseccion(0.001,1,2)       # parametros x izq, x der,  funcion elegida
print()
met_num.ReglaFalsa(0.001,1,2)      # parametros x izq, x der,  funcion elegida       
print()        
met_num.NewtonRapson(1.5,3)        # parametros xi,  funcion elegida    
print() 
met_num.secante(0.5,0.6,4)
