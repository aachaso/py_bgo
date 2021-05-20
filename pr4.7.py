import json
firm_dict = {}
avarage_dict = {}
i = 0
total_income = 0

with open('test_7.txt', 'r') as file_corporate:
    for firm in file_corporate:
        name, structure, income, cost = firm.split()
        firm_dict[name] = int(income) - int(cost)
        if firm_dict.setdefault(name) >= 0:
            total_income = total_income + firm_dict.setdefault(name)
            i += 1
    avarage_dict = {'avarage income': round(total_income/i)}
    firm_list = [firm_dict, avarage_dict]

with open('test_7_out.json', 'w') as write_file:
    json.dump(firm_list, write_file)

    js_line = json.dumps(firm_list)
    print(f'Итог вычеслений: {js_line}')