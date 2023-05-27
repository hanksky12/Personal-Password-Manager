import json
import os
import cryptography
from .encrypt import Encrypt
from .otp import Otp


class File:

    def __init__(self, _file_path='password.txt'):
        print("===========Start===========")
        self._user = None
        self._data = None
        self._password = None
        self._password2 = None
        self._file_path = _file_path
        if os.path.exists(_file_path):
            self._open()
        else:
            self._create()



    def reset_password(self):
        print("===========重新設定密碼(reset_password)===========")
        self._init_two_password()
        self._make_qr_code()
        self._save_file()

    def insert(self):
        print("===========新增紀錄(new_record)===========")
        id = str(self._latest_id() + 1)
        name = input("請输入新增帳號new account：")
        password = input("請输入密碼new account_pass：")
        self._data["data"].append(
            {
                "id": id,
                "name": name,
                "password": password
            })
        self._save_file()
        print(f"===========已新增id={id}紀錄===========")

    def update(self):
        print("===========修改紀錄(update_record)===========")
        print("不修改請按Enter(if not modify press Enter)")
        _id = input("請輸入id：")
        _name = input("請輸入新帳號update account：")
        _password = input("請輸入新密碼update account_pass：")
        for item in self._data["data"]:
            if item["id"] == _id:
                item["name"] = _name if _name else item["name"]
                item["password"] = _password if _password else item["password"]
                self._save_file()
                print(f"===========已修改id={_id}紀錄===========")
                break
        else:
            print("id不存在 id not found")

    def delete(self):
        print("===========刪除紀錄(delete_record)===========")
        _id = input("請輸入id：")
        is_check = input("確認y 取消n：")
        if is_check == "n":
            print("取消刪除(cancel delete)")
            exit()
        for item in self._data["data"]:
            if item["id"] == _id:
                self._data["data"].remove(item)
                self._save_file()
                print(f"===========已刪除id={_id}紀錄===========")
                break

    def _open(self):
        self._password = input("請输入第一段密碼(first_pass)：")
        self._password2 = input("請输入第二段密碼(second_pass)：")
        otp = Otp(self._password)
        for times in range(3):
            if otp.is_pass():
                self._open_file()
                break
            else:
                print(f"otp驗證第{times + 1}失敗failed")
        else:
            print("otp失敗次數過多failed too many times")
            exit()

    def _create(self):
        print("===========初始設定 init===========")
        self._init_two_password()
        self._user = input("請输入姓名your name：")
        self._make_qr_code()
        self._data = {
            "user": self._user,
            "data": []
        }

    def _latest_id(self):
        id = 0
        for item in self._data["data"]:
            if int(item["id"]) > id:
                id = int(item["id"])
        return id

    def _pretty_json(self, _data):
        print(json.dumps(_data, indent=4, ensure_ascii=False))

    def _init_two_password(self):
        self._password = input("請設定第一段檔案密碼(set first_pass)：")
        if len(self._password) < 8:
            print("密碼長度不足(length not enough)")
            exit()
        _check_password = input("請再次輸入第一段檔案密碼(first_pass check)：")
        self._check_two_password(self._password, _check_password)
        self._password2 = input("請設定第二段檔案密碼(set second_pass)：")
        _check_password2 = input("請再次輸入第二段檔案密碼(second_pass check)：")
        self._check_two_password(self._password2, _check_password2)

    def _check_two_password(self, password1, password2):
        if password1 != password2:
            print("密碼不一致password not equal !!!")
            exit()

    def _open_file(self):
        try:
            print("===========open file===========")
            with open(self._file_path, 'rb') as file:
                encrypted_data = file.read()
                encrypt = Encrypt(self._password, self._password2)
                self._data = encrypt.decrypt(encrypted_data)
                self._user = self._data["user"]
                self._pretty_json(self._data)
        except cryptography.fernet.InvalidToken as e:
            print("密碼錯誤wrong password!!!")
            exit()

    def _save_file(self):
        print("===========save file===========")
        self._pretty_json(self._data)
        encrypt = Encrypt(self._password, self._password2)
        encrypted_data = encrypt.encrypt(self._data)
        with open(self._file_path, 'wb') as file:
            file.write(encrypted_data)

    def _make_qr_code(self):
        print("===========new QRCode===========")
        otp = Otp(self._password)
        otp.make_qr_code(self._user, self._user)


    def __del__(self):
        print("===========TheEnd==========\n===========By!=ByHank~==========")