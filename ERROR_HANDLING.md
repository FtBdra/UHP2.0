## 🛡️ Error Handling Documentation - Sistem Autentifikasi

### Overview
Sistem autentifikasi UHP memiliki error handling yang komprehensif di 3 layer:
1. **Client-side validation** (register.html & login.html)
2. **Server-side validation** (auth.js)
3. **UI Feedback** (styling & UX)

---

## Error Handling Registrasi

### Field Validation (Client-side)

#### 1. Nama Lengkap
- ❌ Tidak boleh kosong
- ❌ Minimal 3 karakter
- ❌ Maksimal 50 karakter

#### 2. Email
- ❌ Tidak boleh kosong
- ❌ Format harus valid (xxx@domain.com)
- ❌ Maksimal 100 karakter
- ❌ Email tidak bisa duplikat (checked di server)

#### 3. Password
- ❌ Tidak boleh kosong
- ❌ Minimal 6 karakter
- ❌ Maksimal 100 karakter
- ❌ Harus cocok dengan konfirmasi password

#### 4. Konfirmasi Password
- ❌ Tidak boleh kosong
- ❌ Harus sama persis dengan password

#### 5. Nama UMKM/Bisnis
- ❌ Tidak boleh kosong
- ❌ Minimal 3 karakter
- ❌ Maksimal 100 karakter

#### 6. Sektor Bisnis
- ❌ Harus dipilih dari dropdown
- ❌ Hanya validasi sector yang terdaftar diterima

---

## Error Handling Login

### Field Validation

#### Email
- ❌ Tidak boleh kosong
- ❌ Format harus valid

#### Password
- ❌ Tidak boleh kosong
- ❌ Case-sensitive

### Login Errors
- ❌ Email atau password salah (tidak memberikan info lebih untuk keamanan)

---

## Error Messages

Semua error messages dimulai dengan emoji ❌ untuk konsistensi visual:

### Registrasi
```
❌ Nama lengkap tidak boleh kosong.
❌ Nama minimal 3 karakter.
❌ Nama maksimal 50 karakter.
❌ Email tidak boleh kosong.
❌ Format email tidak valid (contoh: nama@domain.com).
❌ Email "<email>" sudah terdaftar. Gunakan email lain atau login di sini.
❌ Password tidak boleh kosong.
❌ Password minimal 6 karakter.
❌ Password maksimal 100 karakter.
❌ Konfirmasi password tidak boleh kosong.
❌ Password tidak cocok. Pastikan kedua password sama.
❌ Nama UMKM/Bisnis tidak boleh kosong.
❌ Nama UMKM/Bisnis minimal 3 karakter.
❌ Nama UMKM/Bisnis maksimal 100 karakter.
❌ Pilih sektor bisnis.
❌ Semua field harus diisi dengan benar.
❌ Terjadi kesalahan saat mendaftar. Coba lagi.
```

### Login
```
❌ Email tidak boleh kosong.
❌ Password tidak boleh kosong.
❌ Email dan password harus diisi.
❌ Email atau password salah. Cek kembali.
❌ Terjadi kesalahan. Coba lagi.
```

---

## UI Feedback

### Error Display
- Error message muncul dengan animasi `slideDown` (300ms)
- Background berwarna merah muda (critical-dim)
- Teks berwarna merah (critical)
- Border 1px dengan opacity 0.3

### Button State
- Tombol disabled saat loading
- Spinner icon berputar selama proses
- Button kembali enabled setelah error atau sukses

### Input Field States (Optional - untuk future enhancement)
- `.error` class: Border merah, background dim merah
- `.success` class: Border hijau, background dim hijau
- Helper text bisa ditampilkan di bawah field

---

## Validation Flow Diagram

### Registrasi
```
User Input
    ↓
Client Validation (register.html)
    ↓
    ├─ Ada Error? → Show Error Message + Return
    │
    └─ OK → Proceed
         ↓
    Server Validation (auth.js)
         ↓
         ├─ Ada Error? → Return Error (termasuk duplikat email)
         │   ↓
         │   Show Error Message
         │
         └─ OK → Create User + Auto Login → Redirect Dashboard
```

### Login
```
User Input
    ↓
Client Validation (login.html)
    ↓
    ├─ Ada Error? → Show Error Message + Return
    │
    └─ OK → Proceed
         ↓
    Server Validation (auth.js)
         ↓
         ├─ Invalid? → Return Error
         │   ↓
         │   Show Error Message
         │
         └─ Valid → Create Session → Redirect Dashboard
```

---

## Security Features

✅ **Password Hashing**: SHA-256 sebelum disimpan  
✅ **Email Validation**: Format regex check  
✅ **Unique Email**: Prevent duplicate accounts  
✅ **Session Expiration**: 24 jam auto-logout  
✅ **Input Sanitization**: `.trim()` untuk semua input  
✅ **Password Confirmation**: Match validation sebelum submit  
✅ **Error Messages**: Tidak memberikan info sensitif (contoh: login error tidak bilang email mana yang salah)

---

## Future Enhancements

- [ ] Real-time field validation dengan visual feedback
- [ ] Password strength indicator
- [ ] Email verification before account activation
- [ ] Rate limiting untuk login attempts
- [ ] Two-factor authentication (2FA)
- [ ] Password reset flow
- [ ] Account recovery options
- [ ] Backend API integration
- [ ] Database persistence
- [ ] HTTPS enforcement
