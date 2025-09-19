# Prompt user for weather input
Prompt = input("What's the weather like today? (sunny/rainy/cold):")

# Clothing recommendation
if Prompt == 'sunny':
    recommendation = 'Wear a t-shirt and sunglass.'
elif Prompt == 'rainy':
    recommendation = 'Dont forget your umbrella and a raincoat.'
elif Prompt == 'cold':
    recommendation = 'Make sure to wear a warm coat and a scarf.'
else: print('Sorry, I dont have recommendation for this weather.')
print(recommendation)
