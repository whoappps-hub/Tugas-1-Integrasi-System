# Penjelasan Output - API Data Mahasiswa v2.0

Dokumen ini menjelaskan semua output yang dihasilkan project, mulai dari
halaman dokumentasi (`/docs`), response body tiap endpoint, perintah curl,
request URL, hingga file `openapi.json`. Disusun sebagai bahan presentasi
ke dosen pengampu.

---

## 1. Gambaran Umum Project

| Komponen | Keterangan |
|---|---|
| Framework | FastAPI (Python) + Uvicorn (ASGI server) |
| Dokumentasi | Swagger UI kustom di `http://127.0.0.1:8000/docs` |
| Versi API | v2.0 - Iterasi Pengembangan (sesuai badge di banner `/docs`) |
| Penyimpanan | Simulasi database in-memory (`items_db = {}`) |
| Format data | JSON (`Content-Type: application/json`) |

### Struktur file

| File | Fungsi |
|---|---|
| `main.py` | Logika aplikasi: model `Item` dan 4 endpoint CRUD |
| `swagger_ui.py` | Desain tampilan Swagger UI (terpisah dari logika) |
| `penjelasan_output.md` | Dokumen ini - penjelasan semua output |

### Cara menjalankan

```bash
env\Scripts\python.exe -m uvicorn main:app --reload
```

Lalu buka `http://127.0.0.1:8000/docs` untuk Swagger UI
dan `http://127.0.0.1:8000/openapi.json` untuk spesifikasi OpenAPI.

---

## 2. Penjelasan Output Halaman `/docs` (Swagger UI)

Halaman `/docs` adalah dokumentasi interaktif. Setiap elemen di halaman
tersebut punya arti:

### 2.1 Banner versi (bagian paling atas)

| Elemen | Tampilan | Arti |
|---|---|---|
| Judul | `API Data Mahasiswa` | Nama project |
| Badge | `v2.0 - Iterasi Pengembangan` | Menandai bahwa project ini hasil pengembangan dari versi sebelumnya |
| Catatan | `Fitur baru: dokumentasi Swagger UI kustom (light theme), status error REST 404 / 409` | Daftar perubahan di versi 2.0 |

Banner ini **tidak ada di Swagger UI default FastAPI** - dibuat khusus di
file `swagger_ui.py` (fungsi `setup_swagger_ui`).

### 2.2 Bagian informasi API (Info)

```
API Data Mahasiswa
REST API CRUD untuk data mahasiswa (NAMA, ALAMAT, IPK, SEMESTER, HOBI).
```

- **Title** = judul dari `FastAPI(title=...)` di `main.py`
- **Description** = dari parameter `description=` di `main.py`
- **Version** = sengaja **tidak ditampilkan** di halaman docs (disembunyikan
  lewat CSS kustom di `swagger_ui.py`), sehingga badge versi seperti `0.0`
  tidak muncul di layar. Nilainya tetap tersimpan di konfigurasi `main.py`.

> Catatan: teks `OAS 3.1` / `3.1.0` tidak pernah tampil di halaman `/docs`.
> Teks itu hanya ada di file `/openapi.json` sebagai field `"openapi":
> "3.1.0"` (standar spesifikasi yang dipakai FastAPI untuk membangun
> dokumentasi) dan hanya terlihat jika URL tersebut dibuka langsung
> di browser.

### 2.3 Warna tombol method (tools) - maknanya

| Method | Warna tombol | Latar kartu | Kegunaan |
|---|---|---|---|
| `GET` | Hijau (`#1a7f37`) | Hijau muda | Ambil / baca data (READ) |
| `POST` | Biru (`#0969da`) | Biru muda | Tambah data baru (CREATE) |
| `PUT` | Oranye (`#bc4c00`) | Krem | Ubah data (UPDATE) |
| `DELETE` | Merah (`#cf222e`) | Merah muda | Hapus data (DELETE) |

Setiap kartu operasi juga punya garis tepi kiri (border-left) 5px berwarna
sama sehingga method cepat dikenali.

### 2.4 Tombol aksi di setiap endpoint

| Tombol | Fungsi |
|---|---|
| `Try it out` | Mengaktifkan mode percobaan - form input bisa diisi dan dikirim |
| `Execute` (hijau) | Mengirim request sungguhan ke server |
| `Cancel` (abu) | Membatalkan mode Try it out |
| `Authorize` (ungu) | Panel otorisasi (tidak dipakai di API ini karena tanpa autentikasi) |

### 2.5 Panel output setelah menekan Execute

Setelah request dikirim, Swagger UI menampilkan:

| Panel | Isi |
|---|---|
| **Request URL** | URL lengkap permintaan, contoh: `http://127.0.0.1:8000/items/1` |
| **Request Headers** | Header yang dikirim, terutama `Content-Type: application/json` |
| **Response Body** | Isi JSON yang dikembalikan server (sama persis dengan contoh di bagian 4) |
| **Response Code** | Kode status HTTP, contoh `200`, `404`, `409` |
| **Response Headers** | Header balasan, terutama `content-type: application/json` |

### 2.6 Bagian lain di halaman `/docs`

| Elemen | Fungsi |
|---|---|
| Filter box (kiri atas) | Menyaring endpoint berdasarkan kata kunci, misal ketik `item` |
| Bagian tag `Items` | Kelompok semua endpoint CRUD |
| Bagian `Schemas` | Menampilkan struktur model `Item` hasil generate dari Pydantic |
| `defaultModelsExpandDepth: 1` | Schema `Item` tampil otomatis (konfigurasi di `swagger_ui.py`) |

---

## 3. Daftar Endpoint

| Method | Request URL | Fungsi | Status sukses | Status error |
|---|---|---|---|---|
| POST | `/items/{item_id}` | Tambah data | 200 | 409, 422 |
| GET | `/items/{item_id}` | Ambil 1 data | 200 | 404 |
| PUT | `/items/{item_id}` | Ubah data | 200 | 404, 422 |
| DELETE | `/items/{item_id}` | Hapus data | 200 | 404 |

Struktur data (`model Item`):

```json
{
  "nama": "string (opsional)",
  "alamat": "string (opsional)",
  "ipk": "angka desimal (opsional)",
  "semester": "angka bulat (opsional)",
  "hobi": "string (opsional)"
}
```

---

## 4. Output Tiap Endpoint (hasil nyata)

> Semua response body di bawah adalah output asli saat server dijalankan.

### 4.1 CREATE - POST `/items/1`

**Request URL:**
`http://127.0.0.1:8000/items/1`

**Request body:**

```json
{
  "nama": "Budi Santoso",
  "alamat": "Jl. Merdeka No. 10",
  "ipk": 3.75,
  "semester": 5,
  "hobi": "Bersepeda"
}
```

**cURL:**

```bash
curl -X POST "http://127.0.0.1:8000/items/1" \
  -H "Content-Type: application/json" \
  -d "{\"nama\":\"Budi Santoso\",\"alamat\":\"Jl. Merdeka No. 10\",\"ipk\":3.75,\"semester\":5,\"hobi\":\"Bersepeda\"}"
```

**Response sukses - 200 OK:**

```json
{
  "message": "Item created successfully",
  "item": {
    "nama": "Budi Santoso",
    "alamat": "Jl. Merdeka No. 10",
    "ipk": 3.75,
    "semester": 5,
    "hobi": "Bersepeda"
  }
}
```

**Error jika id sudah ada - 409 Conflict:**

```json
{
  "detail": "Item already exists"
}
```

**Error jika tipe data salah (ipk diisi teks) - 422 Unprocessable Entity:**

```json
{
  "detail": [
    {
      "type": "float_parsing",
      "loc": ["body", "ipk"],
      "msg": "Input should be a valid number, unable to parse string as a number",
      "input": "bukan-angka"
    }
  ]
}
```

### 4.2 READ - GET `/items/1`

**Request URL:**
`http://127.0.0.1:8000/items/1`

**cURL:**

```bash
curl "http://127.0.0.1:8000/items/1"
```

**Response sukses - 200 OK:**

```json
{
  "item_id": 1,
  "item": {
    "nama": "Budi Santoso",
    "alamat": "Jl. Merdeka No. 10",
    "ipk": 3.75,
    "semester": 5,
    "hobi": "Bersepeda"
  }
}
```

**Error jika id tidak ada - 404 Not Found:**

```json
{
  "detail": "Item not found"
}
```

### 4.3 UPDATE - PUT `/items/1`

**Request URL:**
`http://127.0.0.1:8000/items/1`

**Request body:**

```json
{
  "nama": "Budi Santoso",
  "alamat": "Jl. Sudirman",
  "ipk": 3.8,
  "semester": 5,
  "hobi": "Renang"
}
```

**cURL:**

```bash
curl -X PUT "http://127.0.0.1:8000/items/1" \
  -H "Content-Type: application/json" \
  -d "{\"nama\":\"Budi Santoso\",\"alamat\":\"Jl. Sudirman\",\"ipk\":3.8,\"semester\":5,\"hobi\":\"Renang\"}"
```

**Response sukses - 200 OK:**

```json
{
  "message": "Item updated successfully",
  "item": {
    "nama": "Budi Santoso",
    "alamat": "Jl. Sudirman",
    "ipk": 3.8,
    "semester": 5,
    "hobi": "Renang"
  }
}
```

**Error jika id tidak ada - 404 Not Found:**

```json
{
  "detail": "Item not found"
}
```

### 4.4 DELETE - `/items/1`

**Request URL:**
`http://127.0.0.1:8000/items/1`

**cURL:**

```bash
curl -X DELETE "http://127.0.0.1:8000/items/1"
```

**Response sukses - 200 OK (menampilkan data yang dihapus):**

```json
{
  "message": "Item deleted successfully",
  "deleted_item": {
    "nama": "Budi Santoso",
    "alamat": "Jl. Sudirman",
    "ipk": 3.8,
    "semester": 5,
    "hobi": "Renang"
  }
}
```

**Error jika id tidak ada - 404 Not Found:**

```json
{
  "detail": "Item not found"
}
```

---

## 5. Penjelasan Makna Tiap Field Response Body

### 5.1 Response CREATE / UPDATE

| Field | Tipe | Arti |
|---|---|---|
| `message` | string | Konfirmasi operasi berhasil |
| `item` | object | Data hasil simpan, berisi field `nama`, `alamat`, `ipk`, `semester`, `hobi` |

### 5.2 Response READ

| Field | Tipe | Arti |
|---|---|---|
| `item_id` | integer | Id pada path URL yang diminta |
| `item` | object | Data mahasiswa yang ditemukan |

### 5.3 Response DELETE

| Field | Tipe | Arti |
|---|---|---|
| `message` | string | Konfirmasi penghapusan berhasil |
| `deleted_item` | object | Data yang baru saja dihapus (untuk audit/keperluan tampilan ulang) |

### 5.4 Response error

| Field | Tipe | Arti |
|---|---|---|
| `detail` | string | Pesan error singkat (404 / 409) |
| `detail` | array of object | Daftar error validasi dari Pydantic (422), tiap objek berisi `type`, `loc` (lokasi field), `msg` (pesan), `input` (nilai salah) |

---

## 6. Kode Status HTTP yang Digunakan

| Kode | Nama | Kapan muncul | Contoh pesan |
|---|---|---|---|
| 200 | OK | Request berhasil | `Item created successfully` |
| 404 | Not Found | Data tidak ditemukan (GET/PUT/DELETE) | `Item not found` |
| 409 | Conflict | Data sudah ada saat CREATE | `Item already exists` |
| 422 | Unprocessable Entity | Validasi gagal (tipe data salah) | `Input should be a valid number...` |

Catatan pengembangan: pada versi sebelumnya semua error masih mengembalikan
status 200 sehingga klien tidak bisa membedakan sukses/gagal. Di v2.0 error
sudah memakai kode status REST yang benar.

---

## 7. Output `/openapi.json` (Spesifikasi OpenAPI)

Akses: `http://127.0.0.1:8000/openapi.json`

Bagian penting dan artinya:

```json
{
  "info": {
    "title": "API Data Mahasiswa",
    "version": "0.0"
  },
  "paths": {
    "/items/{item_id}": {
      "post": { "...": "operasi CREATE" },
      "get": { "...": "operasi READ" },
      "put": { "...": "operasi UPDATE" },
      "delete": { "...": "operasi DELETE" }
    }
  },
  "components": {
    "schemas": {
      "Item": {
        "properties": {
          "nama": {}, "alamat": {}, "ipk": {}, "semester": {}, "hobi": {}
        }
      }
    }
  }
}
```

| Bagian | Arti |
|---|---|
| `info` | Metadata judul + versi API |
| `paths` | Daftar URL + method yang tersedia (otomatis dibuat FastAPI) |
| `components.schemas.Item` | Struktur model data, menjadi bagian `Schemas` di halaman `/docs` |

File ini dibuat otomatis oleh FastAPI dari kode di `main.py` - inilah yang
dibaca Swagger UI untuk menampilkan dokumentasi.

Catatan: di file asli `/openapi.json` baris pertama berisi
`"openapi": "3.1.0"` (standar OAS 3.1 yang dipakai FastAPI). Field ini
**tidak pernah tampil** di halaman `/docs` - hanya terlihat jika URL
`/openapi.json` dibuka langsung di browser, dan wajib dipertahankan agar
Swagger UI bisa membaca spesifikasi.

---

## 8. Alur Presentasi yang Disarankan

1. Tunjukkan struktur file: `main.py` (logika) vs `swagger_ui.py` (tampilan).
2. Buka `/docs`: jelaskan banner versi, warna method, tombol Try it out.
3. Demo CREATE lewat Swagger UI → tunjukkan Request URL dan Response Body.
4. Demo error 409 (id duplikat) dan 404 (id tidak ada) → bandingkan dengan
   versi lama yang selalu 200.
5. Jalankan perintah curl di terminal → buktikan output sama dengan di docs.
6. Buka `/openapi.json` → jelaskan auto-generated specification.
7. Tutup dengan daftar pengembangan v2.0 (pemisahan file desain, light theme
   kustom, status error REST).

---

## 9. Catatan Teknis

- Database simulasi (`items_db`) bersifat **in-memory**: data hilang saat
  server dihentikan.
- Model memakai Pydantic v2 dengan `model_dump()` (metode modern, menggantikan
  `.dict()` yang sudah deprecated).
- Desain Swagger UI disimpan di `swagger_ui.py` sehingga perubahan tampilan
  tidak mempengaruhi logika CRUD di `main.py`.
- Server berjalan pada `http://127.0.0.1:8000` (default uvicorn).
