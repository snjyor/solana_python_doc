### solders.keypair.Keypair.from_seed_and_derivation_path
# 从种子和派生路径创建密钥对。派生路径是一个字符串，例如 "m/44'/501'/0'/0'"。
# - 44' 是 BIP44 标准规定的硬化路径。
# - 501' 是 Solana 的币种编号（SLIP44标准中 Solana 的 ID 是 501）。
# - 0' 和 0 是账户索引和变体索引，通常用于生成主账户。


from solders.keypair import Keypair
demo_keypair = [212,232,237,180,136,254,44,53,57,6,149,58,97,53,64,
                93,151,38,207,41,76,21,251,53,116,53,117,197,95,210,
                191,71,100,144,105,175,247,137,234,220,140,236,9,114,
                168,122,178,77,126,65,239,102,83,186,4,89,77,73,148,
                197,74,35,150,35]  # 64 bytes
derive_path = "m/44'/501'/0'/0'"  # 主账户
demo_pubkey = Keypair.from_seed_and_derivation_path(demo_keypair, derive_path).pubkey()
print(demo_pubkey)  #Fvr5dcMCXY2bMy4mTxHyD7WoPausWnLHYtKDCzjffrQR
derive_path2 = "m/44'/501'/0'/0/0"  # 子账户
demo_pubkey2 = Keypair.from_seed_and_derivation_path(demo_keypair, derive_path2).pubkey()
print(demo_pubkey2)  # HpX9bdM9scDS31w74u7ntd6ni9vwjvXv6W9i67Xk9FtZ
derive_path3 = "m/44'/501'/0'/0/1"  # 子账户
demo_pubkey3 = Keypair.from_seed_and_derivation_path(demo_keypair, derive_path3).pubkey()
print(demo_pubkey3)  # 6tR16P1qs2qhiAW7Bok4Gm3P5CMVehzGtJLEb3Nne6x9

