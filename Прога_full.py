import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
class Difraction:
    def __init__(self,liambda,N,d,b):
        self.liam=liambda/1000
        self.b=b
        self.d=d
        self.N=N
        self.color="white"
        self.clr()
    def calc(self):
        pi=np.pi
        pred=self.liam/self.b
        m=int(10*self.N*self.d/self.b)
        sn=np.linspace(-pred, pred, 2*m, dtype="float64")
        u=(pi*self.b*sn)/self.liam
        r=(pi*self.d*sn)/self.liam
        y=(((np.sin(u)/u)**2)*(((np.sin(self.N*r)/np.sin(r))))**2)/self.N**2   
        return sn, y
    def show1(self):
        mx=int(self.d/self.b)#mx-1
        x,y=self.calc()
        plt.plot(x,y)
        plt.xlabel("sin($\phi$)")
        plt.ylabel("I, отн.ед")
        plt.title(f"Зависимость интенсивности для {self.N} щелей.")
        pred=self.liam/self.b
        plt.xlim([-pred, pred])
        plt.text(0.5*pred, 0.9, f"$\lambda$={1000*self.liam} нм", size=15)
        plt.text(0.5*pred, 0.8, f"b={self.b} мкм ", size=15)
        plt.text(0.5*pred, 0.7, f"d={self.d} мкм", size=15)
        plt.grid(True)
        plt.show()
    def show2(self):
        if self.color!="white":
            pi=np.pi
            step=self.liam/self.d
            sn=np.array([0.00001])
            for i in range(1,int(self.d/self.b)):
                k=i*step
                sn=np.append(sn,k)
                sn=np.append(sn,-k)
            u=(pi*self.b*sn)/self.liam
            y=(np.sin(u)/u)**2
            for i in range(len(sn)):
                plt.axvline(sn[i], 0, 1, color=self.color, linewidth=3, alpha=y[i])
            pred=self.liam/self.b
            plt.xlim([-pred, pred])
            ax=plt.gca()
            ax.get_yaxis().set_visible(False)
            plt.title(f"Дифракционная картина для {self.N} щелей")
            plt.text(0.5*pred, 0.9, f"$\lambda$={1000*self.liam} нм", size=15)
            plt.text(0.5*pred, 0.8, f"b={self.b} мкм ", size=15)
            plt.text(0.5*pred, 0.7, f"d={self.d} мкм", size=15)
            plt.xlabel("sin($\phi$)")
            plt.show()
        else:
            print("Свет не из видимого диапазона длин волн")
            print("Невозможно смоделировать дифракционную картину")
    def show3(self):
        if self.color!="white":
            x,y=self.calc()
            for i in range(len(x)):
                plt.axvline(x[i], 0, 1, color=self.color, linewidth=3, alpha=y[i])
            pred=self.liam/self.b
            plt.xlim([-pred, pred])
            ax=plt.gca()
            ax.get_yaxis().set_visible(False)
            plt.title(f"Дифракционная картина для {self.N} щелей")
            plt.text(0.5*pred, 0.9, f"$\lambda$={1000*self.liam} нм", size=15)
            plt.text(0.5*pred, 0.8, f"b={self.b} мкм ", size=15)
            plt.text(0.5*pred, 0.7, f"d={self.d} мкм", size=15)
            plt.xlabel("sin($\phi$)")
            plt.show()
        else:
            print("Свет не из видимого диапазона длин волн")
            print("Невозможно смоделировать дифракционную картину")
    def clr(self):
        liam=self.liam
        clr=""
        if 0.38<=liam<=0.45:
            clr="violet"
        elif 0.45<liam<=0.48:
            clr="blue"
        elif 0.48<liam<=0.51:
            clr="cyan"
        elif 0.51<liam<=0.55:
            clr="green"
        elif 0.55<liam<=0.57:
            clr="lightgreen"
        elif 0.57<liam<=0.59:
            clr="yellow"
        elif 0.59<liam<=0.63:
            clr="orange"
        elif 0.63<liam<=0.780:
            clr="red"
        else:
            print("Свет не из видимого диапазона длин волн")
        self.color=clr
        print(clr)
class Interference():
    def __init__(self, liambda, dliam, d, l=0):
        self.liam=liambda/1000
        self.dlm=dliam/1000
        self.d=d
        self.l=l
        self.color="white"
        self.clr()
    def clr(self):
        liam=self.liam
        clr=""
        if 0.38<=liam<=0.45:
            clr="violet"
        elif 0.45<liam<=0.48:
            clr="blue"
        elif 0.48<liam<=0.51:
            clr="cyan"
        elif 0.51<liam<=0.55:
            clr="green"
        elif 0.55<liam<=0.57:
            clr="lightgreen"
        elif 0.57<liam<=0.59:
            clr="yellow"
        elif 0.59<liam<=0.63:
            clr="orange"
        elif 0.63<liam<=0.780:
            clr="red"
        else:
            print("Свет не из видимого диапазона длин волн")
        self.color=clr
        print(clr)
    def Young(self):
        mx=int(self.liam/self.dlm)
        pred=((mx+1)*self.liam*self.l)/self.d
        dx=self.liam*self.l/self.d
        fig, ax=plt.subplots()
        ax.set_facecolor(self.color)
        ax1=plt.gca()
        ax1.get_yaxis().set_visible(False)
        #ax.add_patch(Rectangle((-dx/4,0),dx/2, 1, color=self.color))
        for i in range(2*mx+1):
            if i%2==1:
                ax.add_patch(Rectangle((-dx/4+i*dx/2,0), dx/2, 1, color="black", alpha=1-i/(2*mx)))
                ax.add_patch(Rectangle((-dx/4-i*dx/2,0), dx/2, 1, color="black", alpha=1-i/(2*mx)))
            else:
                ax.add_patch(Rectangle((-dx/4+i*dx/2,0), dx/2, 1, color=self.color))
                ax.add_patch(Rectangle((-dx/4-i*dx/2,0), dx/2, 1, color=self.color))
        plt.xlim([-pred, pred])
        plt.title("Интерференционная картина для схесы Юнга")
        plt.text(0.5*pred, 0.9, f"$\lambda$={1000*self.liam} нм", size=15)
        plt.text(0.5*pred, 0.8, f"$\delta$$\lambda$={1000*self.dlm} нм ", size=15)
        plt.text(0.5*pred, 0.7, f"d={self.d} cм", size=15)
        plt.text(0.5*pred, 0.6, f"l={self.l} cм", size=15)
        plt.show()
    def Newt(self):
        mx=int(self.liam/self.dlm)
        rm=(mx*20000*self.liam*self.d)**0.5
        fig, ax=plt.subplots()  
        ax.set_facecolor(self.color)
        plt.axis([-rm,rm,-rm,rm])
        plt.axis("equal")
        for i in range(mx,0, -1):
                r=(10000*self.liam*i*self.d)**(0.5)
                a=1-i/mx
                plt.gca().add_artist(plt.Circle((0,0), radius=r, color="black", alpha=a))
                if i!=0:
                    r=(10000*(i-0.5)*self.liam*self.d)**(0.5)
                    plt.gca().add_artist(plt.Circle((0,0), radius=r, color=self.color, alpha=1))
                else:
                    r=(10000*0.5*self.liam*self.d)**(0.5)
                    plt.gca().add_artist(plt.Circle((0,0), radius=r, color=self.color, alpha=1))
        plt.title("Интерференционная картина колец Ньютона")
        plt.text(0.6*rm, 0.6*rm, f"$\lambda$={1000*self.liam} нм", size=15)
        plt.text(0.6*rm, 0.5*rm, f"$\delta$$\lambda$={1000*self.dlm} нм ", size=15)
        plt.text(0.6*rm, 0.4*rm, f"R={self.d} cм", size=15)
        plt.show()
a=Difraction(700, 10, 20, 2)
a.show1()
a.show2()
a.show3()
b=Interference(400,30, 2, 200)
b.Young()
c=Interference(600, 20, 10)
c.Newt()

