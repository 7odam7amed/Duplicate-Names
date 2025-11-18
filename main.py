import pandas as pd

# قراءة الملفات
df1 = pd.read_excel("E:/Python Beginners/travel/26e.xlsx")
df2 = pd.read_excel("E:/Python Beginners/travel/26s.xlsx")
df3 = pd.read_excel("E:/Python Beginners/travel/7e.xlsx")
df4 = pd.read_excel("E:/Python Beginners/travel/7s.xlsx")

# تنظيف أسماء الأعمدة: إزالة المسافات من البداية والنهاية
for df in [df1, df2, df3, df4]:
    df.columns = df.columns.str.strip()

# توحيد اسم العمود
df1 = df1.rename(columns={"اسم الطالب رباعيا باللغة العربية": "اسم الطالب"})
df2 = df2.rename(columns={"اسم الطالب رباعيا باللغة العربية": "اسم الطالب"})
df3 = df3.rename(columns={"اسم الطالب رباعيا": "اسم الطالب"})
df4 = df4.rename(columns={"اسم الطالب رباعيا باللغة العربية": "اسم الطالب"})

# دمج الملفات
all1 = pd.concat([df1, df2])
all2 = pd.concat([df3, df4])
all_students = pd.concat([all1, all2])

# تأكد من الأعمدة بعد الدمج
print("أعمدة بعد الدمج:", all_students.columns)

# استخراج المكررات
duplicates = all_students[all_students.duplicated(subset="اسم الطالب", keep=False)]

# إزالة التكرار في ملف الإخراج
unique_names = duplicates["اسم الطالب"].drop_duplicates()

# حفظ المكررات في ملف نصي
with open("duplicates.txt", "w", encoding="utf-8") as file:
    for name in unique_names:
        file.write(str(name) + "\n")

print("✔ تم حفظ الأسماء المكررة في ملف duplicates.txt")
