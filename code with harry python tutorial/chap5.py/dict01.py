a = {
    "key": "value",
    "mru": "coder",
    "marks": "100",
    "list": [1,2,3]
    }
print(a)
print(type(a))

print(a['mru'])
print(a['key'])
print(a['marks'])
print(a['list'])

print(a)
update_a = {'mru':'dancer'}
a.update(update_a)
print(a)


#diff between .get() and []

print(a.get("mru"))
print(a["mru"])

print(a.get("mru2")) #returns None
#print(a["mru2"])    # throws an error bcoz mru2 not present in list. 


#dict methods 

print(a.items())
print(a.keys())
print(a.update({"mru": "singer"}))
print(a.get("mru"))