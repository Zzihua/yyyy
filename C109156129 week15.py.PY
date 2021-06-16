import json
import requests
import pymysql

data ={'lang':'tw','type':'2'}
response = requests.get("https://apis.youbike.com.tw/api/front/station/all",data)

#json.loads 把字串或byte轉換成dictionary型別
if response.status_code==200:
    tmp =json.loads(response.content)
    totalvalue=[]
    totalkey=[]
    for i in tmp['retVal']:
        values=[j[1] for j in i.items()]
        keys=[j[0] for j in i.items()]
        totalvalue.append(values)
        totalkey.append(keys)
    
    conn =pymysql.connect(host='140.127.149.199',port=3306,user='ic',passwd='ic',db='ic',charset='utf8') #建立連線
    cursor =conn.cursor(pymysql.cursors.DictCursor)
    for i in range(len(totalvalue)):
        cursor.execute(f"INSERT INTO `c109156129` (`area`, `name`,`address`) VALUES ('{totalvalue[i][1]}', '{totalvalue[i][5]}','{totalvalue[i][7]}');")
    
    cursor.execute("SELECT * FROM `c109156129`;")
    rows =cursor.fetchall()

    data=[]
    for i in range(len(rows)):
        data.append(rows[i])

    # dictionary-->byte,str
    tmp=json.dumps(data,indent=1,ensure_ascii=False)
    print(tmp)

    conn.commit()
    cursor.close()
    conn.close()    

    
        

