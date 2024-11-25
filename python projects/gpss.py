from gmplot import gmplot
import csv

gmap =gmplot.GoogleMapPlotter(28.689169, 77.334526, 17)
gmap.coloricon="http://www.googlemapsmarkers.com/v1/%s/"
with open("C:/Users/surya/Downloads/route.csv","r") as f:
    read=csv.reader(f)
    k=0
    
    for i in read:
        lat=float(i[0])
        long=float(i[1])
        
        if k==0:
            gmap.marker(lat,long,"red")
            k =1
        else:
            gmap.marker(lat,long,"blue")
            
gmap.marker(lat,long,"pink")

gmap.draw("mymap.html")