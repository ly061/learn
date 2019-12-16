import xlwt
# 创建workboook对象
workbook = xlwt.Workbook(encoding='utf-8', style_compression=0)
# 创建一个sheet对象，一个sheet对应excel文件中一张表格
sheet = workbook.add_sheet('test_excel', cell_overwrite_ok=True)               # cell_overwrite_ok 是否能够覆盖单元格
# 向表中添加数据
li = ["ly", "ly01", "ly02", "ly03", "ly04"]
for i in range(5):
    sheet.write(0, i, li[i])

workbook.save(r"test_excel.csv")


import csv
with open('./test_excel.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(["a", "b", "c"])
    writer.writerow(["1", "2", "3"])
    writer.writerow(["4", "5", "6"])


with open('./test_excel.csv', 'r') as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)
