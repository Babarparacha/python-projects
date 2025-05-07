from langdetect import detect

text=input("Enter word to detect language:")
language=detect(text)
print(f"the language is: {language}")
