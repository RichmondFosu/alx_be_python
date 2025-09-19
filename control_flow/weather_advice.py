# Prompt user for weather input
current_weather = input('What is the weather like today? (sunny/rainy/cold): ')

# Clothing recommendation
if current_weather == 'sunny':
    recommendation = 'Wear a t-shirt and sunglass.'
elif current_weather == 'rainy':
    recommendation = 'Dont forget your umbrella and a raincoat.'
elif current_weather == 'cold':
    recommendation = 'Make sure to wear a warm coat and a scarf.'
else: print('Sorry, I dont have recommendation for this weather.')
print(recommendation)
