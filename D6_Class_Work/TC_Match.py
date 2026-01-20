import re

text = "python is powerful programing language"
#match  Beginning of string only
#Matches pattern only at the beginning of the string.

result = re.match("python", text)
if result:
    print("match found")
else:
    print("no match found")


#Searches for pattern anywhere in the string.
searchresult = re.search("powerful", text)
print(searchresult.group())
print(searchresult.start())
print(searchresult.end())

email = "bhagya@gmail.com"
if re.match(r"[a-zA-Z]+@", email):
    print("Valid Start")

#fullmatch
result2 = re.fullmatch(r"\d{10}", "1234567898")
print(result2)

#findall Returns a list of all matching substrings.
print(re.findall(r"\d+", "price 50 and 100 and 200"))

for n in re.finditer(r"\d+", "A1 b1000, B33, C444"):
    print(n.group(), n.start(), n.end())

for n in re.finditer(r"[a-z]", "a1 b1000, B33, C444"):
    print(n.group(), n.start(), n.end())
for n in re.finditer(r"[A-Z]", "a1 b1000, B33, C444"):
    print(n.group(), n.start(), n.end())

print(re.search(r"\d+","Age is 25"))

print(re.search(r"^a.*c$","abnkkkknnc"))

m=re.search(r"\w+(?=@)","bhagya@gmail.com")
print(m.group())

print(re.search("python","Python",re.I))

text2="one\ntwo\nthree"
print(re.findall(r"^o\w+",text2,re.M))
