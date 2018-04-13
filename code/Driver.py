"""This is the driver"""

from PointPlotter import PointPlotter
from ChainHandler import ChainLoader

xlo=0.0
xhi=1000.0
ylo=0.0
yhi=1000.0


pp=PointPlotter()
pp.set_axis(xlo, xhi, ylo, yhi)

chain=ChainLoader("data/Wiggle8.txt") #load data
pp.plotPoint(chain[0]._allPoints, 'black') #plot points

#change the number 40.0 here to apply the generalisation with different treshold
pp.plotPolylines(chain[0].generalise(30.0), 'red') #generalise and plot generalised line
#pp.addCaption("Wiggle4.txt with \nPeucker Line Generalisation") #add a caption
pp.show()#show graph