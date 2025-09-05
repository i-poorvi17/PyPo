x=int(input("categories defined for gst \n\n 1.essentials(milk,eggs,fresh vegetables),healthcare,hopstialsand educational services \n\n 2. packaged food,transport,household essentials ,small vehicles,\n\n  3. Mobile Phones,processed foodS, all mostly goods and services , electronics and restaurants \n\n 4. luxury goods,tobacco products, expensive cars\t"))
total=0
cop=float(input("enter the cost of product"))
if(x==1):
    print(cop)
elif(x==2):
    total=cop+(0.05*cop)
    print('total amount=',total,'/-only')
elif(x==3):
    total=cop+(0.18*cop)
    print('total amount=',total,'/-only')
elif(x==4):
    total=cop+(0.40*cop)
    print('total amount=',total,'/-only')
else:
    print('invalid input')