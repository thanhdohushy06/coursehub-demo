-- ===================================================
-- VII. THỬ CÁC RÀNG BUỘC BẰNG DỮ LIỆU SAI
-- ===================================================

-- 1. Đăng ký trùng một lớp (Vi phạm PRIMARY KEY pk_enrollments)
-- SQL | 05_constraint_checks.sql - loi co y
INSERT INTO enrollments (student_id, class_section_id)
VALUES ('22000001', 'WEB-01');

-- 2. Đăng ký cho sinh viên không tồn tại (Vi phạm FOREIGN KEY)
-- SQL | 05_constraint_checks.sql - loi co y
INSERT INTO enrollments (student_id, class_section_id)
VALUES ('22999999', 'WEB-01');

-- 3. Đổi sức chứa lớp thành 0 (Vi phạm CHECK ck_sections_capacity)
-- SQL | 05_constraint_checks.sql - loi co y
UPDATE class_sections
SET capacity = 0
WHERE id = 'WEB-01';

-- 4. Bỏ trống số tín chỉ (Vi phạm NOT NULL credits)
-- SQL | 05_constraint_checks.sql - loi co y
UPDATE courses
SET credits = NULL
WHERE code = 'INT2204';

-- 5. Dùng lại email của sinh viên khác (Vi phạm UNIQUE uq_students_email)
-- SQL | 05_constraint_checks.sql - loi co y
UPDATE students
SET email = 'anh@example.com'
WHERE id = '22000002';

-- 6. Nhập họ tên chỉ gồm dấu cách (Vi phạm CHECK ck_students_name)
-- SQL | 05_constraint_checks.sql - loi co y
UPDATE students
SET name = '   '
WHERE id = '22000004';

-- 7. Kiểm tra dữ liệu sau các lần bị từ chối
-- SQL | Query Tool - chay sau cac vi du loi
SELECT COUNT(*) AS total_enrollments
FROM enrollments;
