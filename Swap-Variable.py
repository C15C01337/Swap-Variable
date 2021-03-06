
#program to swap user input value

print("Devloped By C15C01337 (Bishal Aryal)")
print("Follow me on Twitter username @C15C01337")

a =input("Enter a value of a:")
b =input("Enter a value of b:")


def swap_values(user_val1, user_val2):
    c = user_val1
    user_val1 = user_val2
    user_val2 = c
    print(f'Swap Value of a is {user_val1}')
    print(f'Swap Value of b is {user_val2}')

swap_values(a, b)