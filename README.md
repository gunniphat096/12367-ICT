# 📋 ระบบเก็บสะสมความดี/กิจกรรมจิตอาสา (Volunteer Activity Logger)
ระบบสำหรับบันทึกและจัดการข้อมูลกิจกรรมจิตอาสา ด้วย Django Framework พร้อมฟอร์มบันทึกและตารางแสดงผลสวยงามด้วย Bootstrap 5
## 🔥 คุณสมบัติ (Features)
- 📄 ฟอร์มบันทึกกิจกรรม พร้อมระบบคำนวณจำนวนชั่วโมงอัตโนมัติ
- 🗂 แสดงตารางกิจกรรมที่เคยบันทึก
- 🖋 แก้ไข และลบข้อมูลกิจกรรม
- 📎 แนบไฟล์หลักฐาน หรือใส่ URL ได้
- 📱 รองรับการแสดงผลบนมือถือ (Responsive)
## 🛠 เทคโนโลยีที่ใช้ (Built With)
- Django - Python Web Framework
- Bootstrap 5 - Frontend Framework
- HTML5, CSS3, JavaScript (Vanilla)
## 📷 ตัวอย่างหน้าจอ (Screenshots)
### ฟอร์มบันทึกกิจกรรม
![3](https://github.com/user-attachments/assets/969e67ad-6dd5-4348-b30d-2c506f89d81c)
![4](https://github.com/user-attachments/assets/79b95135-8126-4f7a-b134-3a3130038ed2)
![5](https://github.com/user-attachments/assets/c570ebe6-c717-4d45-8e37-afd656e81b8e)
### ตารางกิจกรรม
![2](https://github.com/user-attachments/assets/69e0f4f8-9c5c-47a3-9a9e-fd108225f654)
![3](https://github.com/user-attachments/assets/a4b9b8ea-99a7-41b4-b7ae-c8781ca47d95)
![6](https://github.com/user-attachments/assets/7500bd76-d8c6-46c9-a9cc-1b7a83690b26)
## วิธีการติดตั้ง
1. Clone โปรเจกต์
2. สร้าง Virtual Environment
3. ติดตั้งแพ็กเกจ
4. รันเซิร์ฟเวอร์
```bash
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name
python -m venv venv
source venv/bin/activate  # หรือ venv\Scripts\activate บน Windows
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```
## 📁 โครงสร้างโปรเจกต์ (Project Structure)
```bash
/ชื่อโปรเจกต์
    /แอป
        templates/
            form.html
            list.html
        models.py
        views.py
        urls.py
    manage.py
    README.md
```
