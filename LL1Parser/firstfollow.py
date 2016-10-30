firstset={}
followset={}
parsingtable={}

class FirstFollow:
    def __init__(self,gram,ter,nonter,start):#need to pass the grammar here.
        self.gram=gram
        self.term=ter
        self.nonterm=nonter
        self.start=start
    
    def first(self,ip):#ip is a string; first() returns first setnn
        fir=[]
        ctr=0
        length=0
        if(ip in self.term):
            fir.extend(ip)
        else:
            for i in self.gram[ip]:
                if(i[0] in self.term):
                    fir.extend(i[0])
                else:
                    length=len(i)
                    while(ctr<length):
                        if('n' in self.gram[i[ctr]]):   # 'n' is for null symbol
                                fir.extend(self.first(i[ctr]))
                                ctr+=1
                        else:                                
                                fir.extend(self.first(i[ctr]))
                                break
        firstset[ip]=fir
        return fir

    def follow(self,ip):
        foll=[]
        if(ip==self.start):
            foll.extend('$')
        for key in self.gram.keys():#iterating thorugh the keys of the grammar
            vals=self.gram[key]
            for each in vals:
                ctr=0
                length=len(each)
                for j in each:
                    if(j==ip):
                        if(ctr<length-1):
                            if((ip != key)and('n'in self.first(each[ctr+1]))):
                                for x in self.first(each[ctr+1]):
                                    if((x not in foll)and(x!='n')):
                                        foll.extend(x)
                                for x in self.follow(key):
                                    if((x not in foll)and(x!='n')):
                                        foll.extend(x)
                            else:
                                for x in self.first(each[ctr+1]):
                                    if((x not in foll)and(x!='n')):
                                        foll.extend(x)
                        if((ip != key)and(ctr==length-1)):
                            for x in self.follow(key):
                                if((x not in foll)and(x!='n')):
                                    foll.extend(x)
                    ctr+=1
                ctr=0
        followset[ip]=foll
        return foll
      
    def parsingtable(self,ip): #method to build the LL1 parsing table        
        for i in self.gram[ip]:  
            if ip not in parsingtable: 
                parsingtable[ip]={}
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
           
    def printparser(self): #prints the parser output
        print("---"*40)
        for i in self.nonterm:
            for j in self.term:
                if j!='n':
                    for k in parsingtable[i][j]:
                        print("[",i, ",",j, "]",":",k,end=" ")
            print("")
            print("---"*30)
                
def createparser(text):#method to create the parser
    text = text.split('\n')
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
    nont=nonterminals
    for i in nont:
        fi=a.first(i)
        fo=a.follow(i)
        firstset[i]=fi
        followset[i]=fo
        
    print(firstset)
    print(followset)
    for i in nont:
        a.parsingtable(i)
    
    a.printparser()
    return parsingtable