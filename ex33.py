xxx = []
def fun_name(loop_limit):
    i = 0
    numbers = []
    while i < loop_limit:
        print "At the top of i is %d" % i
        numbers.append(i)
        i = i + 1
        print "Numbers now: ", numbers
        print "At the bottom i is %d" % i
    return numbers
  
     
numbers2 = fun_name(13)
       

print "The numbers: "

for bp in numbers2:
    print bp 
        
