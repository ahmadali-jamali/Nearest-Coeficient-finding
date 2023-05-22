
#finding  Coefficient function
def finding_Coefficient(n):
    if n%5 == 0: # the coeficient 
        return True
    else:
        return False

#finding the nearest coefficient
def finding_nearest_Coefficient(n):
    m = n
    s = n
    for i in range(1,6):
        k = i+m
        if finding_Coefficient(k)== True:
            return k
            break
        l = s-i
        if finding_Coefficient(l)== True:
            return l
            break
        
#main function        
if __name__ == "__main__":

    n = int(input('Please insert integer number:\n'))
    print(finding_nearest_Coefficient(n))
    
    
    
