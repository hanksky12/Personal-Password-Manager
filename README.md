# Personal Password Manager 個人密碼管理工具

---
## Description
Use two-stage manager password plus Multi-factor authentication, three locks to protect all your private account password management

使用兩段式管理密碼加上MFA，三道鎖保護你的所有私人帳戶密碼管理

### First two passwords
After setting two sets of passwords, please keep them hidden, the program does not store your passwords in any way

前兩道密碼在設定兩組密碼後，請藏好記住，程式沒有以任何方式儲存你的密碼

### MFA
After setting the password, the program will automatically generate the QRcode used by MFA. Please scan it with Google Authenticator(or others) on your mobile phone and delete the picture to ensure that only your mobile phone can unlock the third lock

在設定密碼後會自動生成MFA使用的QRcode，請用手機的Google Authenticator(或其他類似的)掃描，並刪除圖片，確保只有你的手機可以解除第三道鎖


## How to use
1. docker-compose up -d
2. docker exec -it <container ID> bash
3. python app.py

### insert
insert new account and password (新增帳號密碼)

### update
update account and password by id (更新帳號密碼)

### delete
delete account and password by id (刪除帳號密碼)

### reset_password
reset two manger password & MFA QRcode (重置兩道管理密碼和MFA QRcode)


