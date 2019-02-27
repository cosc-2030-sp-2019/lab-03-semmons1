#Stefan Emmons
#COSC 2030-01
#Lab 03
#Dr. Hill, or Pedro Marquez
#2-27-2019

#As with the last program,
#Much of this lab is the same as the original Python program, nothing chanes until the calculate function.
import operator 
ops = {
       '+':operator.add,
       '-':operator.sub,
       '*':operator.mul,
       '/':operator.truediv,
       '^':operator.pow
       }

def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        pass

def calculate(exp):
    stack = []
    stack_2 = [] #because of the way prefix notation is read into a list, we need a second stack to hold operators.
    #As can be seen below, the loop structure that reads in characters is the same, however, stack #2 will hold the operands, whereas stack #1 will hold the
    #operators. 
    result = 0
    for i in exp:
        stack.insert(0,i)
    for i in stack:
        if is_number(i):
            stack_2.insert(0,i)
            #From here onwards, the expression itself is calculated in much of the same way that one would with RPN. For the sake of consistency, we will be
            #using insert functions which require position arguments. 
        else:
            if (len(stack)<2):
                print ('Error: insufficient values in expression')
                break
            else:
                print ('stack: ', stack_2, 'where i = ', i) #Stack #2 has all operands, so this print statement needs to be modified slightly.
                operand1 = float(stack_2.pop(1)) #Same pop functions, just a different stack.
                operand2 = float(stack_2.pop(0))
                if (i=='/' or i =='^'): #As with the previous Postfix Program, some operators are position sensitive. If these two specific operators are
                    #encountered, we must flip the operands to acquire the correct result. Beyond this small modification, everything is printed in much of 
                    #the same format. 
                    result = ops[i](operand2, operand1)
                else:
                    result = ops[i](operand1,operand2)
                stack_2.insert(0,str(result))
    return result

print ("Start of Prefix Notation Evaluator")
exp_file = open("prefix_express_1.txt", 'r')
for line in exp_file:
        exp_list = line.rstrip().split(' ')
        answer = calculate(exp_list)
        print ('RESULT: %f' % answer)
print ("End of Prefix Notation Evaluator")
exp_file.close()

#For the sake of being able to effectively check my own work, I have created my own 
#prefix notation document.
#Expression 1: + * 568 6 / 99 5 = 3427.8, this comes out correct!
#Expression 2: / * 33 + 7 2 400 = 0.7425, this comes out correct!
#Expression 3: * 88 + 2 / 21 5 = 545.6, this comes out correct!
#Expression 4: - 600 + 2 ^ 7 9 = 40,353,009, this comes out correct!