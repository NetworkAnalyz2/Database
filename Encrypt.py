from cryptography.fernet import Fernet


def encrypt_file(path): #path = r"F:\"の形で入力すること
    # keyの作成
    key = Fernet.generate_key()

    #キーをローカルに保存する
    with open(r"F:\NA\test_key.key", "wb") as key_data:
        key_data.write(key)

    #暗号化するファイルの取得
    with open(path , "r") as file:
        data = file.read()

    print("暗号化する前:", data)

    #データをバイトに変換する
    byte_data = data.encode()

    #Fernetオブジェクトの初期化
    f = Fernet(key)

    #バイトデータを暗号化する
    encrypt_data = f.encrypt(byte_data)

    #暗号化した情報をファイルに書き込む
    with open(path, "wb") as file:
        file.write(encrypt_data)

    print("暗号化した後:" , encrypt_data)


def decrypt_file(path):

    #キーの読み込み
    with open(r"F:\NA\test_key.key", "rb") as test_key:
        key = test_key.read()

    #暗号化したファイルの読み込み
    with open(path, "rb") as file:
        encrypt_data = file.read()

    print("暗号化された情報:", encrypt_data)

    #キーを使ってFernetオブジェクトを初期化
    f = Fernet(key)

    #データの復号化
    decrypt_data = f.decrypt(encrypt_data)

    print("複合化した情報:", decrypt_data.decode('utf-8'))

    with open(path, "wb") as file:
        file.write(decrypt_data)

data_path = r"F:\NA\test.txt"
decrypt_file(data_path)

