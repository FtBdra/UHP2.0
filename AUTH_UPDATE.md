## 🔐 Sistem Autentifikasi UHP - Update Fitur Registrasi

### Fitur Baru yang Ditambahkan:

#### 1. **Halaman Registrasi** (`register.html`)
   - Form pendaftaran akun baru dengan validasi lengkap
   - Field yang dibutuhkan:
     - Nama Lengkap
     - Email (unique check)
     - Password (min 6 karakter)
     - Konfirmasi Password
     - Nama UMKM/Bisnis
     - Sektor Bisnis (dropdown dengan 9 pilihan)
   - Toggle visibility untuk password
   - Auto-login setelah registrasi berhasil

#### 2. **Logika Registrasi** (`js/auth.js`)
   - Fungsi `uhpRegister()` dengan validasi:
     - Email tidak boleh duplikat
     - Password min 6 karakter
     - Semua field wajib diisi
     - Password harus cocok saat konfirmasi
   - User data disimpan di localStorage dengan key `uhp_registered_users`
   - Password di-hash menggunakan SHA-256 untuk keamanan

#### 3. **Login Enhanced** (`js/auth.js`)
   - Fungsi login sekarang mendukung user custom (hasil registrasi)
   - Menggunakan helper `getAllUsers()` untuk cek semua user (demo + registered)

#### 4. **UI Updates**
   - **Login Page**: Tambah link "Belum punya akun? Daftar di sini"
   - **Styling**: File `register.css` untuk styling form registrasi
   - Design konsisten dengan login page (dark theme, gradients, animations)

### Cara Menggunakan:

1. **Daftar Akun Baru**:
   - Buka `register.html`
   - Isi semua form
   - Klik "Daftar Akun"
   - Auto login & redirect ke dashboard

2. **Login**:
   - Bisa pakai akun demo (lihat di login.html)
   - Atau pakai akun yang baru dibuat
   - Redirect ke dashboard

### Data Storage:

**Demo Users** (di `data.js`):
- andi@uhp.id / andi123
- zaky@uhp.id / zaky123
- (+ 4 akun demo lainnya)

**Registered Users** (di localStorage):
- Disimpan dengan key `uhp_registered_users`
- Format: JSON array
- Persistent sampai user clear localStorage

### Session Management:

- Session key: `uhp_session`
- Durasi: 24 jam
- Auto-clear saat logout
- Perjalanan ke dashboard/login auto-redirect jika sudah/belum login

### Validasi & Security:

✅ Email uniqueness check  
✅ Password hashing (SHA-256)  
✅ Password confirmation  
✅ Min 6 karakter password  
✅ Session expiration (24 jam)  
✅ CSRF protection (form-based)  

### Next Steps (Optional):

- Backend API integration untuk persistent storage
- Email verification
- Password reset flow
- Social login (Google, GitHub)
- Two-factor authentication (2FA)
