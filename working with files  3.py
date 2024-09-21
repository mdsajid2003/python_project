#Showing the options
def operations():
 print('Enter the following options\n'
      'For finding:              "find"\n'
      'For replacing with serial "replace"\n'
      'For replacing all :       "replace all"')
#Taking the input from the user
 choice = input('Enter your choice: ')
#opening the file and reading it
 with open('example.txt','r') as f:
    data = f.read()
 c = 0
#checking the choice of the user
 if choice == 'find':   #the user choosing find
    words = data.split()
    len_words = len(words)
    print(data)
    inpst = input('Enter the string you want to find: ')
    for _ in words:
        if _ == inpst:
            c +=1
    print(f'Word "{inpst}": {c} ')  
 elif choice == 'replace':   #user choosing replace
    words = data.split()
    len_words = len(words)
    print(data)
    print(f'words: {len_words}')
    replace,replacing = replacedinput()
    serial  = int(input(f'enter the serial number to be placed replaced '
                        'there are {len_words} in the string'))
    if serial != len_words:
        data = data.replace(replace,replacing,serial)
        print(data)
    else:
        print('error')
 elif choice == 'replace all':  #user choosing replace all
    print(data)
    toreplace,replaced = replacedinput()
    data = data.replace(toreplace,replaced)
    print(data)
def replacedinput():
   toreplace = input('Enter the string you want to replace ')  #taking the string to be replace
   replaced =  input('Enter the string  to replace ')           #taking the new string to be placed
   return toreplace,replaced
operations()
