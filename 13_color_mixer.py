color_mixes={
    ('red','blue'):'purple',
    ('red','yellow'):'orange',
    ('blue','yellow'):'green',
    ('blue','green'):'teal',
    ('white','red'):'pink',
    ('red','green'):'brown',
}

while True:
    color1=input("enter your fixex color 1:").strip()
    color2=input("enter your fixex color 2:").strip() #for space like 'red  '=>'red'

    mix=None
    if(color1,color2) in color_mixes:
        mix=color_mixes[(color1,color2)]
    elif(color2,color1) in color_mixes:
        mix=color_mixes[(color2,color1)]
    if mix:
        print(f" when you mix {color1} and {color2},you get {mix} ")
    else:
        print("i do not know what colors make when mixed")
    if not input("mix more colors(y/n):").lower().startswith('y'):
        print('good bye')
        break    