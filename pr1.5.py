sales_proceeds = int(input("Enter your company sales proceeds,$ - "))
costs = int(input("Enter your company costs,$ - "))

if costs < sales_proceeds:
    profitability = ((sales_proceeds - costs) / sales_proceeds)
    print(f'Your campaign is generating revenue! Business profitability is {profitability * 100}%')
    num_emp = int(input('Enter number of company employees - '))
    print(f'Profit for one employee is {(sales_proceeds - costs) / num_emp}$')
else:
    print('Sorry, but the campaign is running at a loss(')
