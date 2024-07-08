### solders.keypair.Keypair.from_seed
# 从种子创建密钥对。可以与from_bytes 进行对比，发现用到的字节序列是一样的。只是from_seed只用了前32个字节。得到的公钥也是一样的。


from solders.keypair import Keypair
demo_keypair = [212,232,237,180,136,254,44,53,57,6,149,58,97,53,64,
                93,151,38,207,41,76,21,251,53,116,53,117,197,95,210,
                191,71,100,144,105,175,247,137,234,220,140,236,9,114,
                168,122,178,77,126,65,239,102,83,186,4,89,77,73,148,
                197,74,35,150,35]  # 64 bytes
demo_pubkey = Keypair.from_seed(demo_keypair[:32]).pubkey()
print(demo_pubkey)  #7mZVNkgJ19gz3tauPCCXf8N9YDb1PiWeFyKa4d23FyDU

