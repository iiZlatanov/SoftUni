data = input()
companies_and_employees_ids = {}

while data != "End":
    split_data = data.split(" -> ")
    company = split_data[0]
    employee_id = split_data[1]
    if company not in companies_and_employees_ids:
        companies_and_employees_ids[company] = [employee_id]
    else:
        companies_and_employees_ids[company] += [employee_id]
    data = input()

for key, value in companies_and_employees_ids.items():
    companies_and_employees_ids[key] = sorted(set(value), key=value.index)

sorted_companies_and_employees_ids = dict(sorted(companies_and_employees_ids.items(), key=lambda x: x[0]))

for companies, employees_ids in sorted_companies_and_employees_ids.items():
    x = "\n-- ".join(employees_ids)
    print(f"{companies}\n-- {x}")
