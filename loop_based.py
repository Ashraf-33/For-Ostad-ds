result = 0
for i in range(1,101):
    # the number i can multiply 3 or 5 those will work
    if i%3 == 0 or i%5 == 0:
        
        # after that find i that  multiply 15 and skip
        if i%15 == 0:
            continue 
        
        # now add the i in result;
        result=result+i

        # when the result goes above 2000 stop the loop;
        if result > 2000:
            break
print(result)    
