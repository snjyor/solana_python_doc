### solders.keypair.Keypair.pubkey
从密钥对中获取公钥。

```python
from solders.keypair import Keypair

mnemonic = "lawsuit dirt click opinion silent element autumn shed junk such heart lake"
sender_keypair = Keypair.from_seed_phrase_and_passphrase(mnemonic, "")
pubkey = sender_keypair.pubkey()
print(pubkey)  # Fm1BJFQt9VEbxicRxaAcKjMVGiHAqxvq1m2UQ6eztCjb
```
