import base64
import pyotp
import qrcode

class Otp:
    def __init__(self, _password):
        base32_key = base64.b32encode(_password.encode()).decode()
        # print(base32_key)
        self._otp = pyotp.TOTP(base32_key)

    def is_pass(self):
        phone_otp = input("請输入OTP驗證碼：")
        return self._otp.now() == phone_otp

    def make_qr_code(self, _user_name, _issuer_name):
        otp_uri = self._otp.provisioning_uri(name=_user_name, issuer_name=_issuer_name)
        qr_code = qrcode.make(otp_uri)
        qr_code.save('qr_code.png')



if __name__ == '__main__':
    otp = Otp("1")
    otp.make_qr_code("user", "issuer")
