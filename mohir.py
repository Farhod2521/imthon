from os import remove


class Talaba:
    def bakalavr1(self, student_id, full_name, nationatily, gender, faculty, admisson_year, resident_hall):

        self.student_id = student_id
        self.full_name = full_name
        self.nationatily = nationatily
        self.gender = gender
        self.faculty = faculty
        self.adminsson_year = admisson_year
        self.resident_hall = resident_hall
    
    def magister2(self, student_id, full_name, nationatily, gender, faculty, admisson_year, resident_hall):

        self.student_id = student_id
        self.full_name = full_name
        self.nationatily = nationatily
        self.gender = gender
        self.faculty = faculty
        self.adminsson_year = admisson_year
        self.resident_hall = resident_hall
    global Bakalavr, Magister
    Bakalavr = []
    Magister = []
    ################################################################## ADD BAKALAVR ##################################
    #######################################################################################################3
    
    def add_bakalavr():
        bakalavr = {}
        
        stundent_id  =  int(input("Stundent Id: "))
        full_name = input("Full_name:")
                
        nationatily = input("Nationatily:")
        gender  = input("Gender:")
        faculty = input("Faculty:")
        adminsson_year = input("Adminsson Year:")
        resident_hall = input("Resindent Hall:")
        bakalavr[stundent_id] = full_name, nationatily,gender,faculty,adminsson_year,resident_hall
        Bakalavr.append(bakalavr)
        return bakalavr

    ################################################################## ADD MAGISTER ##################################
    #######################################################################################################3
    def add_magister():
        magister = {}
        
        stundent_id  =  int(input("Stundent Id: "))
        full_name = input("Full_name:")
                
        nationatily = input("Nationatily:")
        gender  = input("Gender:")
        faculty = input("Faculty:")
        adminsson_year = input("Adminsson Year:")
        supervisor_name = input("Supervisor Name:")
        research_topic = input("Research Topic:")
        magister[stundent_id] = full_name, nationatily,gender,faculty,adminsson_year,supervisor_name,research_topic
        Magister.append(magister)
        return magister

    ######################################### REMOVE ########################################################
    #########################################################################################################
    def remove():
        print("================================")
        print("Bakalavr Talablari")
        for i in Bakalavr:
            print(i)

        print("=================================")
        print("Magister Talablari")
        for i in Magister:
            print(i)
        print("============================")
        print("Talaba o'chirish uchun bo'limni tanlang!")
        print(" ")
        print("a)Bakalavr")
        print("b)Magister")
        harf =  input("a yoki b ni  kiriting:")
        if harf == 'a':
            print("Talabani o'chirish  stundent ID kiriting !!! ")
            a = int(input("Stundent ID: "))
            
            for i in Bakalavr:
                if i[a]:
                    del i[a]
                else:
                    print("Bunday Id mavjud emas")
                    remove()
            print("=============================")
            print("Bakalavrda qolgan talabalar Ro'yhati")
            for i in Bakalavr:
                print(i)
            
        elif harf == 'b':
            print("Talabani o'chirish  stundent ID kiriting !!! ")
            a = int(input("Stundent ID: "))
            
            for i in Magister:
                del i[a]
            print("=============================")
            print("Magisterda qolgan  talabalar Ro'yhati")
            for i in Magister:
                print(i)
            return restart()
    ############################################ SEARCH ################################################
    #####################################################################################################
    def search():
        print("============================")
        print("Talaba qidirish uchun bo'limni tanlang!")
        print(" ")
        print("a)Bakalavr")
        print("b)Magister")
        harf =  input("a yoki b ni  kiriting:")
        if harf == 'a':
            print("Talabani qidirish uchun  stundent ID kiriting !!! ")
            a = int(input("Stundent ID: "))
            
            for i in Bakalavr:
                if i[a]:
                    d = i[a]
                    print(d)
                    print(f"Full Name: {d[0]},\n Nationatily: {d[1]},\nGender: {d[2]},\nFaculty: {d[3]},\nAdminssion Year: {d[4]} ,\nSupervisor Name: {d[5]}   ")
        if harf == 'b':
            print("Talabani qidirish uchun  stundent ID kiriting !!! ")
            a = int(input("Stundent ID: "))
            
            for i in Magister:
                if i[a]:
                    d = i[a]
                    print(d)
                    print(f"Full Name: {d[0]},\n Nationatily: {d[1]},\nGender: {d[2]},\nFaculty: {d[3]},\nAdminssion Year: {d[4]} ,\nSupervisor Name: {d[5]}   ")
        
    ############################### DISPLAY ALL ###################################################
    # ##############################################################################################              
    def display_all():
        print("===============================================")
        print("-------Bakalavrda o'qiydigan talabalar ro'yhati------")
        print("===============================================")
        for i in Bakalavr:
            print(i)
        print("===============================================")
        print("-------Magisterda o'qiydigan talabalar ro'yhati------")
        print("===============================================")
        for i in Magister:
            print(i)

            

print("######################  Assalomu Alaykum Xush kelibsiz X unversityga  ####################################")
def restart():
    print("==========================================================")
    print("==========================================================")
    print("Quydagi buyruqlarni bajarish uchun sonni tanglang ")
    print(" ")
    print("1)Add (yangi talaba qo'shish)")
    print("2)Remove (talabani tizimdan o'chirish Stundent ID bo'yicha)")
    print("3)Find (talabani id bo'yicha izlash )")
    print("4)Display All (Tizimda barcha ma'lumotlar ko'rish)")
    print("5)Exit (tizimdan chiqish) ")
    print("==========================================================")
    print("==========================================================")
    son  =  int(input("Raqamni tanlang: "))
    while son <= 0 or son>5:
        print("Bunday buyruq mavjud emas ( 1 dan 5 gacha )!!!!!! ")
        son  =  int(input("Raqamni tanlang: "))
    if  son == 2:
        return two()
    if  son ==3:
        return three()
    if son == 4:
        return four()
    if  son == 5:
        return five()
    return son
def two():    
    Talaba.remove()
    return restart()
def three():
    Talaba.search()
    return restart()
def four():
    Talaba.display_all()
    return restart()
def five():
    print("E'tiboringiz uchun rahmat !!!")
    exit()

son =  restart()

if son == 1:
    def one():
        
        while son == 1:
            print("=====================================")
            print("=====================================")
            print("Talaba qo'shish uchun bo'limni tanlang!")
            print(" ")
            print("a)Bakalavr")
            print("b)Magister")
            harf =  input("Kirting:")
            if harf == 'a':
                Talaba.add_bakalavr()
                print("========================================================")
                print("========================================================")
                print("Bosh sahifaga qaytish uchun 1 ni bosing!")
                print("Talaba qo'shish uchun 2 ni bosing!")
                a =  int(input("kiriting:"))
                if a == 1:
                    return restart()
                elif a == 2:
                    return one()
            if harf == 'b':
                Talaba.add_magister()
                print("========================================================")
                print("========================================================")
                print("Bosh sahifaga qaytish uchun 1 ni bosing!")
                print("Talaba qo'shish uchun 2 ni bosing!")
                a =  int(input("kiriting:"))
                if a == 1:
                    return restart()
                    
                elif a == 2:
                    return one()
        return one()
    one()


       