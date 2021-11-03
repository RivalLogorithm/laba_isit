import numpy as np
import random
import xlsxwriter
products = ["Хлеб", "Яйцо", "Колбаса", "Сыр", "Молоко", "Кофе", "Печенье", "Макароны", "Курица", "Конфеты"]
data = np.zeros((30, 10), dtype=str)
#temp_list = []
finally_data = []
# for i in range(0, 30):
#     for j in range(0, random.randint(3, 10)):
#         pr = products[random.randint(0, 9)]
#         while pr in data[i]:
#             pr = products[random.randint(0, 9)]
#         data[i][j] = pr

for i in range(0, 30):
    temp_list = []
    for j in range(0, random.randint(2, 7)):
        pr = products[random.randint(0, 9)]
        while pr in temp_list:
            pr = products[random.randint(0, 9)]
        temp_list.append(pr)
    finally_data.append(temp_list)

print(finally_data)

with xlsxwriter.Workbook('test.xlsx') as workbook:
    worksheet = workbook.add_worksheet()

    for row_num, data in enumerate(finally_data):
        worksheet.write_row(row_num, 0, data)
# print(data)