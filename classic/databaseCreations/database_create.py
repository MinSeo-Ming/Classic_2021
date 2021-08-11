import csv
import os
from clothes.models import Color,Clothing,Clothes_Main_type,Length
from weather.models import Month, fine_Dust_ppm_2_5,fine_Dust_ppm_10,Weather
from django.contrib.auth.models import User
from django.utils import timezone

current_path = os.path.abspath(__file__)
dir = os.path.dirname(current_path)


def createColor():
    file_path = os.path.join(dir,'clothes_colors.csv')
    with open(file_path,'r',encoding='utf-8-sig',newline='')as f:
        reader = csv.reader(f)
        for row in reader:
            Color.objects.create(
                color = row[0]
            )

def createType():
    file_path = os.path.join(dir,'clothes_type.csv')
    with open(file_path,'r',encoding='utf-8-sig',newline='')as f:
        reader = csv.reader(f)
        for row in reader:
            
            Clothes_Main_type.objects.create(
                type = row[0]
            )


def createLength():
    file_path = os.path.join(dir,'length.csv')
    with open(file_path,'r',encoding='utf-8-sig',newline='')as f:
        reader = csv.reader(f)
        
        for row in reader:
            
            Length.objects.create(
                length = row[0]
            )
    

def createMonth():
    file_path = os.path.join(dir,'month.csv')
    with open(file_path,'r',encoding='utf-8-sig',newline='')as f:
        reader = csv.reader(f)
        
        for row in reader:
            Month.objects.create(
                month = row[0],
                min_temp = float(row[1]),
                max_temp = float(row[2])
            )


def createFineDust_10():
    file_path = os.path.join(dir,'fine_dust_10.csv')
    with open(file_path,'r',encoding='utf-8-sig',newline='')as f:
        reader = csv.reader(f)
        for row in reader:
            
            fine_Dust_ppm_10.objects.create(
                grade = row[0],
                min_ppm =int(row[1]),
                max_ppm =int(row[2])
            )


def createFineDust_2_5():
    file_path = os.path.join(dir,'fine_dust_2_5.csv')
    with open(file_path,'r',encoding='utf-8-sig',newline='')as f:
        reader = csv.reader(f)
        for row in reader:
            
            fine_Dust_ppm_2_5.objects.create(
                grade = row[0],
                min_ppm =int(row[1]),
                max_ppm =int(row[2])
            )

def createClothes():
    file_path = os.path.join(dir,'clothing.csv')
    with open(file_path,'r',encoding='utf-8-sig',newline='')as f:
        reader = csv.reader(f)
        make = User.objects.get(username ='default')
        for row in reader:
            print(row[1])
            t = Clothes_Main_type.objects.get(type=row[1])
            c = Color.objects.get(color =row[2])
            l = Length.objects.get(length = row[5])
            img = "clothing/images/" + row[6]
            print(t)

            Clothing.objects.create(
                author = make,
                type = t,
                color=c,
                alias=row[3],
                create_date=timezone.now(),#이건 timestamp,
                month=int(row[4]),
                length=l,
                image = img
            )



def createWeather():
    i=1
    seasons =['봄','여름','가을','겨울']
    list = Month.objects.all()
    
    for i in range(12):
        if i<=2 or i ==12:
                s=seasons[3]
        elif i<=5:
            s = seasons[0]
        elif i<=8:
            s = seasons[1]
        else:
            s = seasons[2]
        mon = list[i]
        temp=Weather.objects.create(
            season =s,
            month = mon
        )
    

def createDB():
    createType()
    createColor()
    createLength()
    createClothes()

    createMonth()
    createFineDust_10()
    createFineDust_2_5()
    createWeather()