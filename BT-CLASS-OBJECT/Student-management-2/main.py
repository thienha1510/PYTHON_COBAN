# Import thư viện student
import StuMana.student as s
 
# CHƯƠNG TRÌNH CHÍNH
action = 0
 
while action >= 0:
    if action == 1:
        s.addStudent()
    elif action == 2:
        s.deleteStudent()
    elif action == 3:
        s.editStudent()
    elif action == 4:
        s.showStudents()
 
    print("Chọn chức năng muốn thực hiện:")
    print("Nhập 1: Thêm sinh viên")
    print("Nhập 2: Xóa sinh viên")
    print("Nhập 3: Sửa sinh viên")
    print("Nhập 4: Xem danh sách sinh viên")
    print("Nhập 0: Thoát khỏi chương trình")
    action = int(input())
    if action == 0:
        break