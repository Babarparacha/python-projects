#check if website contain an https or not

print('🔍 website url cheker 🔍')
url=input("\n enter a website url: ")
if url.startswith("https:"):
    print('this website uses https(secure)')
elif url.startswith('http'):
    print('❌this website does not contain https(not secure)')
else:
    print('this does not look like complete url')    