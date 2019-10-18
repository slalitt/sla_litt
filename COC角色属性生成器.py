print('----------这是一个神奇的coc跑团属性随机系统----------\n')
import random
a=random.randint(1,6)
b=random.randint(1,6)
c=random.randint(1,6)
STR = (a+b+c)*5
CON = (a+b+6)*5
SIZ = (a+b+c)*5
DEX = (a+b+c)*5
APP = (a+b+c)*5
INT = (a+b+6)*5
POW = (a+b+c)*5
EDU = (a+b+6)*5
LUC = (a+b+c)*5
SUM = STR+CON+SIZ+DEX+APP+INT+POW+EDU
temp = input('输入0开始roll点：')
num = int(temp)
i = 0
while i < 5:
    a=random.randint(1,6)
    b=random.randint(1,6)
    c= random.randint(1,6)
    STR = (a+b+c)*5
    CON = (a+b+6)*5
    SIZ = (a+b+c)*5
    DEX = (a+b+c)*5
    APP = (a+b+c)*5
    INT = (a+b+6)*5
    POW = (a+b+c)*5
    EDU = (a+b+6)*5
    LUC = (a+b+c)*5
    SUM = STR+CON+SIZ+DEX+APP+INT+POW+EDU
    if 430<=SUM<=575 :
        print('\n力量')
        print(STR)
        print('体质')
        print(CON)
        print('体型')
        print(SIZ)
        print('敏捷')
        print(DEX)
        print('外貌')
        print(APP)
        print('智力')
        print(INT)
        print('意志')
        print(POW)
        print('教育')
        print(EDU)
        print('幸运')
        print(LUC)
        print('总值(不包括幸运)')
        print(SUM)
        i+=1
        if i==5 :
            print('\nroll点回数用尽,请使用第五回roll点的数据。')
            break
            
        temp = input('\n若不满意该属性请继续输入0\n若满意请输入1：')
        num = int(temp)
        if num == 1:
            print('\n该组属性将成为您的初始角色属性。')
            break

        
        
        


    
