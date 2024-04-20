#CAN CHI

def calculate_can_chi_calendar(year):
    result = ''
    can = ['Canh', 'Tân', 'Nhâm', 'Quý ', 'Giáp', 'Ất', 'Bính', 'Đinh', 'Mậu', 'Kỷ']
    chi = ['Thân', 'Dậu', 'Tuấn', 'Hợi', 'Tý', 'Sửu', 'Dần', 'Mẹo', 'Thìn', 'Tỵ', 'Ngọ', 'Mùi']
    result = can[year%10] + " " + chi[year%12]
    return result

print(calculate_can_chi_calendar(2024))