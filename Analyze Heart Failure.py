import pandas as pd

df = pd.read_csv("heart_failure_clinical_records_dataset.csv")

print("Berikut ini adalah lima data teratas:")
print(df.head())

print("\n Info dataset:")
print(df.info())

print("\n Summary of dataset:")
print(df.describe())

import matplotlib.pyplot as plt

#Bagian ini untuk memplot banyak laki-laki dan perempuan yang meninggal akibat gagal jantung
df_sex_death_proportion = df.groupby("sex")["DEATH_EVENT"].sum().reset_index()
sex_death_dict = {"sex": ["female", "male"], "death_count": [df_sex_death_proportion["DEATH_EVENT"][0], df_sex_death_proportion["DEATH_EVENT"][1]]}
sex_death_proportion = pd.DataFrame(sex_death_dict)

#Bagian ini untuk memplot banyak orang anemia dan tidak anemia yang meninggal akibat gagal jantung
df_anaemia_death_proportion = df.groupby("anaemia")["DEATH_EVENT"].sum().reset_index()
anaemia_death_dict = {"kategori": ["Tidak Anaemia", "Anaemia"], "death_count": [df_anaemia_death_proportion["DEATH_EVENT"][0], df_anaemia_death_proportion["DEATH_EVENT"][1]]}
anaemia_death_proportion = pd.DataFrame(anaemia_death_dict)

#Bagian ini untuk memplot banyak orang diabetes dan tidak diabetes yang meninggal akibat gagal jantung
df_diabetes_death_proportion = df.groupby("diabetes")["DEATH_EVENT"].sum().reset_index()
diabetes_death_dict = {"kategori": ["Tidak Diabetes", "Diabetes"], "death_count": [df_sex_death_proportion["DEATH_EVENT"][0], df_diabetes_death_proportion["DEATH_EVENT"][1]]}
diabetes_death_proportion = pd.DataFrame(diabetes_death_dict)

#Bagian ini untuk memplot banyak perokok dan tidak perokok yang meninggal akibat gagal jantung
df_smoking_death_proportion = df.groupby("smoking")["DEATH_EVENT"].sum().reset_index()
smoking_death_dict = {"kategori": ["Bukan Perokok", "Perokok"], "death_count": [df_smoking_death_proportion["DEATH_EVENT"][0], df_smoking_death_proportion["DEATH_EVENT"][1]]}
smoking_death_proportion = pd.DataFrame(smoking_death_dict)

fig, (ax1, ax2, ax3, ax4) = plt.subplots(1,4)
ax1.pie(sex_death_proportion["death_count"], labels = sex_death_proportion["sex"], autopct = '%1.2f%%')
ax2.pie(anaemia_death_proportion["death_count"], labels = anaemia_death_proportion["kategori"], autopct = '%1.2f%%')
ax3.pie(diabetes_death_proportion["death_count"], labels = diabetes_death_proportion["kategori"], autopct = '%1.2f%%')
ax4.pie(smoking_death_proportion["death_count"], labels = smoking_death_proportion["kategori"], autopct = '%1.2f%%')

plt.suptitle("Presentase Kematian Akibat Gagal Jantung", fontsize = 20)
plt.figure(1)

#Bagian ini untuk menenujukkan distribusi kematian akibat gagal jantung berdasarkan umur dan jenis kelamin
age_death_female = []
for i in range(299):
    if df["DEATH_EVENT"][i] == 1 and df["sex"][i] == 0:
        age_death_female.append(df["age"][i])

age_death_male = []
for i in range(299):
    if df["DEATH_EVENT"][i] == 1 and df["sex"][i] == 1:
        age_death_male.append(df["age"][i])

plt.figure(2)
plt.hist([age_death_female,age_death_male], bins=15, ec="black", stacked='True')
plt.title("Distribusi Kematian Akibat Gagal Jantung")
plt.ylabel("Jumlah Orang")
plt.xlabel("Umur")
plt.legend(["Female","Male"])

#Bagian ini untuk menenujukkan distribusi kematian akibat gagal jantung berdasarkan umur
plt.figure(3)
age_death = []
for i in range(299):
    if df["DEATH_EVENT"][i] ==1:
        age_death.append(df["age"][i])

plt.hist(age_death, bins=15, ec="black")
plt.title("Distribusi Kematian Akibat Gagal Jantung")
plt.ylabel("Jumlah Orang")
plt.xlabel("Umur")

#Bagian ini untuk menanpilkan boxplot untuk data kematian berdasarkan umur
plt.figure(4)
plt.boxplot(age_death)
plt.title("Boxplot untuk Data Kematian Berdasarkan Umur")
plt.ylabel("Umur")
plt.show()
