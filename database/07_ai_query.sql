-- ===================================================
-- IX. KIỂM TRA TRUY VẤN DO AI ĐỀ XUẤT
-- ===================================================

-- 1. Truy vấn chạy được nhưng đếm sai (Dùng COUNT(*) với LEFT JOIN)
-- SQL | 07_ai_query.sql - vi du sai de doi chieu
SELECT cs.id, COUNT(*) AS enrolled
FROM class_sections AS cs
LEFT JOIN enrollments AS e ON e.class_section_id = cs.id
WHERE cs.id = 'WEB-02'
GROUP BY cs.id;
-- 2. Sửa cột được đếm (Dùng COUNT(cột) thay cho COUNT(*))
-- SQL | 07_ai_query.sql - truy van da sua
SELECT cs.id, COUNT(e.student_id) AS enrolled
FROM class_sections AS cs
LEFT JOIN enrollments AS e ON e.class_section_id = cs.id
WHERE cs.id = 'WEB-02'
GROUP BY cs.id;
