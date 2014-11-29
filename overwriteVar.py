
class parent:
	var1 = 'bacon'
	var2 = 'porkchops'

class child(parent):
	var2 = 'double porkchops'

pobj = parent()
cobj = child()
print pobj.var1
print cobj.var1
print cobj.var2
