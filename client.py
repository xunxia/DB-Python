import socket
import sys
HOST, PORT = "localhost", 9999

def showMenu():
    print("Python DB Menu\n")
    print("1.Find Customer")
    print("2.Add Customer")
    print("3.Delete Customer")
    print("4.Update Customer age")
    print("5.Update Customer address")
    print("6.Update Customer phone")
    print("7.Print Report")
    print("8.Exit")   
    print("9.Save back to file")
    return

showMenu()
while(True):
    valid = False
    while(not valid):
        choice = input("\nSelect:")
        valid = True
    if choice =="1":
        name = input("please enter the name:")
        data = "find"+";"+name
        sock1 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock1.sendto(bytes(data + "\n", "utf-8"), (HOST, PORT))
        received = str(sock1.recv(1024), "utf-8")
        print(received+"\n")
        showMenu()
        continue
    elif choice=="2":
        name = input("please enter the name:")
        age = input("please enter the age:")
        address = input("please enter the address:")
        phoneNumber = input("please enter the phone number:")
        data = "add"+";"+name+";"+age+";"+address+";"+phoneNumber
        sock2 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock2.sendto(bytes(data + "\n", "utf-8"), (HOST, PORT))
        received = str(sock2.recv(1024), "utf-8")
        print(received+"\n")
        showMenu()
        continue
    elif choice=="3":
        name = input("please enter the name:")
        data = "delete"+";"+name
        sock3 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock3.sendto(bytes(data + "\n", "utf-8"), (HOST, PORT))
        received = str(sock3.recv(1024), "utf-8")
        print(received+"\n")
        showMenu()
        continue
    elif choice=="4":
        name = input("please enter the name:")
        age = input("please enter the age:")
        data = "updateage"+";"+name+";"+age
        sock4 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock4.sendto(bytes(data + "\n", "utf-8"), (HOST, PORT))
        received = str(sock4.recv(1024), "utf-8")
        print(received+"\n")
        showMenu()
        continue
    elif choice=="5":
        name = input("please enter the name:")
        address = input("please enter the address:")
        data = "updateaddress"+";"+name+";"+address
        sock5 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock5.sendto(bytes(data + "\n", "utf-8"), (HOST, PORT))
        received = str(sock5.recv(1024), "utf-8")
        print(received+"\n")
        showMenu()
        continue
    elif choice=="6":
        name = input("please enter the name:")
        phoneNumber = input("please enter the phone number:")
        data = "updatephone"+";"+name+";"+phoneNumber
        sock6 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock6.sendto(bytes(data + "\n", "utf-8"), (HOST, PORT))
        received = str(sock6.recv(1024), "utf-8")
        print(received+"\n")
        showMenu()
        continue
    elif choice=="7":
        data = "print"
        sock7 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock7.sendto(bytes(data + "\n", "utf-8"), (HOST, PORT))
        received = str(sock7.recv(10240), "utf-8")
        print(received+"\n")
        showMenu()
        continue
    elif choice=="8":
        print("Good Bye")
        exit()
    elif choice=="9":
        data = "save"
        sock9 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock9.sendto(bytes(data + "\n", "utf-8"), (HOST, PORT))
        received = str(sock9.recv(1024), "utf-8")
        print(received+"\n")
        showMenu()
        continue
    else:
        print("invalid input, enter an integer between 1-9.\n")
        showMenu()
        continue