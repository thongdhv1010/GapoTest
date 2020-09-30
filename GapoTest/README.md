<h2 id="title">Lession_1</h2>
-  python3
- Run:
    python3.5 lession_1.py


<h2 id="title">Lession_2</h2>
<h3>I. Giải thích thuật toán: </h3>
- Sử dụng thuật toán tìm kiếm Rabin Karp
- Giải thích: 
Thuật toán sử  phương pháp băm (hashing), mỗi xâu sẽ được gán với 1 giá trị của hàm băm,
ví dụ xâu "Bán hàng online" được gán với giá trị 2, và 2 xâu được gọi là bằng nhau nếu giá
trị băm của nó bằng nhau. Như vậy thay vì việc phải so sánh xâu con của đoạn văn bản với 
từ ngữ cần check, ta so sánh giá trị băm của chúng và đưa ra kết quả. 
- Đặc điểm:
    - Thực hiện trái qua phải
    - Có pha tiền xử lí với độ phức tạp O(m)
    - Độ phức tạp xấu nhất O(mn) mong đợi O(m+n)
- Input:
    - Xâu mẫu x=(x0,x1,…,xm-1) độ dài m
    - Xâu văn bản: y= (y0, y1,…, yn-1) độ dài n
- Ouput: tất cả các vị trí của x trong y

<h3>II. Doc API </h3>
<h4>1. Api set từ ngữ xấu </h4>
- URI: [host]/define/word/bad
- Method: POST
- BODY: 
<table>
    <tr>
        <th>Field</th>    
        <th>Type</th>    
        <th>Description</th>    
    </tr>
    <tr>
        <td>words_bad</td>
        <td>Array</td>
        <td>Danh sách các từ ngữ xấu</td>
    </tr>
</table>
- Body Example:

```
{
    "words_bad": [
        "Bán hàng online",
        "Gửi mình ảnh nude",
        "Gâu gâu"
    ]
}
```
- Curl
```
curl --location --request POST '0.0.0.0:19931/define/word/bad' \
--header 'Content-Type: application/json' \
--data-raw '{
    "words_bad": [
        "Bán hàng online",
        "Gửi mình ảnh nude",
        "Gâu gâu"
    ]
}'
```

<h4>2. Api kiểm tra từ ngữ xấu trong đoạn văn bản</h4>
- URI: [host]/check_paragraph
- Method: POST
- BODY: 
<table>
    <tr>
        <th>Field</th>    
        <th>Type</th>    
        <th>Description</th>    
    </tr>
    <tr>
        <td>paragraph</td>
        <td>String</td>
        <td>Nội dung đoạn văn bản cần kiểm </td>
    </tr>
</table>
- Body Example:

```
{
    "paragraph": "Bán hàng online là bạn sẽ bán hàng nhưng không có cửa hàng, HOẶC có cửa hàng nhưng việc quảng bá sản phẩm thông qua kênh online., và khách hàng cũng sẽ đặt hàng online.Bạn không biết Bán hàng online thì nên bán gì cho hiệu quả ? Thật ra, bán hàng online nó không có gì quá to tát đâu bạn, nó như bạn bán hàng bình thường ở ngoài thôi.Nhưng đặc biệt hơn là bạn sẽ tiếp cận khách hàng qua kênh online, là xu hướng và tiềm năng mới trong kinh doanh khi việc kinh doanh truyền thống quá đắt đỏ."
}
```
- Curl
```
curl --location --request POST '0.0.0.0:19931/check_paragraph' \
--header 'Content-Type: application/json' \
--data-raw '{
    "paragraph": "Bán hàng online là bạn sẽ bán hàng nhưng không có cửa hàng, HOẶC có cửa hàng nhưng việc quảng bá sản phẩm thông qua kênh online., và khách hàng cũng sẽ đặt hàng online.Bạn không biết Bán hàng online thì nên bán gì cho hiệu quả ? Thật ra, bán hàng online nó không có gì quá to tát đâu bạn, nó như bạn bán hàng bình thường ở ngoài thôi.Nhưng đặc biệt hơn là bạn sẽ tiếp cận khách hàng qua kênh online, là xu hướng và tiềm năng mới trong kinh doanh khi việc kinh doanh truyền thống quá đắt đỏ."
}'
```

- Response:
<table>
    <tr>
        <th>Field</th>    
        <th>Type</th>    
        <th>Description</th>    
    </tr>
    <tr>
        <td>result </td>
        <td>Array </td>
        <td>Danh sách các từ ngữ xấu có trong đoạn văn bản </td>
    </tr>
    <tr>
        <td>result.location</td>
        <td>Array </td>
        <td>Danh sách vị trí xuất hiện các từ ngữ xấu </td>
    </tr>
    <tr>
        <td>result.word_bad </td>
        <td>String </td>
        <td>Nội dung từ ngữ xấu </td>
    </tr>
</table>

- Response Example:

```
{
    "result": [
        {
            "location": [
                0,
                183
            ],
            "word_bad": "Bán hàng online"
        }
    ]
}
```

<h4>III. Cài đặt</h4>
- Yêu cầu:
    - Python3
    - Redis 
- Thông tin config redis trong bài hiện tại:
    - Config: src/general/redis_config.py
    - host: localhost
    - port: 6379
- Cài đặt các thư viện cần sử dụng: pip3.5 install -r requirements.txt 
- Run app: python3.5 lession_2.py
