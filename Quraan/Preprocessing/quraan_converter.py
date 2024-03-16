import pandas as pd
file = open("quran_k.txt", 'r', encoding='utf-8')

file_content = file.read()

file_content = file_content.replace("أ" , "ا")
file_content = file_content.replace("إ" , "ا")
file_content = file_content.replace("آ" , "ا")
file_content = file_content.replace("ة" , "ه")

df = pd.read_csv(file_content, sep='|', header=None, names=['Sorah_num', 'Ayah_num', 'Ayah text'])

print
