# Activity 1:

# create a class:
class IOString():

    def __init__(self):
        self.str1 = ""

    def get_String(self):
        self.str1 = input("Enter a string: ")

    def print_String(self):
        print("The result is:", self.str1.upper())

# object creation:
str1 = IOString()

# call fuctions:
str1.get_String()
str1.print_String()


# Activity 2:

class Employee():

    def __init__(self):
        print('Employee created')

    def __del__(self):
        print("Destructor called")

def Create_obj():
    print("making a object...")
    obj = Employee()
    print("function ended...")
    return obj

print('Calling Create_Obj function')
obj = Create_obj()
print("Program end...")


# Activity 3:

class pair_elements():

    def twoSum(Self, nums, target):
        lookup = {}

        for i, num in enumerate(nums):
            if target - num in lookup:
                return (lookup[target - num], i)
            lookup[num] = i

# Take input of dum from user
value = int(input("Enter the sum for which you want to make this search : "))

print("Index1=%d, index2=%d" %pair_elements().twoSum((10,20,30,40,50,60,70), value))
