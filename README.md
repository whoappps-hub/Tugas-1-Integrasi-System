# API Data Mahasiswa

REST API CRUD untuk data mahasiswa (NAMA, ALAMAT, IPK, SEMESTER, HOBI) dibangun dengan FastAPI. Kunci identitas record adalah `nama` (natural key, case-sensitive). Penyimpanan in-memory (dict) — data hilang saat server restart.

## Setup

Windows (venv sudah ada di folder `env`):

```powershell
env\Scripts\Activate.ps1      # bila gagal: Set-ExecutionPolicy -Scope Process Bypass
pip install -r requirements.txt
```

Linux/macOS:

```bash
python -m venv env
source env/bin/activate
pip install -r requirements.txt
```

## Menjalankan

```bash
uvicorn main:app --reload --port 8010
```

- Swagger UI: http://localhost:8010/docs
- ReDoc: http://localhost:8010/redoc
- OpenAPI JSON: http://localhost:8010/openapi.json

> Port 8000 saat ini dipakai proyek lain, karena itu `--port 8010` dipakai.
> Bila port 8000 kosong, cukup `uvicorn main:app --reload` (docs di http://localhost:8000/docs).

## Endpoint

| Method | Path | Fungsi | Success | Error |
|--------|------|--------|---------|-------|
| POST | `/mahasiswa` | Tambah data baru | 201 | 409, 422 |
| GET | `/mahasiswa` | Ambil semua data | 200 | — |
| GET | `/mahasiswa/{nama}` | Ambil satu data | 200 | 404, 422 |
| PUT | `/mahasiswa/{nama}` | Perbarui data | 200 | 404, 422 |
| DELETE | `/mahasiswa/{nama}` | Hapus data | 200 | 404, 422 |

## Contoh Request

```bash
curl -X POST http://localhost:8010/mahasiswa -H "Content-Type: application/json" -d "{\"nama\":\"Budi Santoso\",\"alamat\":\"Jl. Merdeka No. 10, Jakarta\",\"ipk\":3.75,\"semester\":5,\"hobi\":\"Bersepeda\"}"

curl http://localhost:8010/mahasiswa

curl "http://localhost:8010/mahasiswa/Budi%20Santoso"

curl -X PUT "http://localhost:8010/mahasiswa/Budi%20Santoso" -H "Content-Type: application/json" -d "{\"nama\":\"Budi Santoso\",\"ipk\":3.80,\"semester\":6,\"hobi\":\"Berenang\"}"

curl -X DELETE "http://localhost:8010/mahasiswa/Budi%20Santoso"
```

## Struktur Project

```
.
├── main.py          # Aplikasi FastAPI (model + 5 endpoint)
├── openapi.yaml     # Spesifikasi OpenAPI 3.0
├── requirements.txt
├── prd.md           # Product Requirements Document
├── schema.md        # Definisi field & skema data
└── design.md        # Spesifikasi OpenAPI & mock Swagger UI
```
