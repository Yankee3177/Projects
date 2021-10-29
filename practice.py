def translateTime(typee,orig,offset):
    return (orig+offset) % typee


typee = int(input("Enter 12 or 24..."))
orig = int(input("Enter time to be translated"))
offset = int(input('Enter hours to be added...'))
print('Your new time is...',translateTime(typee,orig,offset))


