subtotal, gratuity = eval(input("Enter the subtotal and a gratuity rate: "))

gratuity /= 100
gratuity = subtotal * gratuity
total = subtotal + gratuity

print("The gratuity is", round(gratuity, 2), "and the total is", round(total, 2))
