Stefan Emmons 
COSC 2030-01 
Lab 03 
Dr. Hill, or Pedro Marquez 
2-27-2019 

Note that unless we import "math" or "operator", most compilers don't know what "sqrt" or "√" means. To keep things simple, I will keep everything in much of the same format as was done in the lab. 
The quadratic formula I am working with: [(-b +- (b^2 - 4ac)^0.5) / (2a)] 
This is first variation of the Quadratic Formula, using postfix notation: 
b - b 2 ^ 4 a * c * - 0.5 ^ 2 a * / + /
Conversely, the second variation of the Quadractic formula using postfix notation is: 
b - b 2 ^ 4 a * c * - 0.5 ^ 2 a * / - 
This is first variation of the Quadratic Formula, using prefix notation: 
/ + - b ^ + ^ b 2 * * 4 a c 0.5 * 2 a 
Conversely, the second variation of the Quadractic formula using prefix notation is: 
/ + - b ^ - ^ b 2 * * 4 a c 0.5 * 2 a 
