import numpy as np
import matplotlib.pyplot as plt
from numpy.core.fromnumeric import mean
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
        # self.translate=self.T_t #possible error
        # self.scale=self.T_s
        # self.rotate=self.T_r
         #create a tranpose for matrix multiplaction of A x transpose(t_t)

 
    
    def translate(self, dx, dy): # dx=dy
        '''
        Function to translate the polygon
    
        This function takes 2 arguments: dx and dy
    
        This function returns the final coordinates

        '''
        Shape.translate(self,dx,dy)
        transposematrix=np.transpose(self.T_t)

        # add the calling function
        print(self.polyco)

        transmatrix= np.dot(self.polyco,transposematrix) #matrix multiplication done
        xlist=np.round(transmatrix[:,0],2) #first column of matrix having changed x co-ordinates
        ylist=np.round(transmatrix[:,1],2) #second column of matrix having changed y coordinates

        return (xlist,ylist)
        

    
    # def scale(self, sx, sy):
    #     '''
    #     Function to scale the polygon
    
    #     This function takes 2 arguments: sx and sx
    
    #     This function returns the final coordinates
    #     '''

    #     Shape.scale(self,sx,sy)


    #     self.columnsum=self.polyco.sum(axis=0)
    #     self.centerx=float(self.columnsum[0]) #calculate colum sumn of x
    #     self.centery=float(self.columnsum[1]) #calculate colum sum of y
    #     self.number=float(self.columnsum[2])  # calculate n for division
    #     print(self.centerx)
    #     print(self.centery)
    #     print(self.number)

    #     self.meanx=self.centerx/self.number #final cX

    #     self.meany=self.centerx/self.number #final cY

    #     self.newx=((self.polyco[:,0]-self.meanx))
    #     print(self.newx)
        
        

    #     self.newy=(self.polyco[:,1]-self.meany)

    #     # self.finalmatrix=(np.array([self.newx,self.newy,self.polyco[:,2]])) #matrix with changed x
    #     self.finalmatrix=np.column_stack((self.newx,self.newy,self.polyco[:,0]))
    #     print(self.finalmatrix)

    #     scalematrix=np.dot(self.finalmatrix,self.T_s) # multiply A x scale matrix
    #     scalexlist=(scalematrix[:,0])+self.meanx # x coordinates by selection 1st column+cX
    #     scaleylist=scalematrix[:,1]+self.meany # y coordinates by selcting 2nd column+ cY
    #     return(np.round(scalexlist,2),np.round(scaleylist,2))
    #     # center part done

    def rotate(self, deg, rx = 0, ry = 0):
        '''
        Function to rotate the polygon
    
        This function takes 3 arguments: deg, rx(optional), ry(optional). Default rx and ry = 0. (Rotate about origin)
    
        This function returns the final coordinates
        '''
        Shape.rotate(self,deg)

        self.newrotatex=self.polyco[:,0]-rx

        self.newrotatey=self.polyco[:,1]-ry
        

        # self.rotatefinalmatrix=np.array([self.newrotatex,self.newrotatey,self.polyco[2]])
        self.rotatefinalmatrix=np.column_stack((self.newrotatex,self.newrotatey,self.polyco[:,0]))

        rotatematrix=np.dot(self.rotatefinalmatrix,np.transpose(self.T_r))
        
        rotatexlist=(rotatematrix[:,0])+ rx # x coordinates by selection 1st column+cX
        rotateylist=(rotatematrix[:,1])+ ry # y coordinates by selcting 2nd column+ cY
        
        self.polyco=np.column_stack((np.round(rotatexlist,2),np.round(rotateylist,2),self.polyco[:,2]))

        print(self.polyco)

        


        return(np.round(rotatexlist,2),np.round(rotateylist,2))



inp = np.array([[1.0, 1.0, 1.0], [1.0, 5.0, 1.0], [5.0, 5.0, 1.0], [5.0, 1.0, 1.0]])

testing=Polygon(inp)
ta=testing.rotate(90)
tb=testing.translate(2,2)
print(tb)
