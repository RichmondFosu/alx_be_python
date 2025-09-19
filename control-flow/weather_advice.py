# Prompt user for weather input
prompt = input('What is the weather like today? (sunny/rainy/cold): ')

# Clothing recommendation
if prompt == 'sunny':
    recommendation = 'Wear a t-shirt and sunglass.'
elif prompt == 'rainy':
    recommendation = 'Dont forget your umbrella and a raincoat.'
elif prompt == 'cold':
    recommendation = 'Make sure to wear a warm coat and a scarf.'
else: print('Sorry, I dont have recommendation for this weather.')
print(prompt)
