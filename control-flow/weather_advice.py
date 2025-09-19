# Prompt user for weather input
weather_input = input("What's the weather like today? (sunny/rainy/cold): ")

# Clothing recommendation
if weather_input == 'sunny':
    recommendation = 'Wear a t-shirt and sunglass.'
elif weather_input == 'rainy':
    recommendation = 'Dont forget your umbrella and a raincoat.'
elif weather_input == 'cold':
    recommendation = 'Make sure to wear a warm coat and a scarf.'
else: print('Sorry, I dont have recommendation for this weather.')
print(recommendation)
