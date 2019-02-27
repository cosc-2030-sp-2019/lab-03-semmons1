#Stefan Emmons
#COSC 2030-01
#Lab 03
#Dr. Hill, or Pedro Marquez
#2-27-2019

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
    result = 0
    for i in exp:
        if is_number(i):
            stack.append(i) #As we were instructed to use append, we removed the position argument needed for insert, as append always adds to the bottom of the stack.
            #or the end of the list
        else:
            if (len(stack)<2):
                print ('Error: insufficient values in expression')
                break
            else:
                print ('stack: ', stack, 'where i = ', i)
                operand1 = float(stack.pop())# for both operand 1 and 2, the position argument for pop has been removed. Seeing as append only has one 
                #position designation, there is no need to specify where the operands are.
                operand2 = float(stack.pop())
                if (i=='-' or i=='/' or i =='^'): #Because of the nature of the way a stack is read (backwards), with position sensitive operators, we must
                    #flip the operands to acquire the correct product. This if statement specifies position sensitive operations, and flips the operands as needed.
                    result = ops[i](operand2, operand1)
                else:
                    result = ops[i](operand1,operand2) #anything else is treated the same because position is not important. 
                stack.append(str(result))
    return result

print ("Start of Reverse Polish Notation Evaluator")
exp_file = open("Expressions1.txt", 'r')
for line in exp_file:
        exp_list = line.rstrip().split(' ')
        answer = calculate(exp_list)
        print ('RESULT: %f' % answer)
print ("End of Reverse Polish Notation Evaluator")
exp_file.close()