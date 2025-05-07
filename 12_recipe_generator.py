import random
proteins=['chicken','beef','tofu','fish','eggs']
veggies=['barocoli','carrot','spinach','bell perry','mushrom']
carbs=['rice','pasta','potatoes','quinoa','bread']
methods=['baked','grilled','stir-fried','roasted','sauteed']
flavours=['garlic','lemon','spicy','herb','sweet & sour']

while True:
    protein=random.choice(proteins)
    veggie=random.choice(veggies)
    carb=random.choice(carbs)
    method=random.choice(methods)
    flavour=random.choice(flavours)
    print(f"your random recipe is this {flavour} {method} {protein} with {veggie} and {carb} ")
    if not input("generate antoher one (y/n):").lower().startswith('y'):
     print("good bye 🙋‍♂️")
     break
