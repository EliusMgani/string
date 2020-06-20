# capitalize()
s = "apkZube"
print(s.capitalize())
print()

# count()
y = "I love Python Tutorial"
print(y.count("o"))
print(y.count("o", 5))
print(y.count("t"))
print(y.count("t", 2, 9))
print()

# index()
y = "I love Python Tutorial"
print(y.index("i"))
print(y.index("i",2))
print(y.index("love"))
print(y.index("h",1,16))
print(y.index("rial",5))
print()

# find()
y = "I love Python Tutorial"
print(y.find("I"))
print(y.find("I",2))
print(y.find("love"))
print(y.find("t",2,10))
print()

# isalpha()
k = 'I love Python 3 Tutorial'
j = 'Nospace'
print(k.isalpha())
print(j.isalpha())
print()

# isalnum()
k = 'I love Python 3 Tutorial'
j = 'Nospace'
print(k.isalnum())
print(j.isalnum())
print()

#isdigit()
k = 'I love Python 3 Tutorial'
j = 'Nospace'
print(k.isdigit())
print(j.isdigit())
print()

# islower()
k = 'I love Python 3 Tutorial'
j = 'Nospace'
print(k.islower())
print(j.islower())
print()

# isupper()
k = 'I love Python 3 Tutorial'
j = 'Nospace'
print(k.isupper())
print(j.isupper())
print()

# isnumeric()
k = 'I love Python 3 Tutorial'
j = '10251784'
print(k.isnumeric())
print(j.isnumeric())
print()

# isspace()
k = 'I love Python 3 Tutorial'
j = 'Nospace'
l = ' '
print(k.isspace())
print(j.isspace())
print(l.isspace())
print()

# istitle()
k = 'I love Python 3 Tutorial'
j = 'Nospace'
print(k.istitle())
print(j.istitle())
print()

#len()
k = 'I love Python 3 Tutorial'
j = '3456 2829 3937 3423 45332 456 3678'
print(len(k))
print(len(j))
print()

# lower()
k = 'I love Python 3 Tutorial'
j = 'Nospace'
h = '3456 2829 3937 3423 45332 456 3678'
print(k.lower())
print(j.lower())
print(h.lower())
print()

# upper()
k = 'I love Python 3 Tutorial'
j = 'Nospace'
h = '3456 2829 3937 3423 45332 456 3678'
print(k.upper())
print(j.upper())
print(h.upper())
print()

# max()
# depend on alphabetic order i.e a to z
# dpend on numerical order i.e 0 to 9
k = 'I love Python 3 Tutorial'
j = 'Nospace'
h = '3456 2829 3937 3423 45332 456 3678'
print(max(k))
print(max(j))
print(max(h))
print()

# min()
# depend on alphabetic order i.e a to z
# dpend on numerical order i.e 0 to 9
k = 'IlovePythonTutorial'
j = 'Nospace'
h = '3456282939373423453324563678'
print(min(k))
print(min(j))
print(min(h))
print()

# raplace()
g = 'I Love Python Tutorial, I Love ApkZube, I Love Coding'
print(g.replace('Love', 'like'))
print(g.replace('Love', 'like', 1))
print(g.replace('I', 'She',2))
print()

# split()
g = 'I Love Python,Java,Android,PHP,JavaScript'
print(g.split(','))
print(g.split(',',2))
print()

# swapcase()
g = 'I Love Python, Java, Android, PHP, JavaScript'
print(g.swapcase())
print()