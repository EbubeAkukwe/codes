#Email slicer without re module

email = input("Enter Email : " )
x = email.find('@')
emails = []
for j in email :
    emails.append(j)
y = len(emails)
name = emails[:x]
domain = emails[x::]
#converting list to string
name_ = ''.join(map(str,name))
domain_ = ''.join(map(str,domain))
print(name_)
print(domain_)
