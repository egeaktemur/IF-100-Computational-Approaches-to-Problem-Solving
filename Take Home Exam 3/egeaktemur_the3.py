# -*- coding: utf-8 -*-
"""egeaktemur_the3.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1iKEQFfgFxMPnDHGBZ1e20CeByefFO6NZ
"""

#Ege Aktemur
shopcart = input("Products in shopping cart: ")
usnumber = shopcart.count("_")
commanumber = shopcart.count(",")
while usnumber<4 or usnumber!=((commanumber+1)*4):
  print("Invalid input for products, please enter in correct format.")
  shopcart = input("Products in shopping cart: ")
  usnumber = shopcart.count("_")
  commanumber = shopcart.count(",")
locoffirstus = shopcart.find("_")
totalfat = 0
totalcarbohydrate = 0
totalprotein = 0
itemsinshopcart = commanumber+1
numinfo1 = str(shopcart[locoffirstus+1:shopcart.find(",")])
while commanumber+1 > 0:
  locoffirstcomma = shopcart.find(",")
  locoffirstus = shopcart.find("_")
  quantity1 = str(numinfo1[0:numinfo1.find("_")])
  fat1 = str(numinfo1[numinfo1.find(quantity1)+len(quantity1)+1:numinfo1.find("_",numinfo1.find("_")+1)])
  carbohydrate1 = str(numinfo1[numinfo1.find(fat1)+len(fat1)+1:numinfo1.find("_",numinfo1.find(fat1)+len(fat1)+1)])
  protein1 = str(numinfo1[numinfo1.find(carbohydrate1)+len(carbohydrate1)+1:])
  totalfat = (totalfat + (int(quantity1)*int(fat1)))
  totalcarbohydrate = totalcarbohydrate + (int(quantity1)*int(carbohydrate1))
  totalprotein = totalprotein + (int(quantity1)*int(protein1))
  shopcart= shopcart[shopcart.find(",")+1:]
  if shopcart.count(",")>0:
    numinfo1= shopcart[shopcart.find("_")+1:shopcart.find(",")]
  else:
    numinfo1=shopcart[shopcart.find("_")+1:]
  commanumber = (int(commanumber)-1)
faminfo = input("Family members' informations: ")
while faminfo.count("_") < 3 or faminfo.count("_") != ((faminfo.count(",")+1)*3):
  print("Invalid input for family information, please enter in correct format.")
  faminfo = input("Family members' informations: ")
fammembernum = (faminfo.count(",")+1)
malecount= 0
femalecount= 0
mancalo=0
femalecalo=0
faminfo1= faminfo[0:faminfo.find(",")]
mancalonew=0
femalecalonew=0
while fammembernum>0:
  locof1stcom=faminfo.find(",")
  locof1stus=faminfo.find("_")
  mancalonew=0
  femalecalonew=0
  if faminfo1[0:1]=="M":
    manweight=((faminfo1[faminfo1.find("_")+1:faminfo1.find("_",2)]))
    manheight=((faminfo1[faminfo1.find(manweight)+len(manweight)+1:faminfo1.find("_",faminfo1.find(manweight)+len(manweight)+3)]))
    manage=((faminfo1[(faminfo1.find(manheight)+len(manheight)+1):faminfo.find(",")]))
    mancalonew=(66.5)+(13.8*int(manweight))+(5*int(manheight))-(6.8*int(manage))
  elif faminfo1[0:1]=="F":
    femaleweight=((faminfo1[faminfo1.find("_")+1:faminfo1.find("_",2)]))
    femaleheight=((faminfo1[faminfo1.find(femaleweight)+len(femaleweight)+1:faminfo1.find("_",faminfo1.find(femaleweight)+len(femaleweight)+3)]))
    femaleage=((faminfo1[(faminfo1.find(femaleheight)+len(femaleheight)+1):]))
    femalecalonew=(655.1+(9.6*int(femaleweight))+(1.9*int(femaleheight))-(4.7*int(femaleage)))
  fammembernum=fammembernum-1
  femalecalo=femalecalo+femalecalonew
  mancalo=mancalo+mancalonew
  faminfo= faminfo[faminfo.find(",")+1:]
  if faminfo.count(",")>0:
    faminfo1= faminfo[0:faminfo.find(",")]
  else:
    faminfo1=faminfo
allcaloneeded=femalecalo+mancalo
neededcarbo=allcaloneeded/2
neededfat=allcaloneeded*3/10
neededprotein=allcaloneeded*1/5
if (9*totalfat)<neededfat:
  print("You need to add products with more fat to your shopping cart.")
if (9*totalfat)>neededfat:
  print("These products will be enough for your family in terms of fat for",format(9*totalfat/neededfat,".0f"),"days.")
if (4*totalcarbohydrate)<neededcarbo:
  print("You need to add products with more carb to your shopping cart.")
if (4*totalcarbohydrate)>neededcarbo:
  print("These products will be enough for your family in terms of carbohydrate for",format(4*totalcarbohydrate//neededcarbo,".0f"),"days.")
if (4*totalprotein)<neededprotein:
  print("You need to add products with more protein to your shopping cart.")
if (4*totalprotein)>neededprotein:
  print("These products will be enough for your family in terms of protein for",format(4*totalprotein//neededprotein,".0f"),"days.")