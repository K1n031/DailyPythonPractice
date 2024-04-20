"""
Viết một chương trình Python để kiểm tra xem một số có phải là số nguyên tố hay không. Số nguyên
tố là số nguyên dương lớn hơn 1 và chỉ có hai ước số dương là 1 và chính nó.
Yêu cầu:
•Viết một hàm có tên là is_prime nhận một số nguyên dương n và trả về một giá trị boolean. Nếu
n là số nguyên tố, hàm sẽ trả về True, ngược lại trả về False.
•Sử dụng Type Hints để gợi ý về kiểu dữ liệu của tham số và giá trị trả về của hàm.
•Sử dụng mypy để kiểm tra kiểu dữ liệu trong chương trình
"""

# Hàm kiểm tra số nguyên tố
def is_prime(n: int) -> bool:
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

if __name__ == "__main__":
    print(is_prime(2))
    print(is_prime("X"))
    print(is_prime.__annotations__)