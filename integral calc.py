#integral calculator, figure out how to make it work for any function
print ("this is an integral calculator :D, it finds integrals of constants. input desired limits and function")
print ("input function as integer in the format of ax (only input a)")
#get input statement working
#input function after i
i=6
function= i
print (function)
print ("x")
print ("now, input boundary b as an integer")
b= input(int)
b= int (b)
print (b)
print ("∫ a dx")
integral1= (b ** 2)
print ("this is the integral of boundary b")
print (integral1)
print ("+C")
print ("now, input boundary a as an integer")
a= input(int)
a= int (a)
print ("∫ a dx")
print (a)
integral2= (a**2)
print ("this is the integral of boundary a")
print (integral2)
print ("+C")
print ("this is the integral of your function")
value1= (integral1*function)
value2= (integral2*function)
print (value1-value2)




