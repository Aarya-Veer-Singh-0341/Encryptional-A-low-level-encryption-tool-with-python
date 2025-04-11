def binary(num):
    if not isinstance(num, int):
        raise ValueError("Input must be an integer.")
    if num < 0:
        raise ValueError("Input must be a non-negative integer.")
    
    binary_list = []
    while num > 0:
        binary_list.append(num % 2)
        num //= 2
    binary_list.reverse()
    return binary_list


def decimal(binary_list):
    binary_list.reverse()
    if not isinstance(binary_list, list):
        raise ValueError("Input must be a list.")
    binary_decimal = []
    for i in range(len(binary_list)):
        if binary_list[i] != 0 and binary_list[i] != 1:
            raise ValueError("Input must be a binary list.")
        binary_decimal.append(binary_list[i]*(2**i))
    decimal_value = sum(binary_decimal)


Enc = []
print("\nData Entry")
Data = int(input("Enter Data you want to encrpyt: "))
binary_Data = binary(Data)

Pwd = int(input("Enter Password for encryption: ")) 
binary_Pwd = binary(Pwd)
print("\nProccessing...")

#equalising binary digits
if len(binary_Data) > len(binary_Pwd):
    data_pwd_diff = len(binary_Data) - len(binary_Pwd)
    binary_Pwd.reverse()
    for i in range(data_pwd_diff):
        binary_Pwd.append(int(0))
    binary_Pwd.reverse()
elif len(binary_Pwd) > len(binary_Data):
    data_pwd_diff = len(binary_Pwd) - len(binary_Data)

    binary_Data.reverse()
    for i in range(data_pwd_diff):
        binary_Pwd.append(int(0))
    binary_Data.reverse()



for i in range(len(binary_Data)):
    if binary_Data[i] == 1 and binary_Pwd[i] == 1:
        Enc.append(int(0))
    elif binary_Data[i] == 0 and binary_Pwd[i] == 0:
        Enc.append(int(1))
    elif binary_Data[i] == 1 and binary_Pwd[i] == 0:
        Enc.append(int(0))
    elif binary_Data[i] == 0 and binary_Pwd[i] == 1:
        Enc.append(int(1))


enter_pwd = int(input("Enter the password: "))
# binary_enter_pwd = binary(enter_pwd)

binary_enter_pwd = binary(enter_pwd)

# Equalising binary digits for enter_pwd and Enc
if len(binary_enter_pwd) > len(Enc):
    enter_pwd_diff = len(binary_enter_pwd) - len(Enc)
    Enc.reverse()
    for i in range(enter_pwd_diff):
        Enc.append(int(0))
    Enc.reverse()
elif len(Enc) > len(binary_enter_pwd):
    enter_pwd_diff = len(Enc) - len(binary_enter_pwd)
    binary_enter_pwd.reverse()
    for i in range(enter_pwd_diff):
        binary_enter_pwd.append(int(0))
    binary_enter_pwd.reverse()

new_data = []
for i in range(len(Enc)):
    if Enc[i] == 0 and binary_enter_pwd[i] == 0:
        new_data.append(int(1))
    elif Enc[i] == 1 and binary_enter_pwd[i] == 1:  
        new_data.append(int(0))
    elif Enc[i] == 1 and binary_enter_pwd[i] == 0:
        new_data.append(int(0))
    elif Enc[i] == 0 and binary_enter_pwd[i] == 1:
        new_data.append(int(1))

#Output
if new_data == binary_Data:
    print("Password is correct")
else:
    print("Password is incorrect")

print(f"\n{binary_Data}:Data given,\n{(Enc)}:Encrypted data")