# -*- coding: utf-8 -*-
"""
"""
from Points import Point2D
from Points import Dpoint

class Polyline(object):
    
    '''A class to represent 2-D points'''

    def __init__(self,arg=None):
      if isinstance(arg, list) or isinstance(arg, tuple):
          self._allPoints = []
          for point in arg:
              if isinstance(point, Point2D):
                  self._allPoints.append(point.clone ())
      elif isinstance(arg, Point2D):
          self._allPoints = [arg.clone()]
      else:
          self._allPoints = []
      self.id=None
          
    def size(self):
        """Returns size of Polyline
        
        Returns:
            an Integer
        
        """
        return len(self._allPoints)    
    
    def getPoint(self,i):
        """Returns point at position i"""
        return self._allPoints[i]
        
    def getPoints(self):
        """Returns all the points in the Polyline
        
        Returns:
            a list
        
        """
        return self._allPoints
        
    def getPointsAsLists(self):
        """Returns a tuple of two lists with x and y values of points.
        
        Returns:
            (x,y) – a tuple with two lists
        
        """
        x=[]
        y=[]
        for p in self._allPoints:
            x.append(p.get_x())
            y.append(p.get_y())
        return (x,y)
        
# Returns start Point
    def getStart(self):
        """returns start Point of the Polyline
        
        """
        if (len(self._allPoints)>0):
            return self.getPoint(0)
        else:
            return None 


    def getEnd(self):
        """returns end Point of the Polyline
        
        """
        if (len(self._allPoints)>0):
            return self.getPoint(self.size()-1)
        else:
            return None


        
    def setID(self,id):
        """sets ID of Polyline"""
        self.id=id

    def addPoint(self,point):
        """Adds a Point to the Polyline"""
        if isinstance(point, Point2D):
            self._allPoints.append(point.clone ())
        elif isinstance(point, tuple):
            self._allPoints.append(Point2D(point[0],point[1]))
      

    
    def furthestFromSeg(self):
        """calculates the furthest point from the segment
        returns the furthest point from the polyline
        
        Throws:
            AssertionError if the size of the Polyline is smaller than 2
        
        Returns:
            a DPoint object
        
        """
        
        assert self.size()>=2
        
        segment = self.getStartEndSeg() #create a new segment

        #initial values  (before entering the loop to have a reference distance)    
        maxdist = 0
        maxpoint = None
        
        #iterate through points 2 to (n-1)
        for i in range(1,self.size()-1): #-1 and +1 because exclude first and last element
            intersect = segment.getClosest(self.getPoint(i)) # get closest intersect point
            dist = self.getPoint(i).distance(intersect)
            if dist >=maxdist:
                maxdist=dist # set new maximal distance
                maxpoint = Dpoint(self.getPoint(i).get_x(), self.getPoint(i).get_y(), dist, i) #set new maximum distance point, created a Dpoint object extending the Point2D class with distance and index
        print("Furthest Point: ", maxpoint)
        print("Furthest Distance: ", maxdist)
        
        return maxpoint #return point with maximum distance to segment
    
    
    
    
    
    
    def combinePolyline(self, l1, l2):
        """Combines the two input polylines to one Polyline object
        
        Input Parameter:
            l1 – a polyline
            l2 – another polyline
        
        Throws:
            AssertionError if last element of l1 is not first element of l2
        
        Returns:
            a Polyline object containing the combined Point2D's
        
        """
        assert l1.getPoints()[-1].equals(l2.getPoints()[0]) # assert that last point of first polyline equals first point of second polyline
        
        combList = l1.getPoints()[:-1] + l2.getPoints() # exclude the last element of the first chain to not have it doubled
        return Polyline(combList) # return combined list
    
    
    
    
    
    def getStartEndSeg(self):
        """returns a segment of the start and end of the polyline
        
        """
        assert self.size()>=2 # asserts that length of the Polyline is at least 2
        
        segment = Segment(self.getStart(), self.getEnd()) #create a segment
        return segment
    
    

    
    
    def split(self, index):
        """Splits a polyline into two polylines at index i
        
        Input Parameter:
            index – index at which the Polyline object should be splitted
        
        Returns:
            A tuple with the two subpolylines
            
        """     
        points1 = self.getPoints()[0:index+1]
        points2 = self.getPoints()[index:]
        return (Polyline(points1), Polyline(points2))
    
    
    
    
    
    def generalise(self, t):
        """generalises a Polyline using the Douglas-Peuker line generalisation algorithm
        recursive function, calling itself
        
        Input Parameter:
            t - tolerance
                
        Returns:
            a Polyline object
            
        """
        if (self.size()<3): #check if that there are less than 2 points in the chain
            print("No more points")
            return self #polyline is returned
        else:
            furthest=self.furthestFromSeg() #get the point which is the furthest from the segment
            
            if (furthest.getD()<t): # check if within tolerance, detD gets the distance
                
                print("Within tolerance {}, max dist at {}".format(t, furthest))
                newSeg = self.getStartEndSeg() # create a segments
                print("returning {}, max dist at {}".format(t, furthest))
                return newSeg.segAsPolyline() #returns segment as Polyline object
            
            else:
                # split the polyline at index of furthest object
                print("Splitting at {}".format(furthest))
                v=self.split(furthest.getI()) # split the Polyline, v is a tuple with the subchains
                
                c1=v[0] # extract first sub chain
                c2=v[1] # extract second sub chain
                
                c1=c1.generalise(t) #recursive call with subchain1
                c2=c2.generalise(t) #recursive call with subchain2
                
                return self.combinePolyline(c1,c2) # return the combined Polyline objects
        
    
     
    def __repr__(self):
        """object representation
        
        """
        rep = "{"
        for i in self.getPoints():
            rep += str(i) + ", "
        rep+= "}"
        return rep
    
    
    def __str__(self):
        """object string representation
        
        """
        return self.__repr__() #calls the repr method
    
    
  

      
class Segment(object):
    """Class representing a segment of two points
    
    responsible for calculations with this segment such as calculating line intersect points
    
    """
    
    def __init__(self,*args):
        """creates a segment object
        
        Input Parameter:
            list of 4 coordinates (x1, y1, x2, y2)
            OR list with a tuple of two Point2D objects
            OR list with two Point2D objects
        
        """
        if len(args)==4:
             p1=Point2D(args[0],args[1])
             p2=Point2D(args[2],args[3])
             self._segPoints=(p1,p2)
        elif len(args)==1:
             plist=args[0]
             p1=plist[0]
             p2=plist[1]
             self._segPoints=(p1.clone(),p2.clone())
        else:
             p1=args[0]
             p2=args[1]
             self._segPoints=(p1.clone(),p2.clone())
             
         
             
    def getStart(self):
        return self._segPoints[0]
    
    def getEnd(self):
        return self._segPoints[1]
        
    def getIntersectLine(self,point):
        """Helper method to return intersect point on the segment line (from a point)
        i.e. closest point on the segment line from another point
        
        Input parameter:
            point – 2Dpoint to calculate the closest instersect from
        
        Returns:
            a Point2D object
        
        """
        x1=self.getStart().get_x()
        y1=self.getStart().get_y()
        x2=self.getEnd().get_x()
        y2=self.getEnd().get_y()
        x3=point.get_x()
        y3=point.get_y()
        # calculate intersection
        m1 = (y2-y1)/(x2-x1)
        c1 = y1-(m1*x1)
        c2 = y3+(x3/m1)
        x4 =(c2-c1)/(m1+(1./m1))
        y4=(m1*x4)+c1
        return Point2D(x4,y4)
        

    def inXRange(self,point):
        """checks if a point is within the x-axis range of the segment
        
        Input Parameter:
            a Point2D object
        
        Returns: 
            true if it is in x range
            false if it is not
        
        """
        x1=self._segPoints[0].get_x()
        x2=self._segPoints[1].get_x()
        px=point.get_x()
        
        minx=min(x1,x2)
        maxx=max(x1,x2)
        
        return (px>=minx)and(px<=maxx)
        
                
    def getIntersect(self,point):
        """ returns the intersect point on the segment line (from a point)
        uses getIntersectLine as helper function
        
        Input parameter:
            point – 2Dpoint to calculate the closest instersect from
        
        Returns:
            a Point2D object
            None if the input-point is not in the x-range of the segment
        
        """
        ip=self.getIntersectLine(point)
        if self.inXRange(ip):
            return ip
        else:
            return None
            
    def getClosest(self,point):
        """calculates the closest intersect point on a segment.
        If point is outside x range the closest distance to either end or start point is returned
        
        Input Parameter:
            point – a Point2D object
        
        Returns:
            a Point2D object
        
        """
        ip=self.getIntersectLine(point)
        if self.inXRange(ip):
            return ip
        else:
            d1=self._segPoints[0].distance(point) #distance to startpoint
            d2=self._segPoints[1].distance(point) #distance to endpoint
            if d1<d2: # take smaller distance
                return self._segPoints[0]
            else:
                return self._segPoints[1]
                

    def segAsPolyline(self):
        """creates a Polyline object out of itself
        
        Returns:
            a Polyline object
        
        """
        return Polyline([self.getStart(), self.getEnd()])
        
     