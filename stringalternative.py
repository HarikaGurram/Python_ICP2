def main():
    user_input = input('please enter a string :')  #taking input from user
    print('String Alternative Output :',string_alternative(user_input)) #calling sub function from main function and printing out the result

def string_alternative(user_input):  #creating subfunction
    return user_input[::2]           #using index slicing step function to return alternative strings

if __name__ == '__main__':
    main()                      #calling main function