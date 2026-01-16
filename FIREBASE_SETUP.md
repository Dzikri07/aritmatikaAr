# 🚀 Setup Firebase Hosting untuk Barisan Aritmatika AR

## Langkah 1: Install Firebase CLI
```bash
npm install -g firebase-tools
```

## Langkah 2: Login ke Firebase
```bash
firebase login
```
- Akan membuka browser untuk login Google
- Pilih akun yang memiliki Firebase project

## Langkah 3: Initialize Firebase (HANYA SEKALI)
Jika belum ada `.firebaserc`:
```bash
firebase init hosting
```

Pilihan:
- Use existing project → Pilih project Firebase Anda
- What do you want to use as your public directory? → `.` (current directory)
- Configure as single-page app? → Y (Yes)

Akan membuat `.firebaserc` secara otomatis.

## Langkah 4: Deploy ke Firebase
```bash
firebase deploy
```

Atau di folder project:
```bash
cd d:\games\arMind
firebase deploy
```

## Langkah 5: Akses URL
Setelah deploy sukses, akan dapat URL seperti:
```
https://your-project.web.app
```

Buka di browser/ponsel dan test!

---

## ⚠️ Penting untuk AR App:
✅ HTTPS → Otomatis (Firebase enforce HTTPS)
✅ Camera Permission → Akan diminta browser
✅ CORS → Tidak ada masalah
✅ .mind files → Serve dengan benar
✅ CDN Global → Fast di mana saja

## Troubleshooting:

### Error: "No project selected"
```bash
firebase use --add
```

### Mau set project ID manual:
```bash
firebase use your-project-id
```

### Lihat status deploy:
```bash
firebase hosting:channel:list
```

### Rollback versi lama:
```bash
firebase hosting:releases:list
firebase hosting:rollback [RELEASE_ID]
```

---

## 📱 Testing di Ponsel:
1. Dari URL Firebase, buka di Chrome/Safari ponsel
2. Browser akan minta permission kamera → Izinkan
3. Scan marker dengan ponsel
4. Objects muncul di atas marker!

Sukses! 🎉
