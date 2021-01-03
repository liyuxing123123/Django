#/python3

countryname = input("Enter country name: ")

countryname = countryname.lower()
print(countryname)
lastcharacter = countryname.strip()[-1]
print(lastcharacter)

if 'a' in lastcharacter:
    print("Vowel found")
elif 'e' in lastcharacter:
    print("Vowel found")
elif 'i' in lastcharacter:
    print("Vowel found")
elif 'o' in lastcharacter:
    print("Vowel found")
elif 'u' in lastcharacter:
    print("Vowel found")
else:
    print('No vowel found')


