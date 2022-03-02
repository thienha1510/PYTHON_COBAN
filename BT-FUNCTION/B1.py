print("Program to calculate the average score of students")

Math = 0; Physical = 0; Chemical = 0; Literature = 0; English = 0

def enter_score():
    # Hàm yêu cầu nhập điểm và trả về giá trị trung bình
    
    # Bước 1: Nhập dữ liệu
    print("Enter math score: ")
    Math = float(input())

    print("Enter physical score: ")
    Physical = float(input())

    print("Enter Chemical score: ")
    Chemical = float(input())

    print("Enter literature score: ")
    Literature = float(input())

    print("Enter english score: ")
    English = float(input())

    # Bước 2: Tính điểm trung bình
    average = (Math + Physical + Chemical + Literature + English) / 5

    return average


def result(score):
    # Hàm in kết quả lên màn hình
    
    print("The average score is: ", average)
    if (score < 5):
        print("Weak learning capacity");
    elif (score >= 5 and score < 7):
        print("Academic ability is average")
    elif (score >= 7 and score < 9):
        print("Academic pretty")
    elif (score >= 9):
        print("Good standing")


# Sử dụng hàm
average = enter_score()
result(average)