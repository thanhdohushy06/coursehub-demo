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
