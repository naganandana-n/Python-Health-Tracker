
''' CS PROJECT - NAGANANDANA NAGENDRA AND JASH VERAGIWALA'''

''' PYTHON HEALTH TRACKER'''

import time
import colorama
from colorama import Fore, Back, Style
colorama.init(autoreset=True)
import sys


def dprint(s):
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.10)

print(Fore.GREEN + "---------------------------------------------------------------------------------------------")

img = [
"       ,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,",
"       ,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,",
"       ,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,&&&&&&&&&,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,",
"       ,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,&&&&&&&&&&&&&&&&&&&,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,",
"       ,,,,,,,,,,,,,,,,,,,,,,,,,,,,,&&&&&&&&&&&&&&&&&&&&&#,,,,,,,,,,,,,,,,,,,,,,,,,,,,,",
"       ,,,,,,,,,,,,,,,,,,,,,,,,,,,,&&&&&&&&&&&&&&&&&&&&&&&,,,,,,,,,,,,,,,,,,,,,,,,,,,,,",
"       ,,,,,,,,,,,,,,,,,,,,,,,,,,,,&&&&#################&&&,,,,,,,,,,,,,,,,,,,,,,,,,,,,",
"       ,,,,,,,,,,,,,,,,,,,,,,,,,,,,(&&##################&&&,,,,,,,,,,,,,,,,,,,,,,,,,,,,",
"       ,,,,,,,,,,,,,,,,,,,,,,,,,,,,,&&##################&&,,,,,,,,,,,,,,,,,,,,,,,,,,,,,",
"       ,,,,,,,,,,,,,,,,,,,,,,,,,,,,##&###################%#,,,,,,,,,,,,,,,,,,,,,,,,,,,,",
"       ,,,,,,,,,,,,,,,,,,,,,,,,,,,,####                 ###,,,,,,,,,,,,,,,,,,,,,,,,,,,,",
"       ,,,,,,,,,,,,,,,,,,,,,,,,,,,,,###   ALWAYS WEAR  ###,,,,,,,,,,,,,,,,,,,,,,,,,,,,,",
"       ,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,##    A MASK     #,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,",
"       ,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,                ,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,",
"       ,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,#            .,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,",
"       ,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,  ####      ####  ,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,",
"       ,,,,,,,,,,,,,,,,,,,,,,,,,,,,,   *##############       ,,,,,,,,,,,,,,,,,,,,,,,,,,",
"       ,,,,,,,,,,,,,,,,,,,.        ,    #############     ,          ,,,,,,,,,,,,,,,,,,",
"       ,,,,,,,,,,,,,,              .    /###########.     ,              .,,,,,,,,,,,,,",
"       ,,,,,,,,,,,,                ,    ////////////      ,,               ,,,,,,,,,,,,",
"       ,,,,,,,,,,,               ,      ///////////       ,,                ,,,,,,,,,,,",
"       ,,,,,,,,,,,                ,     *//////////      .,                 ,,,,,,,,,,,",
"                                                                                       ",
]
j = [
"               _    _            _ _   _       _______             _                   ",
"              | |  | |          | | | | |     |__   __|           | |                  ",
"              | |__| | ___  __ _| | |_| |__      | |_ __ __ _  ___| | _____ _ __       ",
"              |  __  |/ _ \/ _` | | __| '_ \     | | '__/ _` |/ __| |/ / _ \ '__|      ",
"              | |  | |  __/ (_| | | |_| | | |    | | | | (_| | (__|   <  __/ |         ",
"              |_|  |_|\___|\__,_|_|\__|_| |_|    |_|_|  \__,_|\___|_|\_\___|_|         ",
"                                                                                       ",
]
     
                                                                        
for i in img:
    n = i
    time.sleep(0.5)
    print(Fore.GREEN + n)
print(Style.RESET_ALL)

for i in j:
    n = i
    time.sleep(0.5)
    print(Fore.WHITE + n)
print(Style.RESET_ALL)

print(Fore.GREEN + "---------------------------------------------------------------------------------------------")
dprint("  WELCOME TO THE HEALTH TRACKER APP.")
print()
dprint('''  TO GET STARTED, ENTER YOUR DETAILS BELOW.
  MAKE SURE TO ENTER THE DETAILS EXACTLY AS GIVEN IN YOUR PASSPORT.''')
print()
print(Fore.GREEN + "---------------------------------------------------------------------------------------------")


all_name=[]
all_age=[]
all_gender=[]
all_place=[] 
all_disability=[]
all_country=[]


def name():
    global name_user
    name_user=input("  ENTER YOUR NAME: ")


def name_check():
    f = open(name_user+".txt","a")
    fh = open(name_user+".txt","r")
    line = fh.read()
    if len(line)>0:
        print(" ")
        dprint('''  WE HAVE NOTICED THAT YOU HAVE USED THE PROGRAM BEFORE.
  ARE THESE YOUR DETAILS? ''')
        print()
        ch = open(name_user+".txt", "r")
        y = ch.readlines()
        for i in y:
            if "NAME: " in i:
                print(" ")
                n = i[6:-1]
                print("    NAME     |", n)
                time.sleep(0.5)
            if "AGE: " in i:
                n = i[5:-1]
                print("    AGE      |", n)
                time.sleep(0.5)
            if "GENDER: " in i:
                n = i[8:-1]
                if n.lower() == "m":
                    print("    GENDER   | Male")
                    time.sleep(0.5)
                else:
                    print("    GENDER   | Female")
                    time.sleep(0.5)
            if "ADDRESS: " in i:
                n = i[9:-1]
                print("    ADDRESS  |", n)
                time.sleep(0.5)
            if "COUNTRY: " in i:
                n = i[9:-1]
                print("    COUNTRY  |", n)
                print(" ")
        dprint("  IF YES, ENTER 'Y', ELSE ENTER 'N': ")
        s = input()
        if s.lower() == "y":
            global a
            a = 0
            hh = open(name_user+".txt", "r")
            l = hh.readlines()
            for i in l:
                if "AGE: " in i:
                    global age_user
                    age_user = i[5:-1]
                if "GENDER: " in i:
                    if i[8:-1] == "m":
                        global gender_user
                        gender_user = "m"
                    else:
                        gender_user = "f"
                if "ADDRESS: " in i:
                    global place_user
                    place_user = i[9:-1]
                if "COUNTRY: " in i:
                    global country_user
                    country_user = i[9:-1]
            hh.close()
            ch.close()
        else:
            a = 1
            pass
    else:
        f.close()
        fh.close()
        a = 1
        pass


def age():
    global age_user
    age_user=int(input("  ENTER YOUR AGE: "))
    if age_user <110 or age_user>0:
        pass
    else:
        age()
    
    
def gender():
    global gender_user
    gender_user = input("  ENTER YOUR GENDER, M FOR MALE, F FOR FEMALE: ")
    if gender_user.lower() == "m" or gender_user == "f":
        pass
    else:
        print("  PLEASE ENTER YOUR GENDER CORRECTLY.")
        gender()


def place():
    global place_user
    place_user=input("  ENTER YOUR CURRENT ADDRESS: ")


def country():
    global country_user 
    country_user=input("  ENTER THE COUNTRY YOU LIVE IN: ")
    
    
def date():
    dprint("  ENTER TODAY'S DATE [FORMAT: YYYY-MM-DD]: ")
    dat=input()
    if dat[4]!= "-" and dat[7]!="-" and len(dat)!=10:
        print("  YOU ARE USING THE WRONG FORMAT. TRY AGAIN [FORMAT: YYYY-MM-DD].")
        date()
    else:
        return dat
    
    
def hospital():
    import selenium
    from selenium import webdriver     
    dprint("  YOUR CURRENT ADDRESS IS SAVED AS: " + place_user)
    print()
    dprint('''  DO YOU WANT TO FIND HOSPITALS NEAR A DIFFERENT LOCATION OR THE ONE GIVEN ABOVE?
  TO ENTER A DIFFERENT LOCATION, ENTER 'Y' ELSE ENTER 'N': ''')
    hos = input()
    if hos.lower() == 'y':
        hospital = input("  ENTER YOUR DESIRED LOCATION: ")
    else:
        hospital = place_user 
    print(" ")
    print(Fore.RED + "  YOU WILL BE REDIRECTED TO A WEBSITE.")
    print(Fore.RED + "  DO NOT CLICK ANYTHING ON THE POP-UP UNTIL THE DESIRED INFORMATION HAS APPEARED.")
    print(" ")
    time.sleep(5)
    chrome = webdriver.Chrome("C:\\Users\\nagan\\Desktop\\Coding Files\\chromedriver\\chromedriver")  # change this if needed
    chrome.get("https://www.google.co.in/")
    time.sleep(2)
    bar = chrome.find_element_by_xpath('//input[@type="text"]')
    time.sleep(1)
    bar.send_keys("Hospitals near ", hospital)
    bar.submit()


name()
name_check()
    
if a == 1:
    print("")
    age()
    print("")
    gender()
    print("")
    place()
    print("")
    country()
    all_name.append(name_user)                                          
    all_age.append(age_user)
    all_gender.append(gender_user)
    all_place.append(place_user)
    all_country.append(country_user)
    fileopen=open(name_user+".txt","w")
    age=str(age_user)
    fileopen.writelines(["NAME: "+name_user+"\n"]) 
    fileopen.writelines(["AGE: "+age+"\n"])
    fileopen.writelines(["GENDER: "+gender_user+"\n"])
    fileopen.writelines(["ADDRESS: "+place_user+"\n"])
    fileopen.writelines(["COUNTRY: "+country_user+"\n"])
    fh=open(name_user+".csv","a")
    fh.writelines(["date\t","temperature","\n"])
    fh.close()
    fileopen.close()

if gender_user.lower() == "m":
    v = "Male"
else:
    v = "Female"    
print(Fore.GREEN + "---------------------------------------------------------------------------------------------")  
dprint("  THANK YOU FOR FILLING UP YOUR DETAILS")
print()
dprint("  TO CONFIRM, YOUR DETAILS ARE AS FOLLOWS:")
print()
print(" ")
print("    NAME     |", name_user)
time.sleep(0.5)
print("    AGE      |", age_user)
time.sleep(0.5)
print("    GENDER   |", v)
time.sleep(0.5)
print("    ADDRESS  |", place_user)
time.sleep(0.5)
print("    COUNTRY  |", country_user)
print(" ")
dprint("  IF YOUR DETAILS ARE CORRECT ENTER 'Y', ELSE 'N': ")
ans = input()
if ans.lower() == "y":
    pass
else:
    main_function()
    
x=0
while x==0:
    print(Fore.GREEN + "---------------------------------------------------------------------------------------------")
    print("    _________________________________________________________________________________")
    time.sleep(0.5)
    print("    |  SERIAL NO.  |  TASK                                                          |")
    time.sleep(0.5)
    print("    |              |                                                                |")
    time.sleep(0.5)
    print("    |      1       |  TO ENTER YOUR BODY TEMPERATURE DAILY.                         |")
    time.sleep(0.5)
    print("    |              |                                                                |")
    time.sleep(0.5)
    print("    |      2       |  TO CHECK THE SITUATION OF COVID-19 IN YOUR COUNTRY.           |")
    time.sleep(0.5)
    print("    |              |                                                                |")
    time.sleep(0.5)
    print("    |      3       |  TO SEE GRAPHICAL ANALYSIS OF YOUR TEMPERATURE.                |")
    time.sleep(0.5)
    print("    |              |                                                                |")
    time.sleep(0.5)
    print("    |      4       |  TO SEE PRECAUTIONS THAT YOU CAN TAKE TO KEEP YOURSELF SAFE    |")
    time.sleep(0.5)
    print("    |              |                                                                |")
    time.sleep(0.5)
    print("    |      5       |  TO GET CONTACT DETAILS OF HOSPITALS NEAR YOU                  |")
    time.sleep(0.5)
    print("    |              |                                                                |")
    time.sleep(0.5)
    print("    |      6       |  TO EXIT THE PROGRAM                                           |")
    time.sleep(0.5)
    print("    _________________________________________________________________________________")
    print(" ")
    dprint('''  FOLLOWING ARE THE TASKS THIS PROGRAM PERFORMS.
  TO SELECT A TASK, ENTER THE SERIAL NO. OF THE TASK: ''')
    b = int(input())
    print(Fore.GREEN + "---------------------------------------------------------------------------------------------")    
    if b==1:
        z=1
        while z==1:
            fh=open(name_user+".csv","a")
            d= date()
            dprint("  ENTER YOUR TEMPERATURE IN CELSIUS [°C]: ")
            temp = input()
            float_temp=float(temp)
            if float_temp > 37:
                import colorama
                from colorama import Fore, Back, Style
                colorama.init(autoreset=True)
                import mysql.connector as sqltor
                mycon=sqltor.connect(host="localhost",user="root",password="12345678",database="project") # change this if needed
                cursor=mycon.cursor()
                st="insert into tempdet values('{}',{})".format(d,temp)
                cursor.execute(st)
                mycon.commit()
                fh.writelines([d,"\t",temp,"\n"])
                print(" ")
                dprint("  ATTENTION!")
                print()
                print(" ")
                print(Fore.RED + "  YOU HAVE A FEVER.")
                print(Fore.RED + "  THIS IS A SYMPTOM SHOWN BY COVID-19 PATIENTS.")
                print(Fore.RED + "  PLEASE VISIT A DOCTOR IMMEDIATELY.")
                print(" ")
                dprint("  THE DETAILS OF THE NEAREST HOSPITAL AND DIRECTIONS TO IT WILL BE SHOWN TO YOUR SHORTLY.")
                print()
                hospital()
                z=0
            else:
                import mysql.connector as sqltor
                mycon=sqltor.connect(host="localhost",user="root",password="12345678",database="project") # change this if needed
                cursor=mycon.cursor()
                st="insert into tempdet values('{}',{})".format(d,temp)
                cursor.execute(st)
                mycon.commit()
                fh.writelines([d,"\t",temp,"\n"])
                dprint('''  WOULD YOU LIKE TO ENTER TEMPERATURES FOR A DIFFERENT DAY?
  IF YES, ENTER 'Y' ELSE ENTER 'N': ''')
                h = input()
                if h.lower() == "y":
                    z=1
                else:
                    z=0
                        

            mycon.close()
        fh.close()
        x=0
        
        
    if b==3:
        import numpy as np
        import matplotlib.pylab as plot
        import datetime 
        all_dates=[]
        all_temps=[]
        import mysql.connector as sqltor
        mycon=sqltor.connect(host="localhost",user="root",password="12345678",database="project") # change this if needed
        cursor=mycon.cursor()
        cursor.execute("select * from tempdet")
        data=cursor.fetchall()
        for i in data:
            all_temps+=[i[0]]
            all_dates+=[i[1]]
        mycon.close()
        plot.xlabel(' date')
        plot.ylabel(' Temperature')
        plot.plot(all_temps,all_dates)
        dprint('''  YOUR TEMPERATURES WILL BE AVAILABLE IN THE FORM OF A GRAPH.
  YOU CAN DOWNLOAD THE GRAPH IF NEEDED.''')
        print()
        time.sleep(5)
        plot.show()
        x=0
        
        
    if b==5:
        hospital()
        x=0
        
        
    if b==4:
        fh=open("precautions.txt","r")
        Str=fh.readlines()
        for i in Str:
            print(i,end=" ")
        print()
        time.sleep(10)
        fh.close()
        x=0
        
        
    if b==2:
        from selenium import webdriver
        import datetime
        import time
        import colorama
        from colorama import Fore, Back, Style
        colorama.init(autoreset=True)
        now = datetime.datetime.now()
        
        dprint("  YOUR COUNTRY IS SAVED AS: " + country_user)
        print()
        dprint('''  DO YOU WANT TO KNOW THE COVID-19 STATISTICS IN YOUR COUNTRY
  OR IN A DIFFERENT COUNTRY?
  TO ENTER A DIFFERENT COUNTRY, ENTER 'Y' ELSE ENTER 'N': ''')
        hos = input()
        if hos.lower() == 'y':
            country = input("  ENTER YOUR DESIRED COUNTRY: ")
        else:
            country = country_user
        print(" ")
        print(Fore.RED + "  YOU WILL BE REDIRECTED TO A WEBSITE, KINDLY CLICK BACK ONTO THE PROGRAM.")
        print(Fore.RED + "  DO NOT CLOSE THE POP-UP. KINDLY 'MINIMIZE' THE POP-UP OPENED.")
        print(" ")
        time.sleep(5)
        dprint("  PLEASE WAIT FOR A FEW SECONDS AS WE GET YOU THE LATEST STATISTICS.")
        print()
        
        
        chrome = webdriver.Chrome("C:\\Users\\nagan\\Desktop\\Coding Files\\chromedriver\\chromedriver") # change this if needed
        
        chrome.get("https://www.worldometers.info/coronavirus/")
        time.sleep(5)
        chrome.execute_script("window.scrollTo(0, document.body.scrollHeight/9);")
        time.sleep(5)
        search = chrome.find_element_by_xpath('//input[@type="search"]')
        search.click()
        search.send_keys(country)
        
        country_name = chrome.find_element_by_css_selector('a.mt_a')
        total_cases = chrome.find_element_by_xpath('//td[3]')
        new_cases = chrome.find_element_by_xpath('//td[4]')
        total_deaths = chrome.find_element_by_xpath('//td[5]')
        new_deaths = chrome.find_element_by_xpath('//td[6]')
        total_recovered = chrome.find_element_by_xpath('//td[7]')
        active_cases = chrome.find_element_by_xpath('//td[8]')
        critical_cases = chrome.find_element_by_xpath('//td[9]')
        
        print(" ")
        print("    _______________________________ ")
        print("    | Country Name                |", country_name.text)
        print("    |                             |")
        print("    | Total cases                 |", total_cases.text)
        print("    |                             |")
        print("    | New Cases in last 24 hours  |", new_cases.text)
        print("    |                             |")
        print("    | Total Deaths                |", total_deaths.text)
        print("    |                             |")
        print("    | New Deaths in last 24 hours |", new_deaths.text)
        print("    |                             |")
        print("    | Total Recovered             |", total_recovered.text)
        print("    |                             |")
        print("    | Active Cases                |", active_cases.text)
        print("    |                             |")
        print("    | Critical Cases              |", critical_cases.text)
        print("    _______________________________ ")
        time.sleep(10)
        chrome.close()
        x=0
        
        
    if b==6:
        dprint('''  THANK YOU FOR USING OUR PROGRAM.
  YOUR HEALTH IS OUR NUMBER ONE PRIORITY.
  STAY SAFE, HEALTHY, AND ALWAYS WEAR A MASK.''')
        x=1



