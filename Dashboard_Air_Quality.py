import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st
import seaborn as sns

# Load Data
tiantan_df = pd.read_csv("tiantan_last.csv")

tiantan_df.sort_values(by="year", inplace=True)
tiantan_df['year'] = pd.to_datetime(tiantan_df['year'], format='%Y')

# Sidebar with author information
st.sidebar.header("Author Information")
st.sidebar.text("Name: Muhammad Zia Ulhaq")
st.sidebar.text("Email: ziaswatfbicia@gmail.com")
st.sidebar.text("Bangkit ID: M322D4KY2896")


# Title
st.header('Proyek Analisis Data: Air Quality Dataset (PRSA Data Tiantan)')

# Baca data dari file CSV
data = pd.read_csv("tiantan_last.csv")

# Tampilkan data di dalam aplikasi
st.write(data)

st.write('''
Data diatas merupakan data kualitas udara pada Kota Tiantan pada tahun 2013-2017 dan ditambakan colom data baru.
''')


st.write('''
Dari sumber bacaan https://waqi.info/#/c/6.892/0/2z dapat diketahui bahwa untuk Air Pullution Level dapat di tentukan berdasarkan nilai PM, oleh kerena itu pada dataset akan ditambahkan variabel baru yaitu "Air Pollution Level" yang berisi:
  - Good (untuk nilai PM 0-50)
  - Moderate (untuk nilai PM 51-100)
  - UfSG (Unhealty for sensitive groups)(Untuk nilai PM 101-150)
  - Unhealty (Untuk Nilai PM 151-200)
  - Very Unhealty (Untuk nilai PM 201-300)
  - Hazardous (Untuk nilai PM 300+)
''')

st.header('''
Seberapa besar proporsi masing-masing tingkat polusi udara di Kota Tiantan?
''')

# Subheader
st.subheader("Proporsi level polusi bersarkan PM2.5")

# Visualisasi
air_pollution_level_counts = tiantan_df['Air Pollution Level (PM2.5)'].value_counts()

# Membuat bar plot
fig, ax = plt.subplots()
ax.bar(air_pollution_level_counts.index, air_pollution_level_counts.values, color='skyblue')

# Menambahkan label dan judul
ax.set_xlabel('Air Pollution Level')
ax.set_ylabel('Frequency')
ax.set_title('Proportion of Air Pollution Levels From PM2.5')
plt.xticks(rotation=45)  # Rotasi label sumbu x agar mudah dibaca

# Menampilkan bar plot di Streamlit
st.pyplot(fig)

st.write('''
Dari output diatas dapat dilihat bahwa proporsi level polusi udara berdasarkan PM2.5 Good Kota Tiantan mencapai nilai > 15.000, moderate  > 8000, UfSG > 4000, Unhealty > 2000, Verry Unhealty > 2000 dan Hazardous < 2000 
''')

# Hitung frekuensi setiap tingkat polusi udara
air_pollution_level_counts = tiantan_df['Air Pollution Level (PM2.5)'].value_counts()

# Hitung total frekuensi semua tingkat polusi udara
total_counts = air_pollution_level_counts.sum()

# Bagi frekuensi masing-masing tingkat polusi udara dengan total frekuensi
proporsi_tingkat_polusi = air_pollution_level_counts / total_counts

# Tampilkan proporsi masing-masing tingkat polusi udara di Streamlit
st.write('Proporsi Tingkat Polusi Udara berdasarkan PM2.5:')
st.write(proporsi_tingkat_polusi)

# Subheader
st.subheader("Proporsi level polusi bersarkan PM10")

# Visualisasi
air_pollution_level_counts = tiantan_df['Air Pollution Level (PM10)'].value_counts()

# Membuat bar plot
fig, ax = plt.subplots()
ax.bar(air_pollution_level_counts.index, air_pollution_level_counts.values, color='skyblue')

# Menambahkan label dan judul
ax.set_xlabel('Air Pollution Level')
ax.set_ylabel('Frequency')
ax.set_title('Proportion of Air Pollution Levels From PM10')
plt.xticks(rotation=45)  # Rotasi label sumbu x agar mudah dibaca

# Menampilkan bar plot di Streamlit
st.pyplot(fig)

st.write('''
Sedangkan dari output diatas dapat dilihat bahwa proporsi level polusi udara berdasarkan PM10 Good Kota Tiantan mencapai nilai > 10.000, moderate  > 8000, UfSG > 6000, Unhealty > 4000, Verry Unhealty > 2000 dan Hazardous < 2000 
''')

# Hitung frekuensi setiap tingkat polusi udara
air_pollution_level_counts = tiantan_df['Air Pollution Level (PM10)'].value_counts()

# Hitung total frekuensi semua tingkat polusi udara
total_counts = air_pollution_level_counts.sum()

# Bagi frekuensi masing-masing tingkat polusi udara dengan total frekuensi
proporsi_tingkat_polusi = air_pollution_level_counts / total_counts

# Tampilkan proporsi masing-masing tingkat polusi udara di Streamlit
st.write('Proporsi Tingkat Polusi Udara Berdasarkan PM10:')
st.write(proporsi_tingkat_polusi)

st.header('''
Variabel apa yang paling berpengaruh dalam menentukan level polusi udara Kota Tiantan?
''')

st.subheader("Visualisasi Berdasarkan SO2")

st.write('''
Boxplot 
''')

# Membuat boxplot
fig, ax = plt.subplots(figsize=(10, 6))
sns.boxplot(x='Air Pollution Level (PM2.5)', y='SO2', data=tiantan_df, palette='Set3', ax=ax)
ax.set_xlabel('Air Pollution Level')
ax.set_ylabel('SO2')
ax.set_title('Boxplot of SO2 by Air Pollution Level')
ax.set_xticklabels(ax.get_xticklabels(), rotation=45)
plt.tight_layout()

# Menampilkan boxplot di Streamlit
st.pyplot(fig)

st.write('''
Barplot 
''')

# Membuat Barplot
fig, ax = plt.subplots(figsize=(10, 6))
sns.barplot(x='Air Pollution Level (PM2.5)', y='SO2', data=tiantan_df, palette='Set3', ci=None, ax=ax)
ax.set_xlabel('Air Pollution Level')
ax.set_ylabel('SO2')
ax.set_title('Barplot of SO2 by Air Pollution Level')
ax.set_xticklabels(ax.get_xticklabels(), rotation=45)
plt.tight_layout()

# Menampilkan barplot di Streamlit
st.pyplot(fig)

st.subheader("Visualisasi Berdasarkan NO2")

st.write('''
Boxplot 
''')

# Membuat boxplot
fig, ax = plt.subplots(figsize=(10, 6))
sns.boxplot(x='Air Pollution Level (PM2.5)', y='NO2', data=tiantan_df, palette='Set3', ax=ax)
ax.set_xlabel('Air Pollution Level')
ax.set_ylabel('NO2')
ax.set_title('Boxplot of NO2 by Air Pollution Level')
ax.set_xticklabels(ax.get_xticklabels(), rotation=45)
plt.tight_layout()

# Menampilkan boxplot di Streamlit
st.pyplot(fig)

st.write('''
Barplot 
''')

# Membuat Barplot
fig, ax = plt.subplots(figsize=(10, 6))
sns.barplot(x='Air Pollution Level (PM2.5)', y='NO2', data=tiantan_df, palette='Set3', ci=None, ax=ax)
ax.set_xlabel('Air Pollution Level')
ax.set_ylabel('NO2')
ax.set_title('Barplot of NO2 by Air Pollution Level')
ax.set_xticklabels(ax.get_xticklabels(), rotation=45)
plt.tight_layout()

# Menampilkan barplot di Streamlit
st.pyplot(fig)

st.subheader("Visualisasi Berdasarkan CO")

st.write('''
Boxplot 
''')

# Membuat boxplot
fig, ax = plt.subplots(figsize=(10, 6))
sns.boxplot(x='Air Pollution Level (PM2.5)', y='CO', data=tiantan_df, palette='Set3', ax=ax)
ax.set_xlabel('Air Pollution Level')
ax.set_ylabel('CO')
ax.set_title('Boxplot of CO by Air Pollution Level')
ax.set_xticklabels(ax.get_xticklabels(), rotation=45)
plt.tight_layout()

# Menampilkan boxplot di Streamlit
st.pyplot(fig)

st.write('''
Barplot 
''')

# Membuat Barplot
fig, ax = plt.subplots(figsize=(10, 6))
sns.barplot(x='Air Pollution Level (PM2.5)', y='CO', data=tiantan_df, palette='Set3', ci=None, ax=ax)
ax.set_xlabel('Air Pollution Level')
ax.set_ylabel('CO')
ax.set_title('Barplot of CO by Air Pollution Level')
ax.set_xticklabels(ax.get_xticklabels(), rotation=45)
plt.tight_layout()

# Menampilkan barplot di Streamlit
st.pyplot(fig)

st.subheader("Visualisasi Berdasarkan O3")

st.write('''
Boxplot 
''')

# Membuat boxplot
fig, ax = plt.subplots(figsize=(10, 6))
sns.boxplot(x='Air Pollution Level (PM2.5)', y='O3', data=tiantan_df, palette='Set3', ax=ax)
ax.set_xlabel('Air Pollution Level')
ax.set_ylabel('O3')
ax.set_title('Boxplot of O3 by Air Pollution Level')
ax.set_xticklabels(ax.get_xticklabels(), rotation=45)
plt.tight_layout()

# Menampilkan boxplot di Streamlit
st.pyplot(fig)

st.write('''
Barplot 
''')

# Membuat Barplot
fig, ax = plt.subplots(figsize=(10, 6))
sns.barplot(x='Air Pollution Level (PM2.5)', y='O3', data=tiantan_df, palette='Set3', ci=None, ax=ax)
ax.set_xlabel('Air Pollution Level')
ax.set_ylabel('O3')
ax.set_title('Barplot of O3 by Air Pollution Level')
ax.set_xticklabels(ax.get_xticklabels(), rotation=45)
plt.tight_layout()

# Menampilkan barplot di Streamlit
st.pyplot(fig)

st.subheader("Visualisasi Berdasarkan TEMP")

st.write('''
Boxplot 
''')

# Membuat boxplot
fig, ax = plt.subplots(figsize=(10, 6))
sns.boxplot(x='Air Pollution Level (PM2.5)', y='TEMP', data=tiantan_df, palette='Set3', ax=ax)
ax.set_xlabel('Air Pollution Level')
ax.set_ylabel('TEMP')
ax.set_title('Boxplot of TEMP by Air Pollution Level')
ax.set_xticklabels(ax.get_xticklabels(), rotation=45)
plt.tight_layout()

# Menampilkan boxplot di Streamlit
st.pyplot(fig)

st.write('''
Barplot 
''')

# Membuat Barplot
fig, ax = plt.subplots(figsize=(10, 6))
sns.barplot(x='Air Pollution Level (PM2.5)', y='TEMP', data=tiantan_df, palette='Set3', ci=None, ax=ax)
ax.set_xlabel('Air Pollution Level')
ax.set_ylabel('TEMP')
ax.set_title('Barplot of TEMP by Air Pollution Level')
ax.set_xticklabels(ax.get_xticklabels(), rotation=45)
plt.tight_layout()

# Menampilkan barplot di Streamlit
st.pyplot(fig)

st.subheader("Visualisasi Berdasarkan PRES")

st.write('''
Boxplot 
''')

# Membuat boxplot
fig, ax = plt.subplots(figsize=(10, 6))
sns.boxplot(x='Air Pollution Level (PM2.5)', y='PRES', data=tiantan_df, palette='Set3', ax=ax)
ax.set_xlabel('Air Pollution Level')
ax.set_ylabel('PRES')
ax.set_title('Boxplot of PRES by Air Pollution Level')
ax.set_xticklabels(ax.get_xticklabels(), rotation=45)
plt.tight_layout()

# Menampilkan boxplot di Streamlit
st.pyplot(fig)

st.write('''
Barplot 
''')

# Membuat Barplot
fig, ax = plt.subplots(figsize=(10, 6))
sns.barplot(x='Air Pollution Level (PM2.5)', y='PRES', data=tiantan_df, palette='Set3', ci=None, ax=ax)
ax.set_xlabel('Air Pollution Level')
ax.set_ylabel('PRES')
ax.set_title('Barplot of PRES by Air Pollution Level')
ax.set_xticklabels(ax.get_xticklabels(), rotation=45)
plt.tight_layout()

# Menampilkan barplot di Streamlit
st.pyplot(fig)

st.subheader("Visualisasi Berdasarkan DEWP")

st.write('''
Boxplot 
''')

# Membuat boxplot
fig, ax = plt.subplots(figsize=(10, 6))
sns.boxplot(x='Air Pollution Level (PM2.5)', y='DEWP', data=tiantan_df, palette='Set3', ax=ax)
ax.set_xlabel('Air Pollution Level')
ax.set_ylabel('DEWP')
ax.set_title('Boxplot of DEWP by Air Pollution Level')
ax.set_xticklabels(ax.get_xticklabels(), rotation=45)
plt.tight_layout()

# Menampilkan boxplot di Streamlit
st.pyplot(fig)

st.write('''
Barplot 
''')

# Membuat Barplot
fig, ax = plt.subplots(figsize=(10, 6))
sns.barplot(x='Air Pollution Level (PM2.5)', y='DEWP', data=tiantan_df, palette='Set3', ci=None, ax=ax)
ax.set_xlabel('Air Pollution Level')
ax.set_ylabel('DEWP')
ax.set_title('Barplot of DEWP by Air Pollution Level')
ax.set_xticklabels(ax.get_xticklabels(), rotation=45)
plt.tight_layout()

# Menampilkan barplot di Streamlit
st.pyplot(fig)

st.subheader("Visualisasi Berdasarkan RAIN")

st.write('''
Boxplot 
''')

# Membuat boxplot
fig, ax = plt.subplots(figsize=(10, 6))
sns.boxplot(x='Air Pollution Level (PM2.5)', y='RAIN', data=tiantan_df, palette='Set3', ax=ax)
ax.set_xlabel('Air Pollution Level')
ax.set_ylabel('RAIN')
ax.set_title('Boxplot of RAIN by Air Pollution Level')
ax.set_xticklabels(ax.get_xticklabels(), rotation=45)
plt.tight_layout()

# Menampilkan boxplot di Streamlit
st.pyplot(fig)

st.write('''
Barplot 
''')

# Membuat Barplot
fig, ax = plt.subplots(figsize=(10, 6))
sns.barplot(x='Air Pollution Level (PM2.5)', y='RAIN', data=tiantan_df, palette='Set3', ci=None, ax=ax)
ax.set_xlabel('Air Pollution Level')
ax.set_ylabel('RAIN')
ax.set_title('Barplot of RAIN by Air Pollution Level')
ax.set_xticklabels(ax.get_xticklabels(), rotation=45)
plt.tight_layout()

# Menampilkan barplot di Streamlit
st.pyplot(fig)

st.subheader("Visualisasi Berdasarkan WSPM")

st.write('''
Boxplot 
''')

# Membuat boxplot
fig, ax = plt.subplots(figsize=(10, 6))
sns.boxplot(x='Air Pollution Level (PM2.5)', y='WSPM', data=tiantan_df, palette='Set3', ax=ax)
ax.set_xlabel('Air Pollution Level')
ax.set_ylabel('WSPM')
ax.set_title('Boxplot of WSPM by Air Pollution Level')
ax.set_xticklabels(ax.get_xticklabels(), rotation=45)
plt.tight_layout()

# Menampilkan boxplot di Streamlit
st.pyplot(fig)

st.write('''
Barplot 
''')

# Membuat Barplot
fig, ax = plt.subplots(figsize=(10, 6))
sns.barplot(x='Air Pollution Level (PM2.5)', y='WSPM', data=tiantan_df, palette='Set3', ci=None, ax=ax)
ax.set_xlabel('Air Pollution Level')
ax.set_ylabel('WSPM')
ax.set_title('Barplot of WSPM by Air Pollution Level')
ax.set_xticklabels(ax.get_xticklabels(), rotation=45)
plt.tight_layout()

# Menampilkan barplot di Streamlit
st.pyplot(fig)


st.subheader('''
Heatmap Korelasi 
''')

# Memilih kolom-kolom numerik saja
numeric_cols = tiantan_df.select_dtypes(include='number')

# Membuat heatmap
fig, ax = plt.subplots(figsize=(12, 8))
sns.heatmap(numeric_cols.corr(), annot=True, cmap='coolwarm', fmt=".2f", linewidths=.5, ax=ax)
ax.set_title('Heatmap Korelasi Antara Variabel')
plt.tight_layout()

# Menampilkan heatmap di Streamlit
st.pyplot(fig)


st.write('''
Dari output diatas dapat dilihat bahwa variabel CO, NO2, SO2 memiliki korelasi yang kuat  
''')

# Define air_polution_df function
def air_polution_df(df):
    air_polution_df = df.groupby(by=['year']).agg({
        "PM2.5": "mean",
        "PM10": "mean",
        "SO2": "mean",
        "NO2": "mean",
        "CO": "mean",
        "O3": "mean"
    }).sort_values(by=['year'], ascending=True)
    air_polution_df = air_polution_df.reset_index()
    air_polution_df['time'] = air_polution_df["year"].astype(str)
    return air_polution_df

# Define air_polution_graph function
def air_polution_graph(df):
    df = df.sort_values(by='year')  # Ensure DataFrame is sorted by 'year'

    fig, ax = plt.subplots(6, 1, figsize=(16, 48))

    pollutants = ["PM2.5", "PM10", "SO2", "NO2", "CO", "O3"]

    for i, pollutant in enumerate(pollutants):
        ax[i].plot(df['year'].to_numpy(), df[pollutant].to_numpy(), marker='o', linewidth=2, color="#39064B")
        ax[i].tick_params(axis='y', labelsize=20)
        ax[i].tick_params(axis='x', labelsize=20, labelrotation=0)
        ax[i].set_ylabel(pollutant, fontsize=25)
        ax[i].set_title(pollutant, loc="center", fontsize=35)

    st.pyplot(fig)

polusi_pertahun = air_polution_df(tiantan_df)
with st.container():
    st.header("Bagaimana trend polusi udara di Kota Tiantan dalam 5 Tahun tersebut (2013-2017)?")
    air_polution_graph(polusi_pertahun)



st.header('Conculsion')

st.write('''
1. Proporsi level polusi udara condong Good
2. Semua variabel memiliki korelasi antara variabel lainnya 
3. Semua indikator dalam 5 tahun menunjuk trend yang mengalami fluktuasi 
''')