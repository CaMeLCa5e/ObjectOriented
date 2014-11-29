class parentClass:
	var1 = "jack"
	var2 = "pumba"

class childClass(parentClass):
	pass

parentObject = parentClass()

print parentObject.var1

childObject = childClass()

print childObject.var2
print childObject.var1