#!/usr/bin/env python3

import re
def getValidStr(reqMsg, validArgs):
    valid = False
    while not valid:
        rtnStr = input(reqMsg).upper()
        if(rtnStr in validArgs):
            valid = True
        else:
            print("Sorry the string only allows values of: ", validArgs)
    return rtnStr

def getEmail(message):
    

    validEmail= False
    while validEmail==False:
        email=input("what is your Email?:").upper()
        email2=input("Please confirm your Email?:").upper()
        pattern= re.compile(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)")
        if ((email== email2) and re.search(pattern,email)):
            validEmail=True
    
    return email



def calculateFee(skill):
    skills={"E":35,"C":20}
    baseRate=10
    rate=baseRate +skills.get(skill)
    return rate

def calcExchage(countryCode,amount):
    rates={"US":{"USD":1.5},"AU":{"AUD": 2.0},"UK":{"GBP":1.0}}
    rates=rates.get(countryCode)
    rate=0
    code=""
    for key in rates:
        code=key
        rate=rates[key]
    amount= amount* rate
    return str(amount)+" "+ code
    
def Main():
    print("welcome to FEE CALCULATOR")
    more= True
    while more:
        
        email=getEmail("What is your email?: ")
        skill=getValidStr("what is your skill? C for casual, E for expert!",["C","E"])
        fee= calculateFee(skill)
        country = getValidStr("What is your country? UK,AU, or US",["UK","AU","US"])
        localFee = calcExchage(country,fee)
        print("Player with email: " + email + " has fee of " + localFee )
        value=getValidStr("Do you wish to calculate another Fee?: Y or N",["Y","N"])
        if (value=="N"):
            more=False
        
