# Import thư viện chứa data
import StuMana.data as d
 
def addStudent():
    """Hàm thêm một sinh viên"""
    print("*** THÊM SINH VIÊN ***")
 
    # Cấu trúc lưu trữ một sinh viên
    infor = {
        'id' : '',
        'name' : ''
    }
 
    # Nhập ID, có kiểm tra trùng ID thì nhập lại
    print("Nhập ID sinh viên:")
    id = input()
 
    while True:
        student = findStudent(id)
        if student != False:
            print("ID này đã tồn tại, vui lòng nhập lại:")
            id = input()
        else:
            break
 
    infor['id'] = id
 
    # Nhập tên
    print("Nhập tên sinh viên:")
    infor['name'] = input()
 
    # Lưu vào danh sách sv
    d.listStudents.append(infor)
 
 
def findStudent(id):
    """Hàm tìm một sinh viên"""
    for i in range(0, len(d.listStudents)):
        if d.listStudents[i]['id'] == id:
            # Trả về mảng gồm 2 phần tử,
            # 0 là vị trí tìm thấy và 1 là dữ liệu
            return [i, d.listStudents[i]]
    return False
 
def deleteStudent():
    """Hàm xóa sih viên"""
    print("*** XÓA SINH VIÊN ***")
    print("Nhập ID sinh viên cần xóa:")
    id = input()
 
    student = findStudent(id)
 
    if student != False:
        d.listStudents.remove(student[1])
        print("Xóa sinh viên thành công")
    else :
        print("Không tìm thấy sinh viên cần xóa")
 
def showStudents():
    """Hàm hiển thị danh sách sv"""
    print("*** DANH SÁCH SINH VIÊN HIỆN TẠI ***")
    for i in range(0, len(d.listStudents)):
        print("[",d.listStudents[i]['id'],"]", "[",d.listStudents[i]['name'],"]",)
 
def editStudent():
    """Hàm sửa sinh viên"""
    print("*** SỬA THÔNG TIN SINH VIÊN ***")
    print("Nhập ID sinh viên cần sửa")
    id = input()
    student = findStudent(id)
    if student == False:
        print("Không tìm thấy sinh viên ", id)
    else :
        print("Nhập tên sinh viên")
        name = input()
        student[1]['name'] = name
        d.listStudents[student[0]] = student[1]