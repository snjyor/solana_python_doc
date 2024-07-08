### solders.keypair.Keypair.from_seed_phrase_and_passphrase
使用助记词和种子词汇创建密钥对。

```python
from solders.keypair import Keypair
mnemonic = "lawsuit dirt click opinion silent element autumn shed junk such heart lake"
demo_pubkey = Keypair.from_seed_phrase_and_passphrase(mnemonic, "").pubkey()
print(demo_pubkey)  # Fm1BJFQt9VEbxicRxaAcKjMVGiHAqxvq1m2UQ6eztCjb
```
