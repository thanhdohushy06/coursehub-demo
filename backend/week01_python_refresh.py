print("CourseHub - Buoi 1")
students = [
{"id": "22000001", "name": "Nguyen Minh Anh", "major": "KHDL"},
{"id": "22000002", "name": "Tran Duc Long", "major": "KHDL"},
]
courses = [
{
"code": "INT2204",
"name": "Co so du lieu Web va he thong thong tin",
"capacity": 3,
"enrolled": 2,
},
{
"code": "INT2205",
"name": "Khai pha du lieu",
"capacity": 2,
"enrolled": 2,
},
]
enrollments = [
{"student_id": "22000001", "course_code": "INT2204"}
]
for course in courses:
    remaining= course["capacity"] - course["enrolled"]
    print(course["code"], "- con", remaining, "cho")

def find_course(course_code):
    for i in courses:
        if i["code"]==course_code:
            return i
    return None

print(find_course("INT2205"))

def can_enroll(student_id, course_code):
        course = find_course(course_code)
        if course is None:
               return False, "Hoc phan khong ton tai"
        if course["enrolled"] >= course["capacity"]:
               return False, "Lop da du so luong"
        duplicated = any(
        item["student_id"] == student_id and item["course_code"] == course_code for item in enrollments
        )
        if duplicated:
              return False, "Sinh vien da dang ky hoc phan nay"
        return True, "Co the dang ky"
print(can_enroll("22000002", "INT2204"))


def search_courses(keyword):
    normalized=keyword.strip().lower()
    result=[]
    for i in courses:
        if normalized in i["code"].lower() or normalized in i["name"].lower():
            result.append(i)
    return result

print(search_courses("2205"))
# ================= DỮ LIỆU BAN ĐẦU =================
students = [
    {"id": "22000001", "name": "Nguyen Minh Anh", "major": "KHDL"},
    {"id": "22000002", "name": "Tran Duc Long", "major": "KHDL"},
]

courses = [
    {
        "code": "INT2204",
        "name": "Co so du lieu Web va he thong thong tin",
        "capacity": 3,
        "enrolled": 2,
    },
    {
        "code": "INT2205",
        "name": "Khai pha du lieu",
        "capacity": 2,
        "enrolled": 2,
    },
]

enrollments = [
    {"student_id": "22000001", "course_code": "INT2204"}
]

# ================= HÀM HỖ TRỢ =================
def find_student(student_id):
    """Tìm sinh viên theo mã"""
    for s in students:
        if s["id"] == student_id:
            return s
    return None

def find_course(course_code):
    """Tìm học phần theo mã"""
    for c in courses:
        if c["code"] == course_code:
            return c
    return None

# ================= 1. HOÀN THIỆN HÀM ĐĂNG KÝ HỌC PHẦN =================
def enroll_student(student_id, course_code):
    # 1. Kiểm tra sinh viên tồn tại
    student = find_student(student_id)
    if student is None:
        return False, "Lỗi: Sinh viên không tồn tại"

    # 2. Kiểm tra học phần tồn tại
    course = find_course(course_code)
    if course is None:
        return False, "Lỗi: Học phần không tồn tại"

    # 3. Kiểm tra lớp còn chỗ
    if course["enrolled"] >= course["capacity"]:
        return False, "Lỗi: Lớp đã đủ số lượng"

    # 4. Kiểm tra sinh viên chưa đăng ký trùng
    duplicated = any(
        item["student_id"] == student_id and item["course_code"] == course_code
        for item in enrollments
    )
    if duplicated:
        return False, "Lỗi: Sinh viên đã đăng ký học phần này rồi"

    # 5. Đăng ký thành công: thêm bản ghi vào enrollments và tăng số lượng enrolled
    enrollments.append({
        "student_id": student_id,
        "course_code": course_code
    })
    course["enrolled"] += 1

    return True, "Đăng ký thành công"

# ================= 2. KIỂM TRA CHƯƠNG TRÌNH (05 TEST CASES) =================
print("--- BẮT ĐẦU CHẠY THỬ 05 TÌNH HUỐNG ---")

# Test 1: Đăng ký thành công (sinh viên 22000002 đăng ký INT2204 còn 1 chỗ)
test1 = enroll_student("22000002", "INT2204")
print("1. Đăng ký thành công:", test1)

# Test 2: Đăng ký trùng (sinh viên 22000001 đăng ký lại INT2204 đã có trong enrollments)
test2 = enroll_student("22000001", "INT2204")
print("2. Đăng ký trùng:", test2)

# Test 3: Lớp đầy (học phần INT2205 có capacity=2, enrolled=2)
test3 = enroll_student("22000002", "INT2205")
print("3. Lớp đầy:", test3)

# Test 4: Mã học phần không tồn tại (INT9999)
test4 = enroll_student("22000001", "INT9999")
print("4. Mã học phần không tồn tại:", test4)

# Test 5: Mã sinh viên không tồn tại (99999999)
test5 = enroll_student("99999999", "INT2204")
print("5. Mã sinh viên không tồn tại:", test5)

# In lại danh sách sau khi thực hiện
print("\n--- KẾT QUẢ DỮ LIỆU SAU CÙNG ---")
print("Enrollments:", enrollments)
print("INT2204 enrolled hiện tại:", find_course("INT2204")["enrolled"])
