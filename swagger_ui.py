"""Kustomisasi tampilan Swagger UI (endpoint /docs).

File ini terpisah dari main.py agar urusan tampilan dokumentasi
mudah diubah tanpa menyentuh logika aplikasi (CRUD).
"""

from fastapi import FastAPI, Request
from fastapi.openapi.docs import get_swagger_ui_html
from fastapi.responses import HTMLResponse

# Konfigurasi perilaku Swagger UI
SWAGGER_UI_PARAMETERS = {
    "docExpansion": "none",
    "filter": True,
    "persistAuthorization": True,
    "tryItOutEnabled": True,
    "displayRequestDuration": True,
    "tagsSorter": "alpha",
    "operationsSorter": "alpha",
    "defaultModelsExpandDepth": 1,
    "showCommonExtensions": True,
    "showExtensions": True,
    "deepLinking": True,
}

# Desain terang (light theme) yang clean
CUSTOM_STYLE = """
<style>
html, body {
    background: #f6f8fa !important;
    color: #1f2328;
    margin: 0;
    font-family: 'Segoe UI', system-ui, -apple-system, sans-serif;
}

/* ===== Banner versi ===== */
.dev-banner {
    position: sticky;
    top: 0;
    z-index: 100;
    display: flex;
    align-items: center;
    gap: 14px;
    padding: 11px 24px;
    background: #ffffff;
    border-bottom: 2px solid #0969da;
    box-shadow: 0 1px 3px rgba(31, 35, 40, 0.08);
    font-family: 'Segoe UI', system-ui, sans-serif;
}
.dev-banner__title {
    font-weight: 700;
    font-size: 15px;
    color: #1f2328;
    letter-spacing: 0.3px;
}
.dev-badge {
    background: #0969da;
    color: #ffffff;
    padding: 3px 12px;
    border-radius: 999px;
    font-size: 12px;
    font-weight: 700;
    text-transform: uppercase;
}
.dev-banner__note {
    margin-left: auto;
    font-size: 12px;
    color: #424a53;
}

/* ===== Dasar Swagger UI ===== */
.swagger-ui {
    background: #f6f8fa;
    color: #1f2328;
    font-family: 'Segoe UI', system-ui, sans-serif;
}
.swagger-ui .wrapper {
    max-width: 1150px;
    padding: 0 24px;
}
.swagger-ui .info .title {
    color: #1f2328 !important;
}
.swagger-ui .info .description {
    color: #424a53 !important;
}
/* Versi ("0.0") disembunyikan dari tampilan - hanya hilang di layar,
   data di /openapi.json tetap utuh agar Swagger UI tetap berjalan */
.swagger-ui .info .version {
    display: none !important;
}
.swagger-ui .info a,
.swagger-ui a {
    color: #0969da !important;
}
.swagger-ui .info {
    margin: 22px 0 10px;
    padding-bottom: 16px;
    border-bottom: 1px solid #d0d7de;
}

/* ===== Kotak pemilih scheme ===== */
.swagger-ui .scheme-container {
    background: #ffffff !important;
    box-shadow: 0 1px 0 rgba(31, 35, 40, 0.04) !important;
    border: 1px solid #d0d7de !important;
    border-radius: 8px;
    padding: 14px 16px;
    margin: 16px 0;
}
.swagger-ui .scheme-container .schemes-title,
.swagger-ui .scheme-container label {
    color: #24292f !important;
}

/* ===== Judul tag (kelompok endpoint) ===== */
.swagger-ui .opblock-tag {
    color: #1f2328 !important;
    border-bottom: 1px solid #d0d7de !important;
    font-size: 18px;
    font-weight: 600;
    background: transparent;
}
.swagger-ui .opblock-tag a {
    color: #1f2328 !important;
}
.swagger-ui .opblock-tag small {
    color: #424a53 !important;
}

/* ===== Kartu operasi (warna method tegas) ===== */
.swagger-ui .opblock {
    border: 1px solid #d0d7de !important;
    border-radius: 8px;
    margin: 14px 0;
    background: #ffffff;
    overflow: hidden;
    box-shadow: 0 1px 2px rgba(31, 35, 40, 0.06);
}
.swagger-ui .opblock .opblock-summary-method {
    border-radius: 6px;
    font-weight: 700;
    letter-spacing: 0.5px;
    border: none;
}

/* GET - hijau */
.swagger-ui .opblock.opblock-get {
    background: #f6fbf7 !important;
    border-left: 5px solid #1a7f37 !important;
}
.swagger-ui .opblock.opblock-get .opblock-summary-method {
    background: #1a7f37 !important;
    color: #ffffff !important;
}

/* POST - biru */
.swagger-ui .opblock.opblock-post {
    background: #f3f8fd !important;
    border-left: 5px solid #0969da !important;
}
.swagger-ui .opblock.opblock-post .opblock-summary-method {
    background: #0969da !important;
    color: #ffffff !important;
}

/* PUT - oranye/amber */
.swagger-ui .opblock.opblock-put {
    background: #fffbf1 !important;
    border-left: 5px solid #bc4c00 !important;
}
.swagger-ui .opblock.opblock-put .opblock-summary-method {
    background: #bc4c00 !important;
    color: #ffffff !important;
}

/* DELETE - merah */
.swagger-ui .opblock.opblock-delete {
    background: #fff8f7 !important;
    border-left: 5px solid #cf222e !important;
}
.swagger-ui .opblock.opblock-delete .opblock-summary-method {
    background: #cf222e !important;
    color: #ffffff !important;
}

.swagger-ui .opblock .opblock-summary-path a,
.swagger-ui .opblock .opblock-summary-operation-id {
    color: #0969da !important;
}
.swagger-ui .opblock-summary-description,
.swagger-ui .opblock .opblock-description {
    color: #424a53 !important;
}
.swagger-ui .opblock .opblock-section-header {
    background: #ffffff !important;
    box-shadow: none !important;
    border-color: #d0d7de !important;
}
.swagger-ui .opblock-body pre,
.swagger-ui .opblock-body .body-param__example {
    background: #f6f8fa !important;
    color: #1f2328 !important;
    border: 1px solid #d0d7de;
    border-radius: 6px;
}
.swagger-ui .highlight-code,
.swagger-ui .microlight {
    background: #f6f8fa !important;
    color: #1f2328 !important;
    border: 1px solid #d0d7de !important;
}

/* ===== Tabel parameter & response ===== */
.swagger-ui table thead tr th {
    color: #1f2328 !important;
    border-bottom: 1px solid #d0d7de !important;
    background: #f6f8fa;
}
.swagger-ui table td {
    color: #24292f !important;
    border-bottom: 1px solid #eaeef2 !important;
}
.swagger-ui .parameter__name {
    color: #1f2328 !important;
}
.swagger-ui .parameter__type,
.swagger-ui .parameter__in {
    color: #424a53 !important;
}
.swagger-ui .response-col_status {
    color: #24292f !important;
    font-weight: 600;
}

.swagger-ui .responses-inner h4,
.swagger-ui .responses-inner h5 {
    color: #1f2328 !important;
}
.swagger-ui .responses-inner p {
    color: #424a53 !important;
}

/* ===== Model / Schema ===== */
.swagger-ui .models {
    border: 1px solid #d0d7de !important;
    border-radius: 8px;
    background: #ffffff;
    padding: 12px 16px;
    margin-top: 24px;
}
.swagger-ui .models h4 {
    color: #1f2328 !important;
}
.swagger-ui .model-container {
    background: #ffffff !important;
    border-color: #d0d7de !important;
    border-radius: 6px;
}
.swagger-ui .model-title {
    color: #0969da !important;
}
.swagger-ui .model-box {
    background: #f6f8fa !important;
    border: 1px solid #d0d7de !important;
}
.swagger-ui .property.primitive {
    color: #0550ae !important;
}

/* ===== Tombol aksi ===== */
.swagger-ui .btn {
    border-radius: 6px;
    font-weight: 600;
    box-shadow: none !important;
    border: 1px solid #d0d7de !important;
    background: #f6f8fa !important;
    color: #24292f !important;
    transition: background 0.15s ease, border-color 0.15s ease;
}
.swagger-ui .btn:hover {
    background: #eef1f4 !important;
    border-color: #b6bdc5 !important;
}
.swagger-ui .btn.cancel {
    background: #f6f8fa !important;
    color: #424a53 !important;
    border-color: #d0d7de !important;
}
.swagger-ui .btn.execute,
.swagger-ui .btn.try-out__btn {
    background: #1a7f37 !important;
    color: #ffffff !important;
    border: 1px solid #1a7f37 !important;
}
.swagger-ui .btn.execute:hover,
.swagger-ui .btn.try-out__btn:hover {
    background: #167331 !important;
}
.swagger-ui .btn.authorize {
    color: #8250df !important;
    border-color: #8250df !important;
    background: #ffffff !important;
}
.swagger-ui .btn-group .btn {
    background: #ffffff !important;
    color: #24292f !important;
    border-color: #d0d7de !important;
}

/* ===== Input & filter ===== */
.swagger-ui input[type="text"],
.swagger-ui input[type="password"],
.swagger-ui textarea,
.swagger-ui select {
    background: #ffffff !important;
    color: #1f2328 !important;
    border: 1px solid #d0d7de !important;
    border-radius: 6px;
}
.swagger-ui input[type="text"]:focus,
.swagger-ui textarea:focus,
.swagger-ui select:focus {
    border-color: #0969da !important;
    box-shadow: 0 0 0 3px rgba(9, 105, 218, 0.15) !important;
    outline: none;
}
.swagger-ui .filter input {
    background: #ffffff !important;
    color: #1f2328 !important;
    border: 1px solid #d0d7de !important;
    border-radius: 6px;
}
.swagger-ui .filter .operation-filter-control {
    color: #424a53 !important;
}

/* ===== Loading ===== */
.swagger-ui .loading-container {
    background: #f6f8fa !important;
}
.swagger-ui .loading-container .loading::after {
    color: #0969da !important;
}
</style>
"""

BANNER = """
<div class="dev-banner">
    <span class="dev-banner__title">API Data Mahasiswa</span>
    <span class="dev-badge">Saya Naufal</span>
    <span class="dev-banner__note">Halo semuanya!</span>
</div>
"""


def setup_swagger_ui(app: FastAPI) -> None:
    """Daftarkan route /docs kustom pada aplikasi FastAPI.

    Penggunaan di main.py:
        app = FastAPI(..., docs_url=None)
        setup_swagger_ui(app)
    """

    async def custom_swagger_ui_html(request: Request) -> HTMLResponse:
        response = get_swagger_ui_html(
            openapi_url=app.openapi_url,
            title="API Data Mahasiswa",
            oauth2_redirect_url=None,
            swagger_ui_parameters=SWAGGER_UI_PARAMETERS,
        )
        html = response.body.decode("utf-8")
        html = html.replace("</head>", CUSTOM_STYLE + "\n</head>")
        html = html.replace("<body>", "<body>" + BANNER)
        return HTMLResponse(html)

    app.add_route("/docs", custom_swagger_ui_html, include_in_schema=False)
