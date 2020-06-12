---
title: "Collections với C#"
date: 2020-06-10T15:27:41+07:00
draft: false
---

Bài viết này sẽ giới thiệu về một vài lớp thường dùng của thư viện
collections của C#. Sau đó là hướng dẫn chi tiết cách tự viết lại
những lớp tương tự với mục đích minh họa các tính năng của ngôn ngữ
C#. Để có thể đọc hiểu bài này nên đọc bài [C#](/csharp) trước.

## Nhắc lại về kiểu dữ liệu trừu tượng và cấu trúc dữ liệu
Môn cấu trúc dữ liệu dạy những cấu trúc như danh sách (list),
ngăn xếp (stack), hàng đợi (queue), bảng băm (hash table),
đủ thứ cây, ... Nội dung bài học khá là loạn vì không phân rõ
giữa kiểu dữ liệu trừu tượng và cấu trúc dữ liệu.

Kiểu dữ liệu trừu tượng là mô tả về khả năng của kiểu dữ liệu
(chẳng hạn như stack có thể thêm vào đỉnh và cũng chỉ có thể
lấy ra từ đỉnh), còn cấu trúc dữ liệu quan tâm đến việc đáp ứng
các khả năng được hứa hẹn đó. Những điểm chung của các cấu trúc
dữ liệu được tập hợp lại thành kiểu dữ liệu trừu tượng.

Dưới đây sẽ tóm tắt về các kiểu dữ liệu trừu tượng

## Các kiểu dữ liệu trừu tượng
### Danh sách (List)
Kiểu này rất thường được sử dụng. Nó hứa hẹn khá nhiều, cụ thể là
một danh sách có thể:
- Thêm phần tử vào vị trí bất kỳ.
- Xóa phần tử bất kỳ khỏi danh sách.
- Đọc giá trị của phần tử ở vị trí bất kỳ trong danh sách.
- Tìm xem danh sách có chứa một giá trị nào đó hay không.
- Duyệt qua từng phần tử trong danh sách.
- Đếm số phần tử trong danh sách.

### Ngăn xếp (Stack)
Kiểu này hạn chế hơn, một ngăn xếp chỉ có thể:
- Thêm phần tử vào đỉnh.
- Xóa phần tử khỏi đỉnh.
- Đọc giá trị phần tử ở đỉnh.
- Đếm số phần tử trong ngăn xếp.

Ngăn xếp có đặc điểm là vào trước ra sau (FILO — First In Last Out).

### Hàng đợi (Queue)
Tương tự như ngăn xếp (chỉ khác 1 chỗ), hàng đợi cũng chỉ có thể:
- Thêm phần tử vào cuối hàng.
- Xóa phần tử ở đầu hàng.
- Đọc giá trị phần tử ở đầu hàng.
- Đếm số phần tử trong hàng đợi.

Hàng đợi có đặc điểm là vào trước ra trước (FIFO — First In First Out).

### Hàng đợi hai đầu (Deque)
Hàng đợi với khả năng thêm và xóa ở cả 2 đầu gọi là Deque.

### Tập hợp (Set)
Cái này thì quá quen rồi, y như bên Toán, tập hợp có thể:
- Thêm phần tử mới vào tập hợp.
- Xóa phần tử trong tập hợp.
- Kiểm tra xem một giá trị nào đó có trong tập hợp hay không.
- Đếm số phần tử trong tập hợp.
- Duyệt qua các phần tử.

Tập hợp có đặc điểm là một đối tượng chỉ được xuất hiện đúng một lần,
nếu đã có trong tập hợp thì có thêm vào nó cũng không làm gì.

### Ánh xạ (Map) / Từ điển (Dictionary) / Mảng kết hợp (Associative array)
Tên thứ ba chỉ thấy PHP xài thôi, còn mấy ngôn ngữ khác đều dùng từ Map
hoặc Dictionary thôi. Cấu trúc dạng này có đặc điểm:
- Lưu dữ liệu theo từng cặp khóa — giá trị.
- Khóa không trùng nhau.

Cấu trúc này có thể:
- Thêm một cặp khóa — giá trị vào.
- Lấy ra một cặp thông qua khóa.
- Xóa cặp có khóa bằng với một giá trị nào đó.
- Tìm cặp khóa — giá trị có khóa được chỉ định.
- Tìm cặp khóa — giá trị có giá trị được chỉ định.
- Đếm số cặp đang chứa.
- Duyệt qua các cặp khóa — giá trị.

## Nhắc lại về độ phức tạp thuật toán
Độ phức tạp thường được ký hiệu bằng ký pháp O lớn (Big-O notation),
ký pháp này thể hiện mối quan hệ giữa kích thước bài toán và thời gian
thực thi, dựa vào nó có thể biết được khi vấn đề lớn lên thời gian sẽ
thay đổi thế nào.

Các độ phức tạp thường gặp (log bên lập trình dùng đều là cơ số 2):
- O(1): Thời gian thực thi không phụ thuộc vào kích thước đầu vào.
Thường thì rất khó đạt được độ phức tạp như vầy.
- O(log n): Thời gian thực thi tăng theo cùng tốc độ tăng của logarithm
kích thước đầu vào. Độ phức tạp này cũng rất tốt.
- O(n): Thời gian thực thi tăng theo cùng tốc độ với kích thước đầu vào.
Những bài toán xử lý tất cả phần tử trong một collection đều cần phải
duyệt qua từng phần tử, và như vậy thì tụi nó đều có độ phức tạp tối thiểu
là O(n).
- O(n·log n): Ở độ phức tạp này thời gian thực thi sẽ tăng nhanh hơn O(n)
nhưng vẫn còn chấp nhận được.
- O(n<sup>2</sup>), O(n<sup>3</sup>), O(n<sup>4</sup>): Ở những độ phức tạp
này thời gian thực thi sẽ tăng lên khá nhanh.
- O(2<sup>n</sup>): Đến độ phức tạp như vầy rồi thì thời gian thực thi tăng cực
kỳ nhanh. Thuật toán có độ phức tạp này chỉ có thể xử lý đầu vào cực nhỏ (tầm vài
chục đến vài trăm). Để dễ hình dung hơn, xem ví dụ này: Một thuật toán nào đó cần
thực hiện 2<sup>n</sup> chỉ thị. Giả sử máy tính có 16 core, mỗi core có thể xử lý
4 tỉ phép tính mỗi giây, tức là mỗi giây máy tính thực hiện được 64 tỉ phép tính.
Với n = 100 thì 2<sup>100</sup> là 1 267 650 600 228 229 401 496 703 205 376, cần
19 807 040 628 566 085 632 giây để chạy xong thuật toán đó. Đổi ra ngày thì nó sẽ
là 229 248 155 423 218 ngày, hay đổi ra năm thì sẽ là 627 647 242 774 năm (tính theo
1 năm = 365.25 ngày). Nếu mình còn sống tiếp được 100 năm thì cần có 6 276 472 428
(hơn 6 tỉ) máy tính mạnh như mô tả ở trên để có thể chạy xong thuật toán này trước
khi mình chết.

Một điểm rất quan trọng cần nhớ là độ phức tạp **không phải hàm thời gian**,
nó chỉ thể hiện quan hệ giữa kích thước đầu vào và thời gian thực hiện thôi.
Một thuật toán có độ phức tạp O(1) vẫn có thể chạy chậm hơn thuật toán có
độ phức tạp O(n) nếu dữ liệu không đủ lớn. Lý do là độ phức tạp không bao gồm
phần hằng số. Ví dụ cần tìm nhà môt người, bài toán chỉ cho phạm vi có cái nhà
cần tìm, nếu mình hỏi từng người trong khu vực đó để tìm cái nhà thì đó là thuật
toán có độ phức tạp O(n), nhưng mà nếu mình đi hỏi hết 7 tỉ người trên thế giới
này để tìm ra cái nhà thì nó là thuật toán có độ phức tạp O(1), tại vì khu vực
mà đề khoanh vùng ra có rộng hay hẹp thì cũng không vượt khỏi 7 tỉ người này được.

## Các cấu trúc dữ liệu
### Mảng (Array)
Mảng là kiểu có
- Các phần tử cùng kiểu và nằm liền nhau trên bộ nhớ.
- Kích thước cố định. Nếu muốn mở rộng mảng chỉ có thể tạo mảng mới
với kích thước lớn hơn rồi chép dữ liệu sang.
- Truy cập ngẫu nhiên (random access): Truy cập phần tử nào cũng mất
cùng một khoảng thời gian. Có được tính chất truy cập ngẫu nhiên này
đồng nghĩa với việc truy cập phần tử mảng là một thao tác O(1).

### Danh sách liên kết (Linked list)
Danh sách liên kết có đặc điểm
- Các phần tử có thể nằm rời rạc trên bộ nhớ, không liền nhau.
- Mỗi phần tử trỏ tới phần tử kế nó, hoặc một giá trị tượng trưng
(sentinel value) để đánh dấu kết thúc danh sách.
- Kích thước không bị giới hạn. Chỉ cần còn đủ bộ nhớ là danh sách
liên kết còn có thể lớn lên.
- Truy cập tuần tự (sequential access): Để đọc một phần tử nằm giữa
phải đi qua tất cả phần tử nằm trước nó. Vì tính tuần tự này nên
truy cập phần tử trong danh sách liên kết là một thao tác O(n).

### Bảng băm (Hash table)
Ý tưởng cơ bản của bảng băm là dữ liệu sẽ được đưa qua hàm băm
(hash function) để tính ra vị trí lưu nó. Hàm băm luôn có dạng
`f(x) mod n` với `x` là dữ liệu cần lưu, `f` là một hàm bất kỳ,
`mod` là phép chia dư (bên C# dùng dấu `%` cho phép toán này),
`n` là kích thước bảng băm.

Ví dụ chọn `f(x) = x` (tức là bỏ cái gì vào `f` thì nó cho ra giống
y vậy) thì hàm băm là `x mod n`. Nếu bảng băm kích thước là `5` và
cần thêm giá trị `123`, `456`, `789` vào bảng băm thì nó sẽ lưu vầy:

```
123 mod 5 = 3
456 mod 5 = 1
789 mod 5 = 4
```

Chỉ số|Giá trị
|:---:|:----:|
|  0  |  -   |
|  1  | 456  |
|  2  |  -   |
|  3  | 123  |
|  4  | 789  |

Trong tình huống tốt nhất, truy cập phần tử của bảng băm sẽ có độ
phức tạp bằng với độ phức tạp hàm băm, tức là có thể đạt tới O(1).
Tuy nhiên thực tế dữ liệu không tự né nhau ra như trong ví dụ trên,
sẽ có lúc dữ liệu khác nhau được băm ra cùng một vị trí, gọi là đụng độ
(collision). Có 2 giải pháp chính là dùng danh sách để lưu hoặc tìm chỗ
khác trên bảng băm để lưu. Vì bài này không lấy xây dựng cấu trúc dữ liệu
làm chủ đề chính nên sẽ không mô tả rõ cách thực hiện việc này.

### Các cấu trúc khác
Còn nhiều cấu trúc khác nữa, đa số là dạng cây: cây nhị phân tìm kiếm
(Binary Search Tree), cây đỏ–đen (red–black tree), cây AVL, ... Tuy
nhiên những cấu trúc này quá phức tạp để có thể nói trong một bài viết
ngắn như vầy.

## Collections — Cấu trúc dữ liệu trong thư viện chuẩn
Trong C#, các cấu trúc dữ liệu được thiết kế theo sơ đồ này:

TODO: Add diagram

## TODO
Collections, foreach
Implement collections
