# I. CÁCH GHI CHÚ TRONG PYTHON
# - Cách ghi chú trong python dùng tổ hợp phím 'ctrl'+'/' hoặc thêm dấu # trước câu
# - Có thể ghi chú bằng cách viết trong dấu ''' ''' hoặc """ """
# -Comment là một thứ cực kì quan trọng, nó giúp truyền đạt ý tưởng, nội dung, 
#chức năng những dòng code của bạn. Khi người khác đọc 
#vào họ có thể dễ dàng hiểu được những nội dung, ý tưởng đó.
# - Một mã nguồn mở, một dự án lớn đều luôn luôn có các comment trong đó. 
# - Nhìn qua các dòng comment, chúng ta cũng có thể 
#đánh giá được người lập trình viên viết đoạn mã nguồn này có kĩ năng code hay không.


# II. BIẾN
# - Tên biến chỉ chứa các chữ cái và dấu '_'
# - Trong python có phân biệt chữ in hoa và in thường 
# - Khi khởi tạo biến thì tên biến phải tránh những từ khóa sau:
# and as assert break class continue def del elif else except exec finally for from 
# global if import in is lambda not or pass print raise return try while with yield
# - Khi khai báo biến chúng ta chỉ cần khai báo 'tên biến'='giá trị'
tuoi = 18 
print(tuoi) 


# III. Kiểu dữ liệu
# Các kiểu dữ diệu khá giống trong c++
# - Để xem kiểu dữ liệu chúng ta dùng hàm type()
print(type(tuoi))
# - Trong python kiểu dữ liệu số nguyên có thể lưu trữ vô hạn
# - Khi làm việc với số thực nên sử dụng Decimal để có kết quả chính xác hơn 
# - Để sử dụng Decimal thì làm như sau
from decimal import *
# - Hàm getcontext().prec dùng để lấy chính xác số chữ số ở trước và sau dấu phẩy 
getcontext().prec=3
print(Decimal(10)/3)
# Để tạo phân số thì dùng hàm Fraction() như sau 
from fractions import *
# Phân số thu được sẽ nằm dưới dạng tối giản 
phan_so=Fraction(1,4)
print(phan_so)
# Để tạo 1 số phức thì dùng hàm complex()
so_phuc=complex(1,3)
print(so_phuc)
# In ra phần thực số phức 
print(so_phuc.real)
# In ra phần ảo số phức 
print(so_phuc.imag)

