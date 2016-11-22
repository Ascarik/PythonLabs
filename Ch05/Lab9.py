future_tuition = 10000;


for i in range(1, 11):
    print(i, "year equals", round(future_tuition, 2))
    future_tuition += future_tuition * 0.05
