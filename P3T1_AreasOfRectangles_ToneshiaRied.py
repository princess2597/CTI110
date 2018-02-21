#CTI-110
#P3T1-Areas of Rectangles
#Toneshia Ried
#February 20, 2018

rectangle1length = float( input( "Please enter the length of rectangle 1:"))

rectangle1width = float( input( "Please enter the length of width 1:"))

rectangle2length = float( input( "Please enter the length of rectangle 2:"))

rectangle2width = float( input( "Please enter the length of width 2:"))

rectangle1area = rectangle1length * rectangle1width

rectangle2area = rectangle2length * rectangle2width

if rectangle1area > rectangle2area:
    print("Rectangle 1 is bigger than Rectangle 2")
elif rectangle2area > rectangle1area: print("Rectangle 2 is bigger than Rectangle 1")
else: 
    print("Both rectangles are equal")
