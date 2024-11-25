str1=input("Enter a first string:")
str2=input("enter a second string:")
print(sorted(str1))
print(sorted(str2))
if sorted(str1)==sorted(str2):
    print("these are anagrams")
else:
    print("these are not anagrams")