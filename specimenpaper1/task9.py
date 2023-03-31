# Question 9

f = input()
pstep = f

dm = f

for i in range(7):
    if pstep == '<':    
        dm = dm + '+'
        pstep = '+'
    
    elif pstep == '+':       
        dm = dm + "&"
        pstep = '&'
    
    elif pstep == '&': 
        dm = dm + '>'
        pstep = '>'
    
    elif pstep == '>':
        dm = dm + '<'
        pstep = '<'
        
print(dm)
