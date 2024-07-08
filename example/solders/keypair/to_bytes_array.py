### solders.keypair.KeyPair.to_bytes_array
# 将密钥对转换为字节数组。下面的代码使用助记词生成了对应的字节序列
# 并对比了从字节序列中恢复出公钥，与直接使用助记词生成的公钥是一样的。


from solders.keypair import Keypair
mnemonic = "lawsuit dirt click opinion silent element autumn shed junk such heart lake"
demo_keypair = Keypair.from_seed_phrase_and_passphrase(mnemonic, "")
byte_array = demo_keypair.to_bytes_array()
print(byte_array)
# byte_array = [44, 42, 200, 133, 14, 138, 255, 245, 79, 36, 49, 153, 192, 200, 74, 
# 26, 85, 46, 215, 202, 246, 124, 222, 167, 250, 50, 191, 191, 75, 206, 203, 121, 
# 219, 73, 95, 145, 140, 219, 104, 0, 34, 200, 237, 211, 127, 28, 122, 190, 110, 
# 173, 120, 8, 10, 47, 201, 234, 79, 95, 41, 35, 176, 149, 78, 154]
print(Keypair.from_bytes(byte_array).pubkey())  # Fm1BJFQt9VEbxicRxaAcKjMVGiHAqxvq1m2UQ6eztCjb
print(demo_keypair.pubkey())  # Fm1BJFQt9VEbxicRxaAcKjMVGiHAqxvq1m2UQ6eztCjb
assert Keypair.from_bytes(byte_array).pubkey() == demo_keypair.pubkey() # True

