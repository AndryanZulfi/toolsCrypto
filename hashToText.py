import hashlib

def hash_to_text(hash_value):
    try:
        # Mendeklarasikan objek hash menggunakan algoritma MD5
        hash_object = hashlib.md5()
        
        # Mengubah nilai hash dalam bentuk string hexadecimal menjadi byte
        hash_bytes = bytes.fromhex(hash_value)
        
        # Memasukkan nilai hash ke dalam objek hash
        hash_object.update(hash_bytes)
        
        # Mendapatkan teks dari nilai hash
        text = hash_object.digest()
        
        # Mengembalikan teks dalam bentuk string
        return text.decode()
    except ValueError:
        return "Hash value tidak valid"

# Contoh penggunaan
hash_value = "e82a4b4a0386d5232d52337f36d2ab73"  # Contoh nilai hash (MD5)
text = hash_to_text(hash_value)
print("Teks dari nilai hash", hash_value, "adalah:", text)