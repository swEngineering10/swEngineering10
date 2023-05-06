import bcrypt  # 해시화된 비밀번호를 만들거나 비밀번호가 올바른지 확인하는 함수들이 있는 bcrypt 모듈을 가져옵니다.


#  함수는 받은 문자열 비밀번호를 utf-8로 인코딩한 후, salt값을 생성하여 bcrypt로 해시화한 결과를 반환합니다.
def hash_password(password: str) -> bytes:
    return bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt())

# 함수는 받은 문자열 비밀번호와 이미 해시화된 비밀번호를 비교하여 올바른지 여부를 불리언 값으로 반환합니다. 이때, 받은 문자열 비밀번호는 utf-8로 인코딩되어야 하며, 해시화된 비밀번호는 bytes 형태로 전달되어야 합니다.
def check_password(password: str, hashed_password: bytes) -> bool:
    return bcrypt.checkpw(password.encode("utf-8"), hashed_password)
