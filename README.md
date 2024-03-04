# Proyek Analisis Data: Air Quality Dataset (PRSA Data Tiantan)

**Nama:** Muhammad Zia Ulhaq  
**Email:** ziaswatfbicia@gmail  
**ID Dicoding:** zia1705  

## Deskripsi Proyek
Proyek ini bertujuan untuk menganalisis kualitas udara di Kota Tiantan menggunakan dataset Air Quality (PRSA Data Tiantan). Analisis dilakukan untuk mengetahui proporsi tingkat polusi udara, variabel yang mempengaruhi tingkat polusi udara, serta tren kualitas udara Kota Tiantan selama periode waktu tertentu.

## Langkah-langkah Proyek

### 1. Menentukan Pertanyaan Bisnis
- Seberapa besar proporsi masing-masing tingkat polusi udara di Kota Tiantan?
- Variabel apa yang paling berpengaruh dalam menentukan level polusi udara Kota Tiantan?
- Bagaimana trend kualitas udara Kota Tiantan?

### 2. Data Wrangling
- Gathering Data: Mengunduh dataset PRSA Data Tiantan dari sumber online.
- Assessing Data: Memeriksa informasi dan keberadaan missing value dalam dataset.
- Cleaning Data: Mengubah tipe data, menghapus kolom yang tidak diperlukan, mengatasi missing value dengan menghapus baris tertentu, serta mengisi missing value dengan metode interpolasi linear.

### 3. Exploratory Data Analysis (EDA)
- Melihat deskriptif data, distribusi data, dan korelasi antar variabel.
- Menambahkan variabel baru untuk mengkategorikan tingkat polusi udara berdasarkan nilai PM2.5 dan PM10.
- Visualisasi proporsi tingkat polusi udara, pengaruh variabel terhadap tingkat polusi udara, dan korelasi antar variabel.

### 4. Visualization & Explanatory Analysis
- Melakukan visualisasi berdasarkan variabel-variabel utama seperti SO2, NO2, CO, O3, TEMP, PRES, DEWP, RAIN, dan WSPM.
- Menggunakan boxplot dan barplot untuk melihat pengaruh variabel terhadap tingkat polusi udara.
- Membuat heatmap untuk melihat korelasi antar variabel dan menghitung korelasi dengan tingkat polusi udara (PM2.5).

### 5. Analisis Trend
- Menganalisis tren kualitas udara Kota Tiantan selama periode waktu tertentu, misalnya dalam 5 tahun terakhir.

## Kesimpulan
- Proporsi tertinggi tingkat polusi udara di Kota Tiantan adalah "Good" sebesar 45,1%, sementara yang paling rendah adalah "Hazardous" sebesar 2,3% dalam 5 tahun terakhir.
- Variabel yang paling berpengaruh dalam menentukan level polusi udara Kota Tiantan adalah "CO", jika menganggap variabel PM2.5 dan PM10 sebagai pembentuk variabel baru "tingkat polusi udara".
- Trend kualitas udara Kota Tiantan mengalami fluktuasi selama periode 5 tahun terakhir.

## File Proyek
- **Dataset:** PRSA_Data_Tiantan_20130301-20170228.csv
- **Notebook:** Analisis_Data_Tiantan.ipynb
- **Output:** tiantan_clean.csv, tiantan_last.csv

## Link Dashboard
- https://ziaair.streamlit.app/

## Referensi
- Sumber dataset: [PRSA Data Tiantan](https://raw.githubusercontent.com/marceloreis/HTI/master/PRSA_Data_20130301-20170228/PRSA_Data_Tiantan_20130301-20170228.csv)
- Sumber informasi tentang kualitas udara: [waqi.info](https://waqi.info/#/c/6.892/0/2z)
