try:
    class calculator:
        def __init__(self, num1, num2):
            self.num1 = num1
            self.num2 = num2

        def add(self):
            return self.num1 + self.num2

        def multi(self):
            return self.num1 * self.num2

        def divi(self):
            return self.num1 / self.num2


    user = input('Whats Your Name?: ')
    print(
        'Hello, Welcome {} To The Calculator Program \ By:Me \ Twitter:@YaqubAlrubiaan \n ---------- \n '.format(user))
    print('\n ----------- \n type "m" if you want Mulitpy mode, \n type "a" if you want addition mode, \n type "d" if you want divison mode \n * type "every" if you want all modes! \n')
    modes = input('m or a or d or every?: ')

    if modes == 'm':
        addnum = int(input("Add The First Number Please:"))
        addnum2 = int(input("Add The Secound Number Please:"))
        x = calculator(addnum, addnum2)
        print(addnum, "X", addnum2, "=", x.multi())
    elif modes == 'a':
        addnum = int(input("Add The First Number Please:"))
        addnum2 = int(input("Add The Secound Number Please:"))
        x = calculator(addnum, addnum2)
        print(addnum, "+", addnum2, "=", x.add())
    elif modes == 'd':
        addnum = int(input("Add The First Number Please:"))
        addnum2 = int(input("Add The Secound Number Please:"))
        x = calculator(addnum, addnum2)
        print(addnum, "/", addnum2, "=", x.divi())
    elif modes == 'every':
        addnum = int(input("Add The First Number Please:"))
        addnum2 = int(input("Add The Secound Number Please:"))
        x = calculator(addnum, addnum2)
        print(addnum, "X", addnum2, "=", x.multi(), "\n", addnum, "+", addnum2, "=", x.add(), "\n", addnum, "/",
              addnum2, "=", x.divi(), )
        print("\n", "Total: ", x.multi() + x.divi() + x.add())
    else:
        print('There is an error, Please Check the information you entered or Contact me: Twitter:@YaqubAlrubiaan')
except:
    print('There is an error, Please Check the information you entered or Contact me: Twitter:@YaqubAlrubiaan')

finally:
    print("\n Thanks For Use The Program! <3")