-- ===================================================
-- TỆP: 06_view_demo.sql
-- QUAN SÁT VIEW KHI CÓ ĐĂNG KÝ MỚI VÀ HOÀN TÁC
-- ===================================================

-- Bước 1: Bắt đầu giao dịch
-- SQL | 06_view_demo.sql - buoc 1
BEGIN;

-- Bước 2: Hoàng Nam (22000004) thử đăng ký lớp WEB-01
-- SQL | 06_view_demo.sql - buoc 2
INSERT INTO enrollments (student_id, class_section_id)
VALUES ('22000004', 'WEB-01');

-- Bước 3: Xem kết quả thống kê qua view (khi giao dịch chưa commit)
-- SQL | 06_view_demo.sql - buoc 3
SELECT class_id, capacity, enrolled, remaining
FROM v_section_summary
WHERE class_id = 'WEB-01';

-- Bước 4: Hủy đăng ký thử để không làm lệch bộ dữ liệu
-- SQL | 06_view_demo.sql - buoc 4
ROLLBACK;

-- Bước 5: Xem lại view để kiểm tra số liệu đã trở về ban đầu
-- SQL | 06_view_demo.sql - buoc 5
SELECT class_id, capacity, enrolled, remaining
FROM v_section_summary
WHERE class_id = 'WEB-01';