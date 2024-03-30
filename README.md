# Python5-OOP
# Class MarketingDataETL:
Ini adalah kelas dasar untuk ekstraksi, transformasi, dan penyimpanan data pemasaran.

a. __init__(self, file_path):
Ini adalah metode konstruktor kelas yang menginisialisasi objek MarketingDataETL. Ini menerima file_path sebagai argumen dan mengatur self.file_path ke nilai yang diberikan dan self.data ke None.

b. extract(self):
Metode ini digunakan untuk mengekstrak data dari file CSV yang diberikan di file_path. Ini membaca file CSV ke dalam DataFrame Pandas. Kemudian mencetak data sebelum transformasi dan mengembalikan DataFrame.

c. transform(self):
Metode ini memeriksa apakah ada kolom 'purchase_date' dalam DataFrame. Jika ada, ia mengubah kolom tersebut menjadi tipe data datetime Pandas, menghapus baris dengan nilai yang hilang dalam kolom 'purchase_date', mencetak data setelah transformasi, dan mengembalikan DataFrame yang diubah.

d. store(self, output_file_path):
Metode ini digunakan untuk menyimpan DataFrame ke dalam file CSV. Jika self.data tidak None, itu mencoba menyimpan DataFrame sebagai file CSV di output_file_path. Jika tidak, itu mencetak pesan bahwa tidak ada data yang tersedia untuk disimpan.

# Class TargetedMarketingETL (subclass of MarketingDataETL):
Ini adalah subkelas dari MarketingDataETL yang menambahkan fungsi segmentasi pelanggan.

a. segment_customers(self):
Metode ini menentukan segmen pengeluaran pelanggan berdasarkan jumlah yang dihabiskan. Ini menambahkan kolom 'spending_segment' ke DataFrame dengan segmen yang sesuai.

b. transform(self):
Metode ini menerapkan transformasi yang sama seperti di kelas dasar (MarketingDataETL) dan kemudian memanggil segment_customers untuk melakukan segmentasi pelanggan tambahan.

c. store_segmented_data(self, output_file_path):
Metode ini digunakan untuk menyimpan DataFrame yang telah ditransformasi dan disegmentasi ke dalam file CSV. Ini memanggil metode store dari kelas dasar untuk menyimpan data.
