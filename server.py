import socketserver

file = open("data.txt", "r")
dict={}
while True:
    line = file.readline()
    if not line:
        break
    else:
        line = line.rstrip("\n")
        info = line.split("|",line.count("|"))
        recoLen = len(info)
        if recoLen < 4:
            for num in range(recoLen,4):
                info.append('')                  
        name = info[0].strip(' ')
        if name =="":
            continue
        name = name.lower()
        sub = tuple(info)
        tempDict={name:sub}
        dict.update(tempDict)  
file.close()

def checkReq(data):
    req = data.split(";",data.count(";"))
    if req[0].lower()=="find":
        name = req[1]
        msg = findRecord(name)
    elif req[0].lower()=="add":
        name = req[1]
        age=req[2]
        address=req[3]
        phone=req[4]
        msg = addRecord(name, age, address, phone)
    elif req[0].lower()=="delete":
        name = req[1]
        msg = deleteRecord(name)
    elif req[0].lower()=="updateage":
        name = req[1]    
        age=req[2]
        msg = updateAge(name, age)
    elif req[0].lower()=="updateaddress":
        name = req[1]
        address=req[2]
        msg = updateAddress(name, address)
    elif req[0].lower()=="updatephone":
        name = req[1]
        phone=req[2]
        msg = updatePhone(name,phone)
    elif req[0].lower()=="save":
        msg = writeIntoFile()
    else:
        msg =printRecord()
    return msg

def writeIntoFile():
    f = open("data.txt", "w")
    res = ""
    for k in sorted(dict.keys()):
        v = dict[k]
        var = "|"
        recoStr = var.join(v)
        res += recoStr+"\n"
    f.write(res)
    f.flush()
    f.close()
    result="the data saved successfully."
    return result

def printRecord():
    m = ""       
    for k in sorted(dict.keys()):
        v = dict[k] 
        m += str(v)+"\n"
    return m

def addRecord(name, age, address, phone):
    key = name.lower()
    if key not in dict:
        recordTup = (name,age,address,phone)
        dict[key] = recordTup
        msga = "Customer added successfully"
    else:
        msga = "Customer already exists"
    return msga

def findRecord(name):
    key = name.lower()
    if key not in dict:
        msgf ="customer not found"
    else:
        msgf = str(dict[key])
    return msgf

def deleteRecord(name):
    key = name.lower()
    if key in dict:    
        del dict[key]               
        msgd = "customer delete successfully"
    else:
        msgd = "Customer does not exist"
    return msgd

def updateAge(name, age):
    key = name.lower()
    if key in dict:
        record = dict[key]
        recoList=list(record)
        recoList[1] =age 
        recNew = tuple(recoList)       
        dict[key] = recNew
        msgag = "The customer's age has update successfully."
    else:
        msgag = "Customer not found."
    return msgag

def updateAddress(name, address):
    key = name.lower()
    if key in dict:
        record = dict[key]
        recoList=list(record)
        recoList[2] =address 
        recNew = tuple(recoList)       
        dict[key] = recNew
        msgad = "The customer's address has update successfully."
    else:
        msgad = "Customer not found."
    return msgad

def updatePhone(name,phone):
    key = name.lower()
    if key in dict:
        record = dict[key]
        recoList=list(record)
        recoList[3] =phone 
        recNew = tuple(recoList)       
        dict[key] = recNew
        msgad = "The customer's phone number has update successfully."
    else:
        msgad = "Customer not found."
    return msgad



class MyUDPHandler(socketserver.BaseRequestHandler):
    
    def handle(self):
        data = self.request[0].strip()
        req = data.decode('utf8')
        socket = self.request[1]
        result = checkReq(req)
        rest = bytes(result,"utf-8")
        socket.sendto(rest, self.client_address)

if __name__ == "__main__":
    HOST, PORT = "localhost", 9999
    server = socketserver.UDPServer((HOST, PORT), MyUDPHandler)
    server.serve_forever()






