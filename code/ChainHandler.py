# -*- coding: utf-8 -*-
"""
"""

from Polylines import Polyline

def ChainLoader(fileName):
    """ Generates a Point field (passed as string) from and x-y file
    assuming first line is a header line"""
    lines = []
    chains = []
    
    myFile=open(fileName,'r')
    
    #iterate through all the file lines to get them into a list of Strings
    #makes it easier to deal with afterwards
    for line in myFile.readlines():
        lines.append(line)
        
    #now process all the lines
    atEnd=False

    lineno=0
    while not(atEnd):
        if lines[lineno].lstrip().upper()[0:3]=="END":
            atEndofblock=True
            atEnd=True
        else: 
            atEndofblock=False
            pl=Polyline()
            pl.setID(lines[lineno])
            lineno=lineno+1
        
        while not(atEndofblock):
            line=lines[lineno]
            if line.lstrip().upper()[0:3]=="END":
                atEndofblock=True
            else:
                items=line.split(',')
                x=float(items[0])
                y=float(items[1])
                pl.addPoint((x,y))
            lineno=lineno+1
        
        if  not(atEnd): 
            chains.append(pl)
        
    return chains


    
