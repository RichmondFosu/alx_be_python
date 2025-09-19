# Prompt user for weather input
weather = input("What's the weather like today? (sunny/rainy/cold):")

# Clothing recommendation
if weathert == 'sunny':
    recommendation = 'Wear a t-shirt and sunglass.'
elif weather == 'rainy':
    recommendation = 'Dont forget your umbrella and a raincoat.'
elif weather == 'cold':
    recommendation = 'Make sure to wear a warm coat and a scarf.'
else: print('Sorry, I dont have recommendation for this weather.')
print(recommendation)
