file_open = open("README", encoding='utf-8')
file_write = open('README_1', 'w', encoding='utf-8')

for text in file_open.readlines():
    file_write.write(text)
file_open.close()
file_write.close()

