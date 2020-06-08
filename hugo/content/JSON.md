---
title: "JSON"
date: 2020-06-09T01:08:18+07:00
draft: false
---

Có các kiểu object, array, string, boolean, number (cả số nguyên và số thực).

Mảng viết trong `[]`, object viết trong `{}`, string viết trong `""`
(**không** chấp nhận `'`), boolean với number viết trực tiếp ở ngoài được.

Object gồm các cặp khóa - giá trị, kiểu của khóa với giá trị không liên quan
gì nhau. Thường thì kiểu được dùng cho khóa là kiểu string.

```json
{
	"page": 1,
	"posts": [
		{
			"date": "1/1/2020",
			"title": "Hello world",
			"draft": false
		}
	]
}
```

Bên trên là 1 đoạn JSON thể hiện đủ các kiểu dữ liệu.

Ngoài cùng là một object với 2 cặp khóa - giá trị:
- Cặp thứ nhất có khóa là `"page"` (kiểu string) và giá trị là `1` (number).
- Cặp thứ hai cũng có khóa kiểu string, nhưng giá trị của nó là kiểu mảng.
Mảng này chỉ có 1 phần tử duy nhất, phần tử này là 1 object với 3 cặp
khóa - giá trị:
	- Khóa `"date"` (kiểu string) với giá trị `"1/1/2020"` (mặc dù nội dung
	của nó là ngày tháng năm nhưng mà kiểu nó vẫn là string).
	- Khóa `"title"` (string) với giá trị `"Hello world"` (string)
	- KHóa `"draft"` với giá trị là `false` (boolean)

Trong JSON **không có chú thích**, tuy nhiên có vài implementation sẽ chấp nhận
chú thích trong JSON (ví dụ như file `settings.json` của Visual Studio Code).

Tương tự, sau thành viên cuối cùng của array hoặc object không được có dấu phẩy,
mặc dù một vài implementation sẽ chấp nhận.
