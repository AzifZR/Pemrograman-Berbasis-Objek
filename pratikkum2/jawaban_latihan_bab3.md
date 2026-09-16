# Latihan Bab 3 - Eksepsi

**1. Mengapa sebuah program perlu memiliki mekanisme penanganan error? Jelaskan dampaknya jika error tidak ditangani dengan baik!**
Mekanisme penanganan error (exception handling) diperlukan agar program tidak berhenti secara mendadak (crash) ketika terjadi kesalahan tak terduga, seperti input salah atau file tidak ditemukan. Dampak jika tidak ditangani: program langsung *force close* sehingga data pengguna bisa hilang, pengalaman pengguna (UX) menjadi buruk, dan celah keamanan sistem bisa terekspos lewat pesan error internal (stack trace) yang bocor ke layar pengguna.

**2. Jelaskan keuntungan penggunaan custom exception dibandingkan hanya menggunakan exception bawaan Python!**
Keuntungan custom exception:
- **Spesifik:** Nama error lebih deskriptif sesuai konteks bisnis aplikasi (misal `SaldoKurangError` lebih jelas daripada sekadar `ValueError`).
- **Pemisahan Logika:** Mempermudah programmer menangkap error tertentu tanpa tidak sengaja menangkap error lain yang sejenis.
- **Data Tambahan:** Custom exception bisa menyimpan data/atribut tambahan (misal sisa saldo dan batas minimum) untuk diolah saat error ditangkap.

**3. Jelaskan cara kerja blok try, except, dan finally dalam penanganan error pada Python!**
- `try`: Blok ini berisi kode utama yang mungkin menimbulkan error/eksepsi. Python akan mencoba mengeksekusinya terlebih dahulu.
- `except`: Jika terjadi error di blok `try`, eksekusi akan langsung melompat ke blok `except` ini untuk menangani error tersebut (mencegah program crash).
- `finally`: Blok ini **selalu** dieksekusi pada akhirnya, baik terjadi error maupun tidak. Biasanya digunakan untuk "bersih-bersih", seperti menutup file, menutup koneksi database, atau melepaskan resource.

**4. Skenario Kesalahan (OverflowError, FileExistsError) bertahap**
Terdapat pada file `skenario_error.py`.
