import random
import time

def chatBot():
    greetings=["hello there!","hi Friend!","nice to meet you","how do you do"]
    
    farewels=['Goodbye!','See you later!','bye bye!','Howdy!']
    jokes=["why don't scientist trust atoms? cz they make up everything",
           "what do you calla fake noddle? an imppasta",
           "why did the scarecrow win an award? cz he was outstanding in his field",
           "what do you call a bear with no teeth? a gummy bear!"]
    facts=["Honey never sopils! Archaeologists found 300-year old honey",""
    "Octapuses have three hearts",""
    "A day on venus is longer than a year on venus",
    "The Hawaiian alphabet has only 12 letters"]
    bot_name="chatbot"
    print(f"🍾{bot_name} is starting up....")
    time.sleep(1)
    print(f"""welcome to {bot_name}!
          
          I can chat about:
          'joke'-Hear a funny joke
          'fact'-learn something new
          'color'-my fav color
          'bye'-end our chat
          """)
    chatting=True
    user_name=input("enter your name:")
    print(f" {bot_name}: nice to meet youm {user_name}! how can we help you today")
    while chatting:
        user_input=input("(😁 you):").strip()
        if user_input in ["hi","hello","hey","howdy"]:
            print(f"{bot_name} :{random.choice(greetings)}")
        elif "joke" in user_input:    
            print(f"{bot_name} :{random.choice(jokes)}")
        elif "joke" in user_input:    
            print(f"{bot_name} :{random.choice(jokes)}")
        elif "fact" in user_input:    
            print(f"{bot_name} :{random.choice(facts)}")
        elif "color" in user_input:    
            print(f"{bot_name}: my favourite color is blue! what 's yours?")
            color=input("😁you").strip()
            print(f"{bot_name}:{color} is a great color")
        elif user_input in ["bye","goodbye","exit","quit"]:
            print(f"{bot_name}:{random.choice(farewels)}")
            print(f"{bot_name}: it was fun chatting with you,{user_name}")
            chatting=False
        else:
            responses=[
                "that intersting tell me more",
                "i am not sure i understand! can you try again",
                "Hmmm let talk somthing else. try asking for a joke"
                "beep boop! my robot brain is processing...."
            ]      
            print(f"{bot_name}:{random.choice(responses)}")
        print("thanks for chatting! Run the program again to talk to me later")



chatBot()    
