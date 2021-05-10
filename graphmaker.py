import matplotlib.pyplot as plt 
from matplotlib import style 
import pandas as pd
import numpy as np
import xlsxwriter 
from emoji import emojize
from sklearn import linear_model
from openpyxl.workbook import workbook

w=('WELCOME TO GRAPH MAKER')
print(w.center(50,'-'))

while True:
    
    print("\n type 1 if you want to input the data here \n type 2 if you want to want to make a graph from a csv file or a excel file \n type 3 if you want to want to make a graph from a TEXT file")
    t=int(input())
    
    if t==1:
        print("\n Graph you need \n 1 for Line Graph \n 2 for Bar Chart \n 3 for Pie Chart \n 4 for Scatter Graph")
        d=int(input())
        STY=input("enter style (bmh or classic or dark_background)").lower()
        style.use(STY.split()) 
        if d==1:
            n=int(input("enter number of lines"))
            
            for i in range(1,n+1):
                x=eval(input("enter x points of line " + str(i)))
                y=eval(input("enter y points of line " + str(i)))
                l=input("do you want to add legend for this line").lower()
                le=l.split()
                if le[0]=='yes':
                    la=input("enter name for the legend of this line")
                else:
                    la=' '
                plt.plot(x,y,label=la)
                plt.legend()
            
            plt.title(input("enter title for line graph"))
            plt.xlabel(input("enter label for x axis"))
            plt.ylabel(input("enter label for y axis"))
            plt.show()
        elif d==2:
            n=int(input("enter number of bar charts required"))
            
            for i in range(1,n+1):
                x=(input("enter x label of bar number "+ str(i)))
                y=input("enter correponding y coordinate")
                le=l.split()
                if le[0]=='yes':
                    la=input("enter name for the legend of this line")
                else:
                    la=' '
                plt.bar(x,y,label=la)
                plt.legend()
                
            plt.title(input("enter title for bar graph"))
            plt.xlabel(input("enter label for x axis"))
            plt.ylabel(input("enter label for y axis"))
            plt.show()
        elif d==3:
            item=[]
            color=[]
            number=eval(input("enter list of percentages"))
            
            for i in range(1,len(number)+1):
                l=input("enter name for label number" + str(i)).strip()
                item.append(l)
            
            for i in range(1,len(number)+1):
                c=input("enter colour for label number" + str(i)).strip()
                color.append(c)
            
            plt.pie(number,labels=item,colors=color,startangle=90,autopct='%1.2f%%',shadow=True)
            plt.legend()
            plt.title(input("enter title"))
            plt.show()
        elif d==4:
            x=eval(input("enter x axis values"))
            y=eval(input("enter corresponding y axis values"))
            x1=pd.DataFrame(x)
            f=pd.DataFrame(y,x)
            plt.title(input("enter title for scatter graph"))
            plt.xlabel(input("enter label for x axis"))
            plt.ylabel(input("enter label for y axis"))
            plt.scatter(x,y)
            reg=linear_model.LinearRegression()
            reg.fit(x1,y)
            bf=input("Do you want line of best fit?").lower()
            bof=bf.strip()
            if bof=='yes':
                bestfit= reg.predict(x1)
                plt.plot(x,bestfit)
            plt.show()
            pre=input("Do you want to predict any x value?").lower()
            predict=pre.strip()
            if predict=='yes':
                p=reg.predict([[float(input('enter the value for which you need prediction'))]])
                print('corresponding value of y= ',p[0])
            
            
            fileexcel=pd.ExcelWriter("test.xlsx")
            f.to_excel(fileexcel,sheet_name="Sheet 1")
            fileexcel.save()

    if t==2:
        ty = input("is it a csv file or excel file").split()
        type=ty[0].lower()
        if type == 'csv' or type == 'csvfile':
            f = input("enter your file name").strip()
            rf = pd.read_csv(f)
        elif type == 'excel' or type == 'excelfile':
            f = input("enter your file name").strip()
            rf = pd.read_excel(f)
        
        print("\n Graph you need \n 1 for Line Graph \n 2 for Bar Chart \n 3 for Pie Chart \n 4 for Scatter Graph")
        d = int(input())
        STY=input("enter style (bmh or classic or dark_background)").lower()
        style.use(STY.split()) 
        
        if d==1:
            n=int(input("enter number of lines"))
            
            for i in range(1,n+1):
                x1=input("name of column containing values of x axis").strip()
                y1=input("name of column containing values of y axis").strip()
                x= rf[x1]
                y =rf[y1]
                l=input("do you want to add legend for this line").lower()
                le=l.split()
                if le[0]=='yes':
                    la=input("enter name for the legend of this line")
                else:
                    la=' '
                plt.plot(x,y,label=la)
                plt.legend()
            
            plt.title(input("enter title for line graph"))
            plt.xlabel(input("enter label for x axis"))
            plt.ylabel(input("enter label for y axis"))
            plt.show()
            reg = linear_model.LinearRegression()
            reg.fit(rf[[x1]],y)
            if predict=='yes':
                p=reg.predict([[float(input('enter the value for which you need prediction'))]])
                print('corresponding value of y= ',p[0])
        elif d==2:
            n=int(input("enter number of bar charts required"))
            
            for i in range(1,n+1):
                x1=input("name of column containing values of x axis").strip()
                y1=input("name of column containing values of y axis").strip()
                x= rf[x1]
                y =rf[y1]
                l=input("do you want to add legend for this line").lower()
                le=l.split()
                if le[0]=='yes':
                    la=input("enter name for the legend of this line")
                else:
                    la=' '
                plt.bar(x,y,label=la)
                plt.legend()
            plt.title(input("enter title for bar graph"))
            plt.xlabel(input("enter label for x axis"))
            plt.ylabel(input("enter label for y axis"))
            plt.show()
        elif d==3:
            color=[]
            x1=input("name of column containing percentages").strip()
            y1=input("name of column name of label").strip()
            x= rf[x1]
            y =rf[y1]
            
            for i in range(1,len(y1)+1):
                c=input("enter colour for label number" + str(i)).strip()
                color.append(c)
            
            plt.pie(x,labels=y,colors=color,startangle=90,autopct='%1.2f%%',shadow=True)
            plt.legend()
            plt.title(input("enter title"))
            plt.show()
        elif d==4:
            x1=input("name of column containing values of x axis").strip()
            y1=input("name of column containing values of y axis").strip()
            x= rf[x1]
            y =rf[y1]
            plt.title(input("enter title for scatter graph"))
            plt.xlabel(input("enter label for x axis"))
            plt.ylabel(input("enter label for y axis"))
            reg = linear_model.LinearRegression()
            reg.fit(rf[[x1]],y)
            plt.scatter(x,y)
            bf=input("Do you want line of best fit?").lower()
            bof=bf.strip()
            if bof=='yes':
                bestfit= reg.predict(rf[[x1]])
                plt.plot(x,bestfit)
            plt.show()
            if predict=='yes':
                p=reg.predict([[float(input('enter the value for which you need prediction'))]])
                print('corresponding value of y= ',p[0])
    
    if t == 3 :
        print("\n So that now you have choosen to make graph from a text file we would like to tell you a rule about it \n the x and y coordianates needs to be seperated either by , or : or any other marking")
        print("for eg: 1,2 \n        3,4 \n you need to enter the marking when promped")
        
        tf = input("enter your file name").strip()
        m = input("enter the seperation marking eg:,").strip()
        x1,y1 = np.loadtxt(tf,unpack=True,delimiter=m)
        
        print("\n Graph you need \n 1 for Line Graph \n 2 for Bar Chart \n 3 for Pie Chart \n 4 for Scatter Graph")
        d = int(input())
        STY=input("enter style (bmh or classic or dark_background)").lower()
        style.use(STY.split()) 

        if d == 1:
            x=[]
            y=[]
            s=int(input('row number from which the machine should start taking the values'))
            e=int(input('row number from which the machine should stop taking the values'))
            for i in range(s-1,e):
                x.append(x1[i])
                y.append(y1[i])
            
            l=input("do you want to add legend for this line").lower()
            le=l.split()
            if le[0]=='yes':
                la=input("enter name for the legend of this line")
            else:
                 la=' '
            plt.plot(x,y,label=la)
            plt.legend()
            plt.title(input("enter title for line graph"))
            plt.xlabel(input("enter label for x axis"))
            plt.ylabel(input("enter label for y axis"))
            plt.show()
            
        elif d==2:
            x=[]
            y=[]
            s=int(input('row number from which the machine should start taking the values'))
            e=int(input('row number from which the machine should stop taking the values'))
            for i in range(s-1,e):
                x.append(x1[i])
                y.append(y1[i])
            l=input("do you want to add legend for this line").lower()
            le=l.split()
            if le[0]=='yes':
                la=input("enter name for the legend of this line")
            else:
                la=' '
            plt.bar(x,y,label=la)
            plt.legend()
            plt.title(input("enter title for bar graph"))
            plt.xlabel(input("enter label for x axis"))
            plt.ylabel(input("enter label for y axis"))
            plt.show()
        elif d==3: 
            x=[]
            y=[]
            s=int(input('row number from which the machine should start taking the values'))
            e=int(input('row number from which the machine should stop taking the values'))
            for i in range(s-1,e):
                x.append(x1[i])
                y.append(y1[i])
            for i in range(1,len(y)+1):
                c=input("enter colour for label number" + str(i)).strip()
                color.append(c)
            
            plt.pie(x,labels=y,colors=color,startangle=90,autopct='%1.2f%%',shadow=True)
            plt.legend()
            plt.title(input("enter title"))
            plt.show()
        elif d==4:
            x=[]
            y=[]
            s=int(input('row number from which the machine should start taking the values'))
            e=int(input('row number from which the machine should stop taking the values'))
            for i in range(s-1,e):
                x.append(x1[i])
                y.append(y1[i])
            x1=pd.DataFrame(x)
            plt.title(input("enter title for scatter graph"))
            plt.xlabel(input("enter label for x axis"))
            plt.ylabel(input("enter label for y axis"))
            plt.scatter(x,y)
            reg=linear_model.LinearRegression()
            reg.fit(x1,y)
            bf=input("Do you want line of best fit?").lower()
            bof=bf.strip()
            if bof=='yes':
                bestfit= reg.predict(rf[[x1]])
                plt.plot(x,bestfit)
            plt.show()
            if predict=='yes':
                p=reg.predict([[float(input('enter the value for which you need prediction'))]])
                print('corresponding value of y= ',p[0])
            
        
    con=(input("do yo wanna continue").upper())
    ucon=con.split()
    if ucon[0] =='NO' :
        print("Thankyou" , emojize(":thumbs_up:"))
        break
    elif ucon[0] =='YES':
        print("Here we go again!! \U0001f600")
        continue
    else:
        break


