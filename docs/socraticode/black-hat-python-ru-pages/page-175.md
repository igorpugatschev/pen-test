# Black Hat Python. Программирование для хакеров и пентестеров — страница 175

Источник: `Black Hat Python. Программирование для хакеров и пентестеров.pdf`

Шифрование и расшифровка файлов   175
Прежде чем заняться шифрованием и расшифровкой данных, мы должны
создать открытый и закрытый ключи для асимметричного алгоритма RSA.
То есть нужно написать функцию для генерации RSA-ключей. Добавим в файл
cryptor.py функцию generate:
def generate():
    new_key = RSA.generate(2048)
    private_key = new_key.exportKey()
    public_key = new_key.publickey().exportKey()
    with open('key.pri', 'wb') as f:
        f.write(private_key)
    with open('key.pub', 'wb') as f:
        f.write(public_key)
Все верно, Python — настолько крутой язык, что на нем это можно уместить
всего в несколько строк кода. Данная функция записывает закрытый и от-
крытый ключи в файлы с именами key.pri и key.pub. Т еперь давайте напишем
небольшую вспомогательную функцию для получения любого из этих ключей:
def get_rsa_cipher(keytype):
    with open(f'key.{keytype}') as f:
        key = f.read()
    rsakey = RSA.importKey(key)
    return (PKCS1_OAEP.new(rsakey), rsakey.size_in_bytes())
Мы передаем этой функции тип ключа (pub или pri), читаем соответствующий
файл и возвращаем шифр и размер RSA-ключа в байтах.
Итак, мы сгенерировали два ключа и написали функцию, которая возвраща-
ет шифр, сформированный на их основе. Т еперь приступим к шифрованию
данных:
def encrypt(plaintext):
    compressed_text = zlib.compress(plaintext) 
    session_key = get_random_bytes(16) 
    cipher_aes = AES.new(session_key, AES.MODE_EAX)
    ciphertext, tag = cipher_aes.encrypt_and_digest(compressed_text) 
    cipher_rsa, _ = get_rsa_cipher('pub')
    encrypted_session_key = cipher_rsa.encrypt(session_key) 
    msg_payload = encrypted_session_key + cipher_aes.nonce + tag + ciphertext 
    encrypted = base64.encodebytes(msg_payload) 
    return(encrypted)
