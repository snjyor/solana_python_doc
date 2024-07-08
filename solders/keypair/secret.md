### solders.keypair.Keypair.secret
从密钥对中获取私钥。下列代码对比了用助记词得到的公钥和使用私钥得到的公钥，发现是一样的。

```python
from solders.keypair import Keypair
mnemonic = "lawsuit dirt click opinion silent element autumn shed junk such heart lake"
demo_keypair = Keypair.from_seed_phrase_and_passphrase(mnemonic, "")
pubkey = demo_keypair.pubkey()
print(pubkey)  # Fm1BJFQt9VEbxicRxaAcKjMVGiHAqxvq1m2UQ6eztCjb
secret = demo_keypair.secret()
print(secret)
# b',*\xc8\x85\x0e\x8a\xff\xf5O$1\x99\xc0\xc8J\x1aU.\xd7\xca\xf6|\xde\xa7\xfa2\xbf\xbfK\xce\xcby'
pubkey = Keypair.from_seed(secret).pubkey()
print(pubkey)  # Fm1BJFQt9VEbxicRxaAcKjMVGiHAqxvq1m2UQ6eztCjb
assert demo_keypair.pubkey() == pubkey  # True

```
