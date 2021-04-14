
from unittest.main import main
import numpy as np
import matplotlib.pyplot as plt
from numpy.core.fromnumeric import mean, shape, transpose
from numpy.lib.polynomial import poly
from numpy.testing import verbose
# NO other imports are allowed

class Shape:
    '''
    DO NOT MODIFY THIS CLASS

    DO NOT ADD ANY NEW METHODS TO THIS CLASS
    '''
    def __init__(self):
        self.T_s = None
        self.T_r = None
        self.T_t = None
    
    
    def translate(self, dx, dy):
        '''
        Polygon and Circle class should use this function to calculate the translation
        '''
        self.T_t = np.array([[1, 0, dx], [0, 1, dy], [0, 0, 1]])
 

    def scale(self, sx, sy):
        '''
        Polygon and Circle class should use this function to calculate the scaling
        '''
        self.T_s = np.array([[sx, 0, 0], [0, sy, 0], [0, 0, 1]])
 
        
    def rotate(self, deg):
        '''
        Polygon and Circle class should use this function to calculate the rotation
        '''
        rad = deg*(np.pi/180)
        self.T_r = np.array([[np.cos(rad), np.sin(rad), 0],[-np.sin(rad), np.cos(rad),0], [0, 0, 1]])

        
    def plot(self, x_dim, y_dim):
        '''
        Polygon and Circle class should use this function while plotting
        x_dim and y_dim should be such that both the figures are visible inside the plot
        '''
        x_dim, y_dim = 1.2*x_dim, 1.2*y_dim
        plt.plot((-x_dim, x_dim),[0,0],'k-')
        plt.plot([0,0],(-y_dim, y_dim),'k-')
        plt.xlim(-x_dim,x_dim)
        plt.ylim(-y_dim,y_dim)
        plt.grid()
        plt.show()



class Polygon(Shape):
    '''
    Object of class Polygon should be created when shape type is 'polygon'
    '''
    def __init__(self, A):
        '''
        Initializations here
        '''
        Shape.__init__(self)
        self.polyco=A
        self.translate1=self.T_t #possible error
        self.scale1=self.T_s
        self.rotate1=self.T_r
         #create a tranpose for matrix multiplaction of A x transpose(t_t)

 
    
    def translate(self, dx, dy=None): # dx=dy
        '''
        Function to translate the polygon
    
        This function takes 2 arguments: dx and dy
    
        This function returns the final coordinates

        '''
        if dy is None:
            dy=dx
        self.oldxcords=self.polyco[:,0]
        self.oldycords=self.polyco[:,1]
        Shape.translate(self,dx,dy)
        transposematrix=np.transpose(self.T_t)

        # add the calling function

        transmatrix= np.dot(self.polyco,transposematrix) #matrix multiplication done
        xlist=transmatrix[:,0] #first column of matrix having changed x co-ordinates
        ylist=transmatrix[:,1] #second column of matrix having changed y coordinates

        self.polyco=np.column_stack((xlist,ylist,self.polyco[:,2]))

        return (np.round(xlist,2),np.round(ylist,2))


        

    
    def scale(self, sx, sy=None):
        '''
        Function to scale the polygon
    
        This function takes 2 arguments: sx and sx
    
        This function returns the final coordinates
        '''
        if sy is None:
            sy=sx

        Shape.scale(self,sx,sy)
        self.oldxcords=self.polyco[:,0]
        self.oldycords=self.polyco[:,1]


        self.columnsum=self.polyco.sum(axis=0)
        self.centerx=float(self.columnsum[0]) #calculate colum sumn of x
        self.centery=float(self.columnsum[1]) #calculate colum sum of y
        self.number=float(self.columnsum[2])  # calculate n for division


        self.meanx=self.centerx/self.number #final cX

        self.meany=self.centery/self.number #final cY

        self.newx=((self.polyco[:,0]-self.meanx))

        
        

        self.newy=(self.polyco[:,1]-self.meany)

        # self.finalmatrix=(np.array([self.newx,self.newy,self.polyco[:,2]])) #matrix with changed x
        self.finalmatrix=np.column_stack((self.newx,self.newy,self.polyco[:,2]))


        scalematrix=np.dot(self.finalmatrix,self.T_s) # multiply A x scale matrix
        scalexlist=(scalematrix[:,0])+self.meanx # x coordinates by selection 1st column+cX
        scaleylist=scalematrix[:,1]+self.meany # y coordinates by selcting 2nd column+ cY
        # self.polyco=np.column_stack((np.round(scalexlist),np.round(scaleylist),self.polyco[:,2]))
        self.polyco=np.column_stack((scalexlist,scaleylist,self.polyco[:,2]))
        return(np.round(scalexlist,2),np.round(scaleylist,2))
        # center part done
        
    
    def rotate(self, deg, rx = 0, ry = 0):
        '''
        Function to rotate the polygon
    
        This function takes 3 arguments: deg, rx(optional), ry(optional). Default rx and ry = 0. (Rotate about origin)
    
        This function returns the final coordinates
        '''
        if deg<0:
            deg=360+deg
        
        Shape.rotate(self,deg)
        self.oldxcords=self.polyco[:,0]
        self.oldycords=self.polyco[:,1]

        self.newrotatex=self.polyco[:,0]-rx

        self.newrotatey=self.polyco[:,1]-ry

        # self.rotatefinalmatrix=np.array([self.newrotatex,self.newrotatey,self.polyco[2]])
        self.rotatefinalmatrix=np.column_stack((self.newrotatex,self.newrotatey,self.polyco[:,2]))
        
        rotatematrix=np.dot(self.rotatefinalmatrix,np.transpose(self.T_r))
        self.polyco=rotatematrix
        rotatexlist=(rotatematrix[:,0])+ rx # x coordinates by selection 1st column+cX
        rotateylist=(rotatematrix[:,1])+ ry # y coordinates by selcting 2nd column+ cY

        # self.polyco=np.column_stack((np.round(rotatexlist,2),np.round(rotateylist,2),self.polyco[:,2]))
        self.polyco=np.column_stack((rotatexlist,rotateylist,self.polyco[:,2]))


        return(np.round(rotatexlist,2),np.round(rotateylist,2))









        

    

    def plot(self):
        '''
        Function to plot the polygon
    
        This function should plot both the initial and the transformed polygon
    
        This function should use the parent's class plot method as well
    
        This function does not take any input
    
        This function does not return anything
        '''
        n=len(self.oldxcords)
        limitx=np.abs(self.polyco[:,0])
        limity=np.abs(self.polyco[:,1])
        maxx=np.max(limitx)+10
        maxy=np.max(limity)+10
        


        plt.plot(self.oldxcords,self.oldycords,linestyle="dashed",color="r")
        plt.plot(np.array([self.oldxcords[0],self.oldxcords[n-1]]),np.array([self.oldycords[0],self.oldycords[n-1]]),linestyle="dashed",color="r")
        plt.plot(self.polyco[:,0],self.polyco[:,1],color="b")
        plt.plot(np.array([self.polyco[0,0],self.polyco[n-1,0]]),np.array([self.polyco[0,1],self.polyco[n-1,1]]),color="b")
        Shape.plot(self,maxx,maxy)
        

        
        # plt.show()
        


class Circle(Shape):
    '''
    Object of class Circle should be created when shape type is 'circle'
    '''
    def __init__(self, x=0, y=0, radius=5):
        '''
        Initializations here
        '''
        self.xcord=x
        self.ycord=y
        self.circlerad=radius
        self.matrix=np.array([[self.xcord,self.ycord,1],[0,0,1],[0,0,1]])

        




    
    def translate(self, dx, dy=None):
        '''
        Function to translate the circle
    
        This function takes 2 arguments: dx and dy (dy is optional).
    
        This function returns the final coordinates and the radius
        '''
        if dy is None:
            dy=dx
        self.circeloldcord=(self.xcord,self.ycord)
        self.circleoldrad=self.circlerad
        Shape.translate(self,dx,dy)
        transposematrix=np.transpose(self.T_t)

        transmatrix=np.dot(self.matrix,transposematrix)
        xlist=np.round(transmatrix[:,0],2) #first column of matrix having changed x co-ordinates
        ylist=np.round(transmatrix[:,1],2) #second column of matrix having changed y coordinates
        self.matrix=np.column_stack((xlist,ylist,self.matrix[:,2]))
        newxcord=transmatrix[0,0]
        newycord=transmatrix[0,1]

        return(np.round(newxcord,2),np.round(newycord,2),self.circlerad)

        

 
        
    def scale(self, sx):
        '''
        Function to scale the circle
    
        This function takes 1 argument: sx
    
        This function returns the final coordinates and the radius
        '''
        self.circeloldcord=(self.xcord,self.ycord)
        self.circleoldrad=self.circlerad
        newradius=abs((self.circlerad)*sx)
        self.circlerad=newradius
        return(np.round(self.matrix[0,0],2),np.round(self.matrix[0,1],2),round(newradius,2))
 
    
    def rotate(self, deg, rx = 0, ry = 0):
        '''
        Function to rotate the circle
    
        This function takes 3 arguments: deg, rx(optional), ry(optional). Default rx and ry = 0. (Rotate about origin)
    
        This function returns the final coordinates and the radius
        '''
        self.circeloldcord=(self.xcord,self.ycord)
        self.circleoldrad=self.circlerad
        Shape.rotate(self,deg)

        self.newrotatex=self.matrix[:,0]-rx


        self.newrotatey=self.matrix[:,1]-ry


        # self.rotatefinalmatrix=np.array([self.newrotatex,self.newrotatey,self.polyco[2]])
        self.rotatefinalmatrix=np.column_stack((self.newrotatex,self.newrotatey,self.matrix[:,2]))

        
        rotatematrix=np.dot(self.rotatefinalmatrix,np.transpose(self.T_r))
        
        self.polyco=rotatematrix
        rotatexlist=(rotatematrix[:,0])+ rx # x coordinates by selection 1st column+cX
        
        rotateylist=(rotatematrix[:,1])+ ry # y coordinates by selcting 2nd column+ cY

        self.matrix=np.column_stack((rotatexlist,rotateylist,self.matrix[:,2]))
        


        return(np.round(rotatexlist[0],2),np.round(rotateylist[0],2),self.circlerad)


        
 
    
    def plot(self):
        '''
        Function to plot the circle
    
        This function should plot both the initial and the transformed circle
    
        This function should use the parent's class plot method as well
    
        This function does not take any input
    
        This function does not return anything
        '''
        circle = plt.Circle(self.circeloldcord,self.circleoldrad, color='g', fill=False,linestyle="dashed")
        # fig, ax = plt.subplots()
        circle2 = plt.Circle((float(self.matrix[0,0]),float(self.matrix[0,1])),self.circlerad, color='g', fill=False)
        fig, ax = plt.subplots()  
        ax.add_patch(circle)
        ax.add_patch(circle2)
        maxx=abs(self.matrix[0,0])+10+self.circlerad
        maxy=abs(self.matrix[0,1])+10+ self.circlerad
        

        Shape.plot(self,maxx,maxy)
        
        # ax.set_aspect(1)
        # plt.show()

        
        

if __name__ == "__main__":
    '''
    Add menu here as mentioned in the sample output section of the assignment document.
    '''
    userverbose=int(input("enter 0 if you dont want graph otherwise enter 1\n"))
    testcaseno=int(input("enter the number of test case\n"))
    for no in range(testcaseno):
        usershape=int(input("enter 0 for polygon or 1 for circle\n"))

        if usershape==0 and userverbose==0:
            mainlist=[]
            polysides=int(input("enter the number of sides in the polygon\n"))
            for i in range(polysides):
                initlist=list(map(float,input("enter x y space seperated\n").split()))
                initlist.append(1)
                mainlist.append(initlist)
            finalcord=np.array(mainlist)
            menu=Polygon(finalcord)


            userquery=int(input("enter the number of query you want to perform\n"))
            for j in range(userquery):
                querylist=input("enter query\n").split()
                if querylist[0]=="T":
                    if len(querylist)==2:
                        print(*np.round(np.array([*menu.polyco[:,0],*menu.polyco[:,1]]),2))
                        menu.translate(float(querylist[1]))
                        print(*np.round(np.array([*menu.polyco[:,0],*menu.polyco[:,1]]),2))


                    elif len(querylist)==3:
                        print(*np.round(np.array([*menu.polyco[:,0],*menu.polyco[:,1]]),2))
                        menu.translate(float(querylist[1]),float(querylist[2]))
                        print(*np.round(np.array([*menu.polyco[:,0],*menu.polyco[:,1]]),2))

                
                elif querylist[0]=="R":
                    if len(querylist)==2:
                        print(*np.round(np.array([*menu.polyco[:,0],*menu.polyco[:,1]]),2))
                        menu.rotate(float(querylist[1]))
                        print(*np.round(np.array([*menu.polyco[:,0],*menu.polyco[:,1]]),2))

                    
                    elif len(querylist)==3:
                        print(*np.round(np.array([*menu.polyco[:,0],*menu.polyco[:,1]]),2))
                        menu.rotate(float(querylist[1]),float(querylist[2]))
                        print(*np.round(np.array([*menu.polyco[:,0],*menu.polyco[:,1]]),2))


                    elif len(querylist)==4:
                        print(*np.round(np.array([*menu.polyco[:,0],*menu.polyco[:,1]]),2))
                        menu.rotate(float(querylist[1]),float(querylist[2]),float(querylist[3]))
                        print(*np.round(np.array([*menu.polyco[:,0],*menu.polyco[:,1]]),2))
                        
                    

                elif querylist[0]=="S":
                    if len(querylist)==2:
                        print(*np.round(np.array([*menu.polyco[:,0],*menu.polyco[:,1]]),2))
                        menu.scale(float(querylist[1]))
                        print(*np.round(np.array([*menu.polyco[:,0],*menu.polyco[:,1]]),2))
                        
                    if len(querylist)==3:
                        print(*np.round(np.array([*menu.polyco[:,0],*menu.polyco[:,1]]),2))
                        menu.scale(float(querylist[1]),float(querylist[2]))
                        print(*np.round(np.array([*menu.polyco[:,0],*menu.polyco[:,1]]),2))
                        

                elif querylist[0]=="P":
                    menu.plot()





        if usershape==0 and userverbose==1:
            mainlist=[]
            polysides=int(input("enter the number of sides in the polygon\n"))
            for i in range(polysides):
                initlist=list(map(float,input("enter x y space seperated\n").split()))
                initlist.append(1)
                mainlist.append(initlist)
            finalcord=np.array(mainlist)
            menu=Polygon(finalcord)


            userquery=int(input("enter the number of query you want to perform\n"))
            for j in range(userquery):
                querylist=input("enter query\n").split()
                if querylist[0]=="T":
                    if len(querylist)==2:
                        menu.translate(float(querylist[1]))
                        menu.plot()
                        # Shape.plot(finalcord,finalcord[polysides-2,0],finalcord[polysides-2,1]) 
                    elif len(querylist)==3:
                        menu.translate(float(querylist[1]),float(querylist[2]))
                        menu.plot()
                
                elif querylist[0]=="R":
                    if len(querylist)==2:
                        menu.rotate(float(querylist[1]))
                        menu.plot()

                    elif len(querylist)==3:
                        menu.rotate(float(querylist[1]),float(querylist[2]))
                        menu.plot()

                elif querylist[0]=="S":
                    if len(querylist)==2:
                        menu.scale(float(querylist[1]))
                        menu.plot()

                    if len(querylist)==3:
                        menu.scale(float(querylist[1]),float(querylist[2]))
                        menu.plot()

                elif querylist[0]=="T":
                    if len(querylist)==2:
                        menu.translate(float(querylist[1]))
                        menu.plot()
                    elif len(querylist)==3:
                        menu.translate(float(querylist[1],float[querylist[2]]))
                        menu.plot()
                elif querylist[0]=="P":
                    menu.plot()

        if usershape==1 and userverbose==0:

            initlist=list(map(float,input("enter a b r space seperated\n").split()))
            menu=Circle(initlist[0],initlist[1],initlist[2])


            userquery=int(input("enter the number of query you want to perform\n"))
            for j in range(userquery):
                querylist=input("enter query\n").split()
                if querylist[0]=="T":
                    if len(querylist)==2:
                        print(*[menu.xcord,menu.ycord,menu.circlerad])
                        print(*menu.translate(float(querylist[1])))
                    elif len(querylist)==3:
                        print(*[menu.xcord,menu.ycord,menu.circlerad])
                        print(*menu.translate(float(querylist[1]),float(querylist[2])))
                
                elif querylist[0]=="R":
                    if len(querylist)==2:
                        print(*[menu.xcord,menu.ycord,menu.circlerad])
                        print(*menu.rotate(float(querylist[1])))
                    elif len(querylist)==3:
                        print(*[menu.xcord,menu.ycord,menu.circlerad])
                        print(*menu.rotate(float(querylist[1]),float(querylist[2])))
                elif querylist[0]=="S":
                    print(*[menu.xcord,menu.ycord,menu.circlerad])
                    print(*menu.scale(float(querylist[1])))
                elif querylist[0]=="P":
                    menu.plot()

        if usershape==1 and userverbose==1:

            initlist=list(map(float,input("enter a b r space seperated\n").split()))
            menu=Circle(initlist[0],initlist[1],initlist[2])


            userquery=int(input("enter the number of query you want to perform\n"))
            for j in range(userquery):
                querylist=input("enter query\n").split()
                if querylist[0]=="T":
                    if len(querylist)==2:
                        menu.translate(float(querylist[1]))
                        menu.plot()
                    elif len(querylist)==3:
                        menu.translate(float(querylist[1]),float(querylist[2]))
                        menu.plot()
                
                elif querylist[0]=="R":
                    if len(querylist)==2:
                        menu.rotate(float(querylist[1]))
                        menu.plot()
                    elif len(querylist)==3:
                        menu.rotate(float(querylist[1]),float(querylist[2]))
                        menu.plot()
                elif querylist[0]=="S":
                    menu.scale(float(querylist[1]))
                    menu.plot()
                elif querylist[0]=="P":
                    menu.plot()



















    
