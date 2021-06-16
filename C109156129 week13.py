class Univerity:
    def __init__(self,name):
        self.cps=[]
        self.name=name
class Campus:
    def __init__(self,name):
        self.dps=[]
        self.name=name
class Department:
    def __init__(self,name):
        self.name=name

dict1={"建工校區":["機械","電子","電機","化材","土木"],
"燕巢校區":["智慧商務系","金資","會資","財稅","觀光"],
"旗津校區":["航運","輪機","造船及海洋","電訊","海事資訊"],
"第一校區":["運籌","國企","企管","風險","資管","行銷與流通","會資","應日","應外","電腦與通訊","財稅","財稅","電子","金融"],
"楠梓校區":["電機","商資","海洋生物","海洋環境","水產食品","水產養殖","漁業生產與管理","半導體","海洋休閒","航管"],
}
#dict={a,b}
NKUST=Univerity("國立高雄科技大學")

for a,b in dict1.items():
    NKUST.cps.append(Campus(a))
    l=len(NKUST.cps)
    for i in b:
        NKUST.cps[l-1].dps.append(Department(i))


l=len(NKUST.cps)
for i in range(l):
    print((NKUST.cps[i].name),":")
    if(i==0 or i==1 or i==2):
        for m in range(l):
            print(NKUST.cps[i].dps[m].name)
    elif(i==3):
        for m in range(14):
            print(NKUST.cps[i].dps[m].name)
    elif(i==4):
        for m in range(10):
            print(NKUST.cps[i].dps[m].name)
    
        
    

 