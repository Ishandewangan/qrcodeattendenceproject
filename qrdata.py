import qrcode
import qrcodedatabase as qrd
import markattendence as mka
detail_store =[]
attendence='None'
def dataEntry():
    try:
        optio_n = int(input("1. Mark Attendence \n2. Admin login\n "))
        if(optio_n==1):
            mka.read_attendence()
        elif(optio_n==2):
            admin = input("Enter Password : ")
            if(admin=='L1997'):
                opt =int(input("1. Add New Student \n2. View Record\n"))
                if(opt==1):
                    while(True):
                        name=input("Enter name : ")
                        roll_no=int(input("Enter roll number : "))
                        m_no=int(input("Enter mobile number : "))
                        qrd.insertValue(name,roll_no,attendence,m_no)
                        ex_it=input("If you want to add more y or n :")
                        detail_store.append([roll_no,name])
                        if(ex_it=="n"):
                            break
                elif(opt==2):
                    print("Your Record is \n")
                    qrd.dataFetch()
            else:
                print('Wrong password')
        for i in range(0,len(detail_store)):
            for j in range(1):
                qr_img =qrcode.make(f"\t{detail_store[i][j]}\n\t{detail_store[i][j+1]}")
                qr_img.save(f"{detail_store[i][j]}.jpg")
    except Exception as e:
        print(e)
qrd.databaseCreate()
qrd.tableCreate()
dataEntry()


