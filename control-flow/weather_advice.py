#Weather Recommendation Program
#input current weather 
weather = input("What's the weather like today? (sunny/rainy/cold):")

# clothing recommendations
if weather == "sunny":
    print(f"Wear a t-shirt and sunglasses.")
elif weather == "rainy":
    print(f"Don't forget your umbrella and a raincoat.")
elif weather == "cold":
    print(f"Make sure to wear a warm coat and a scarf.")
else:
    print(f"Sorry, I don't have recommendations for this weather.") 
