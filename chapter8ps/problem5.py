#wap  function to print first n lines od=f the folowing pattern
#***
#**
#*
# for n=3
def pattern(n):
    if(n==0):
        #print("") or return
        return
    print("*" *n)
    pattern(n-1)
    
pattern(3)