# -*- coding: utf-8 -*-
"""
"""

import matplotlib.pyplot as mp
from Polylines import Polyline
from Points import Point2D

class PointPlotter(object):
    """Class to plot all the points and polylines with matplotlib    
    """
           
    def addCaption(self, caption):
        '''adds a caption to the figure
        '''
        mp.text(1,1,caption)
    
    
    def show(self):
        """shows plot"""
        mp.show()
    
    
    def plotPoint(self,point,colour='black'):
        """plots a point or a list of points"""
        if isinstance(point,Point2D):
            mp.scatter([point.get_x()],[point.get_y()],color=colour)
        elif isinstance(point,list):
            x=[]
            y=[]
            for p in point:
                if isinstance(p,Point2D):
                    x.append(p.get_x())
                    y.append(p.get_y())
            mp.scatter(x,y,color=colour)
    
    def set_axis(self,xlo,xhi,ylo,yhi):
        """sets axis to desired values"""
        mp.axis([xlo,xhi,ylo,yhi])
        mp.axis("equal")
        
   
        
    def plotPolylines(self,chains,colour='black'):
        """plots one or several polylines
        
        Input Parameter:
            chains – either a list of Polyline objects or one Polyline object
        
        """
        if isinstance(chains,Polyline):
            xys=chains.getPointsAsLists()
            mp.plot(xys[0],xys[1],color=colour)
        elif isinstance(chains,list):
            for chain in chains:
                if isinstance(chain,Polyline):
                    xys=chain.getPointsAsLists()
                    mp.plot(xys[0],xys[1],color=colour)   
    
    
