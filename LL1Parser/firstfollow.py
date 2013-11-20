firstset={}
followset={}
parsingtable={}

class FirstFollow:
    def __init__(self,gram,ter,nonter,start):#need to pass the grammar here..
        self.gram=gram
        self.term=ter
        self.nonterm=nonter
        self.start=start
        
        ''' def findset(self):
        for i in self.nonterm:
            self.firstfind(i)
            #self.follow(i)
        for i in self.term:
            print(firstset[i])
    
    def firstfind(self,ip):
        self.first(ip)'''    
    def first(self,ip):#ip is a string; first() returns first setnn
        #print('in First')
        #length=len(ip)
        fir=[]
        ctr=0
        length=0
        if(ip in self.term):
            fir.extend(ip)
        else:
            for i in self.gram[ip]:
                # print('1')
                #print(i[0],":",i,"::")
                if(i[0] in self.term):
                    #print('2')
                    #print(i[0])
                    #print(ctr)
                    fir.extend(i[0])
                else:
                    #print('3')
                    length=len(i)
                    while(ctr<length):
                        #print('4')
                        if('n' in self.gram[i[ctr]]):   # 'n' is for null symbol
                                #print('5')
                                #print(ctr)
                                fir.extend(self.first(i[ctr]))
                                #print(fir)
                                ctr+=1
                                #print(ctr)
                        else:
                                #print('6')
                                
                                fir.extend(self.first(i[ctr]))
                                #print(fir)
                                #print(ctr)
                                break
        firstset[ip]=fir
        return fir

    def follow(self,ip):
        foll=[]
        if(ip==self.start):
            foll.extend('$')
        for key in self.gram.keys():#iterating thorugh the keys of the grammar
            vals=self.gram[key]
            #print('1')
            #print('key',key)
            #print('vals',vals)
            for each in vals:
                #print('2')
                #print('each',each)
                ctr=0
                length=len(each)
                #print('len',length)
                for j in each:
                    #print('3')
                    #print('j',j)
                    if(j==ip):
                        #print('4')
                        if(ctr<length-1):
                            #print('5')
                            if((ip != key)and('n'in self.first(each[ctr+1]))):
                                #print('6')
                                for x in self.first(each[ctr+1]):
                                    if((x not in foll)and(x!='n')):
                                        foll.extend(x)
                                for x in self.follow(key):
                                    if((x not in foll)and(x!='n')):
                                        foll.extend(x)
                                #print('foll',foll)
                            else:
                                #print('7')
                                for x in self.first(each[ctr+1]):
                                    if((x not in foll)and(x!='n')):
                                        foll.extend(x)
                                #print('foll',foll)
                        if((ip != key)and(ctr==length-1)):
                            #print('8')
                            for x in self.follow(key):
                                if((x not in foll)and(x!='n')):
                                    foll.extend(x)
                            #print('foll',foll)
                    ctr+=1
                ctr=0
        followset[ip]=foll
        return foll
      
    def parsingtable(self,ip):
        #print(self.gram)
        
        for i in self.gram[ip]:
            #print("+++",i)
            #print(i[0],":",i,"::",ip)   
            if ip not in parsingtable: 
                parsingtable[ip]={}
                #for j in firstset[ip]:
                    #if j not in parsingtable[ip]: 
                        #parsingtable[ip][j]=[]
                #print("pppp",i,type(i))
            #print(i[0],":",i,"::######",ip)
                
            if i[0] in self.term and i[0]!='n':
                
                if i[0] not in parsingtable[ip]:
                    parsingtable[ip][i[0]]=[]
                parsingtable[ip][i[0]].append(str(ip +" -> "+ i))
            elif i == 'n':
                
                for k in followset[ip]:
                    if k not in parsingtable[ip]: 
                        parsingtable[ip][k]=[]
                    parsingtable[ip][k].append(str(ip +" -> "+ i))
            else:
                
                for k in firstset[ip]:
                    if k not in parsingtable[ip]: 
                        parsingtable[ip][k]=[]
                    parsingtable[ip][k].append(str(ip + " -> "+i))
        
        for i in self.term :
            
            if i not in parsingtable[ip] and i!="n":
                parsingtable[ip][i]=[]
                parsingtable[ip][i].append("Error")
            
            
                
    def printparser(self):
        print("---"*40)
        for i in self.nonterm:
            for j in self.term:
                if j!='n':
                    for k in parsingtable[i][j]:
                
                        print("[",i, ",",j, "]",":",k,end=" ")
            print("")
            print("---"*30)
                

                                                                              
                                                    
                        
                        
        
                #(i[0] in self.nonterm):
                #fir.append(self.first(i[0]))
               
            #'''        while(i<length):
        '''if(ip[i] in term):
                fir.append(ip[i])
                i+=1
                elif(ip[i] in nonterm):#must check productions/..
                fir.append(self.first(ip[i]))
                if('n' in gram(ip[i]):
                   i+=1
                else:
                   break
                   
             return fir'''
def createparser(text):
    text = text.split('\n')
    #for t in text:
        #print(text[0])
        #print(type(text[0]))
    #(key,value)=text[0].split[':']
    #print(key,value)
    #grammar=dict(text[0])
    t=text[0]
    t =t.split(",,")
    dict={}
    for i in t:
        print(i[0])
        dict[i[0]]=[i[3:-1]]
        k=i[3:-1].split(",")
        dict[i[0]]=k

    terminals=list(text[1].split(","))
    nonterminals=list(text[2].split(","))
    start=text[3]
    print(terminals,nonterminals,start)
    a=FirstFollow(dict,terminals,nonterminals,start)
    #a.findset()
    nont=nonterminals
    # print('FOLLOW :',"e " ,a.first('E'))
    for i in nont:
        fi=a.first(i)
        fo=a.follow(i)
        #print('FOLLOW :',i," " ,a.first(i))
        #print('FIRST  :',i," ",a.follow(i))
        firstset[i]=fi
        followset[i]=fo
        
    
    print(firstset)
    print(followset)
    for i in nont:
        a.parsingtable(i)
    
    a.printparser()
    return parsingtable
    
    #print(a.first('('))
