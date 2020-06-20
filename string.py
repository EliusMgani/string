a = "hello"
b = "ApkZube"
print(a+" "+b)
print()

# Example of String.
name = "Rajat"
length = len(name)
i = 0
for n in range(-1, (-length-1), -1):
	print(name[i], "\t\t\t", name[n])
	i+=1
print()

# String Concatanation Operator
str1 = "Apk"
str2 = "Zube"
print(str1 + str2)
print()

# String Replication Operator
print("ApkZube " * 5)
print(3 * "Python ")
print()

# String Membership operator
c = "ApkZube"
d = "Apk"
e = "Zube"
f = "Dev"
print("Example of In operator")
print(d in c)
print(e in c)
print(f in c)
print()
print()
print("Example of Not In operator")
print(d not in c)
print(e not in c)
print(f not in c)
print()

# String Relational/Comparison Operator
print("ApkZube"=="ApkZube")
print("apkZube">="ApkZube")
print("A"<"a")
print()

#String Slice Notation
s = "Monty Python"
print(s[6:10])
print(s[-12:-7])
print(s[-1: :-1]) # Reversed all String
print(s[ : :-1]) # Reversed all String
print(s[2:10:2]) # Step 2
print(s[ :5]) # From 0 to 4
print(s[3: ]) # From 3 to the end of the String
print(s[ : ]) # Copy all String 