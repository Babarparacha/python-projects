
def count_words(text):
     # hey there how are you=>["hey","there","how","are","you"]
     words=text.split()
     return len(words)
def count_characters(text,include_spaces):
    if include_spaces:
        return len(text)
    else:
        return len(text.replace(" ",""))
def count_sentence(text):
    sentence_endings=[".",",","!","?"]
    count=0
    for char in text:
      if char in sentence_endings:
       count+=1
    #    handling the edge case
    if count==0 and text.strip():
        count=1   

    return count
def analyze_text(text):
   word_count=count_words(text)
   chat_count_space=count_characters(text,True)
   chat_count_without_space=count_characters(text,False)
   sentence_count=count_sentence(text)
   if sentence_count>0:
       words_per_sentence=word_count/sentence_count
   else:
       words_per_sentence=0
   if word_count>0:
       chars_per_word=chat_count_space/word_count
   else:
       chars_per_word=0   
   print("=== text analyze result==")   
   print(f"• words: {word_count}")
   print(f"• character with spaces: {chat_count_space}")
   print(f"• character without spaces: {chat_count_without_space}")
   print(f"• sentences: {sentence_count}")
   print(f"• average word per sentence: {words_per_sentence:.1f}")
   print(f"• average character per sentence: {chars_per_word:.1f}")
   print("===😁word counter===")
   print("===😁count words,characters and sentence in your text===")
   reading_time_minutes=word_count/225
   if reading_time_minutes<1:
       reading_time_seconds=reading_time_minutes*60
       print(f". estimate reding time :{reading_time_seconds:.0f} seconds")
   else:
       print(f". estimate reding time :{reading_time_minutes:.1f} seconds")
       
def main():
    while True:
        print("choose an option")
        print("1-enter text to anlyze")
        print("2-exit")
        choice=input("your choice 1/2:")
        if choice=="1":
            print("enter or paste your text below(press enter twice to finish )")
            lines=[]
            while True:
                line=input()
                if not line and not lines[-1]:
                    break
                else:
                    lines.append(line)
            text="".join(lines)
            if not text.split():
                print("no text provided! please try agian")
                continue
            analyze_text(text)        
        elif choice=="2":
            print("goodbye!")
            break
        else:
            print("❌ invalid choice! choose 1 or 2 ")
        
main()