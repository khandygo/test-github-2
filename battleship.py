def drawbattlefield(field_):
    str=''
    for st in field_:
        for i in st:
            if i==0:
                str+=' '
            elif i==1:
                str+='*'
            else: str+='$'
        print (str)
        str=''

def validate_battlefield(field):
    ship4=0
    ship3=0
    ship2=0
    ship1=0
    res=True
    tmpfield = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
    tmpfield1=[]
    tmpfield1.append([0,0,0,0,0,0,0,0,0,0,0,0])        
    for ln in field:
        ln.append(0)
        ln.insert(0,0)
        tmpfield1.append(ln)
    tmpfield1.append([0,0,0,0,0,0,0,0,0,0,0,0])        

    for i in range(1,11):
        for j in range(1,11):
            count=0
            if tmpfield[i][j]!=-1:
                tmpfield[i][j]=-1
                if tmpfield1[i][j]==1:
                    if (tmpfield1[i+1][j+1])or(tmpfield1[i+1][j-1])==1:
                        print('!!!')
                        res=False
                        break
                    elif (tmpfield1[i][j+1]==0)and(tmpfield1[i+1][j]==0):
                        #tmpfield[i][j+1]=-1
                        #tmpfield[i+1][j]=-1
                        ship1+=1
                    elif (tmpfield1[i][j+1]==1)and(tmpfield1[i+1][j]==1):
                        #tmpfield[i][j+1]=-1
                        #tmpfield[i+1][j]=-1
                        res=False
                        break
                    elif (tmpfield1[i][j+1]==1):
                        tmpfield1[i][j+1]=-1
                        count=2
                        while True:
                            if (tmpfield1[i][j+count]==1):
                                tmpfield[i][j+count]=-1
                                count+=1
                            else:
                                break
                        if (tmpfield1[i+1][j+count-1]==1)or(tmpfield1[i+1][j+count-2]==1)or(tmpfield1[i+1][j+count]==1):
                            res=False
                            break
                    elif (tmpfield1[i+1][j]==1):
                        tmpfield[i+1][j]=-1
                        count=2
                        while True:
                            if (tmpfield1[i+count][j]==1):
                                tmpfield[i+count][j]=-1
                                count+=1
                            else:
                                break
                        if (tmpfield1[i+count-1][j-1]==1)or(tmpfield1[i+count][j-1]==1)or(tmpfield1[i+count-1][j+1]==1)or(tmpfield1[i+count][j+1]==1):
                            res=False
                            break
                if count==2:
                    ship2+=1
                elif count==3:
                    ship3+=1
                elif count==4:
                    ship4+=1
                if res==False:
                    break
    if (res==True)and(ship1==4)and(ship2==3)and(ship3==2)and(ship4==1):
        res=True
    else:
        res=False
    return res


#        print(ship1)
#        print(ship2)
#        print(ship3)
#        print(ship4)
#    print(ship1)
#    print(ship2)
#    print(ship3)
#    print(ship4)
    


#battleField = [[0, 1, 0, 1, 0, 1, 0, 0, 0, 0],
 #              [0, 1, 0, 1, 0, 1, 0, 0, 0, 0],
  #             [0, 1, 0, 0, 0, 0, 0, 1, 0, 0],
   #            [0, 0, 1, 0, 0, 1, 0, 1, 0, 0],
    #           [0, 0, 1, 0, 0, 0, 0, 1, 0, 0],
     #          [0, 0, 1, 0, 0, 0, 0, 1, 0, 0],
      #         [0, 0, 0, 0, 0, 0, 1, 0, 1, 0],
       #        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        #       [1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         #      [0, 0, 0, 0, 0, 0, 1, 1, 0, 0]]
battleField = [[1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 1, 1, 1, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 1, 0, 0, 0, 0, 0, 1, 0, 0],
                 [0, 1, 0, 0, 0, 1, 0, 1, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
                 [0, 0, 1, 0, 0, 0, 0, 1, 0, 0],
                 [1, 0, 1, 0, 1, 1, 0, 0, 0, 0],
                 [0, 0, 1, 0, 0, 0, 0, 0, 0, 1],
                 [0, 0, 0, 0, 0, 0, 1, 0, 0, 1]]
drawbattlefield(battleField)
print(validate_battlefield(battleField))

