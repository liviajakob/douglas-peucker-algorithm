# -*- coding: utf-8 -*-
"""
"""

import math

class Point2D(object):
    '''A class to represent 2-D points'''


    def __init__(self,x,y):  
        #ensure points are always reals
        self._x=x*1.
        self._y=y*1.
        
        
    def equals(self, point):
        """checks if an input point is equal to itself
        
        Returns:
            true if euqual
            false if not equal
        """
        if str(point) == str(self):
            return True
        else:
            return False
      
        
              
    def clone(self):
        """returns a clone of itself (another identical Point2D object)"""
        return Point2D(self._x,self._y)
   
    def get_x(self):
        return self._x
                  
    def get_y(self):
        return self._y
             
    def get_xys(self):
        """return x,y tupel 
        """
        return (self.x,self._y)        

         
    def distance(self, other_point):    
        """Returns distance between points
        
        """
        xd=self._x-other_point._x
        yd=self._y-other_point._y
        return math.sqrt((xd*xd)+(yd*yd))
     
          
            
    def __str__(self):
        return ('x={:.2f} y={:.2f}').format(self._x, self._y)

    


class PointField(object):
    '''A class to represent a field (collection) of points'''
    
    def __init__(self,PointsList=None):
        self._allPoints = []
        if isinstance(PointsList, list):
            self._allPoints = []
            for point in PointsList:
                if isinstance(point, Point2D):
                    self._allPoints.append(point.clone())
  
    def getPoints(self):
        return self._allPoints
        
    def size(self):
        """Returns length"""
        return len(self._allPoints)
    
    
    

class Dpoint(Point2D):
    """Class extending the Point2D with distance and index
    
    """
    def __init__(self, x, y, d=None, i=None):
        Point2D.__init__(self, x, y)
        self._distance=d
        self._index=i
        
    def setD(self, d):
        """Returns distance
        """
        self._distance=d  
        
        
    def getD(self):
        return self._distance;
    
    def setI(self, i):
        self._index=i
    def getI(self):
        return self._index