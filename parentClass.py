class Mom: 
	var1 = "hi mom"

class Dad:
	var2 = "hi i'm dad"

class child(Mom, Dad):
	var3 = "brand new var"
	#child has all parent attrs
childObject = child()

print childObject.var1
print childObject.var2

