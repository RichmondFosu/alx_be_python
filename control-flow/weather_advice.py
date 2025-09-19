# Prompt user for weather input
weather = input("What's the weather like today? (sunny/rainy/cold):")

# Clothing recommendation

if weather == 'sunny':
    recommend("Wear a t-shirt and sunglasses.")
elif weather == 'rainy':
    recommendt(" Don't forget your umbrella and a raincoat.")
elif weather == 'cold':
    recommend("Make sure to wear a warm coat and a scarf.")
else:
    print("Sorry, I don't have a recommendation for this weather.")
print(recommend)