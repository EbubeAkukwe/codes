import random
num1 = '0903'
num2 = '0806'
num1_ = ''
num2_ = ''
mtn_num1 = []
mtn_num2 = []
v = ''
f = 9999999
with open ('mtnphonenumbers.txt' , 'a') as mtn_nums :
    while f > 0 :
        for i in range(0, 9999999, 1) :
            v = 7 - len(str(i))
            if v == 0 :
                pass
            else:
                if v >0<=7 :
                    i_ = ("{p}"+str(i)).format(p = "0"*(v))
                    i = (str(i)+"{p}").format(p = "0"*(v))
                else:
                    pass
            num1_ = num1+ str(i_)
            num1_rev = num1 + str(i)
            num2_ = num2+ str(i_)
            num2_rev = num2 + str(i)
            #write numbers to .txt file
            mtn_nums.write(num1_ + "\n")
            mtn_nums.write(num2_ + "\n")
            mtn_nums.write(num1_rev + "\n")
            mtn_nums.write(num2_rev + "\n")
            #print numbers
            '''mtn_num1.append(num1)
            mtn_num2.append(num2)
            mtn_num1.append(num1_rev)
            mtn_num2.append(num2_rev)
            print(num2_+"\n"+num2_rev)'''
        f -= 1
    mtn_nums.close()



