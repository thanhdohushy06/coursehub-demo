# CourseHub - Buoi 3

Backend: FastAPI + SQLAlchemy Core + PostgreSQL.
Chay tu thu muc goc:
python -m uvicorn backend.app.main:app --reload

Swagger UI: http://127.0.0.1:8000/docs
Postman environment: base_url = http://127.0.0.1:8000

Thu tu kiem tra du lieu:
GET health -> GET courses/sections -> POST enrollment
-> thu loi 409/422 -> DELETE enrollment -> GET sections.

Bai tap tu thuc hanh:
- Bai 1: GET /lecturers (danh sach giang vien)
- Bai 2: GET /sections/{section_id} (chi tiet lop hoc phan gom mon hoc, hoc ky, giang vien, suc chua)
- Bai 3: PATCH /sections/{section_id}/capacity (cap nhat suc chua lop, validation gt 0, conflict khi nho hon so da dang ky)
- Bai 4: GET /courses ho tro phan trang (skip, limit) va tim kiem (q)
- Bai 5: Collection Postman day du request va test script cho tat ca endpoint tren.

Khong commit backend/.env.
