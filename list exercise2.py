first_names = ["Ainsley", "Ben", "Chani", "Depak"]
preffered_size = ["Small", "Large", "Medium"]

preffered_size.append("Medium")

print(preffered_size)

customer_data = [["Ainsley","Small",True],
                 ["Ben","Large",False],
                 ["Chani","Medium",True],
                 ["Depak","Medium",False]]
customer_data2 = [["Amit","Large", True ],
                  ["Karim","X-Large", False]]
print(customer_data)

customer_data[2] = "Chani", "Medium", False
print(customer_data)

del customer_data[1]
print(customer_data)

customer_data_final = customer_data + customer_data2

print(customer_data_final)