### solders.keypair.Keypair.sign_message
使用密钥对进行消息签名

```python
from solana.rpc.api import Client
from solders.keypair import Keypair

client = Client("http://localhost:8899")
demo_keypair = Keypair.from_seed_phrase_and_passphrase("lawsuit dirt click opinion silent element autumn shed junk such heart lake", "")
sign_msg = demo_keypair.sign_message(b'hello solana')
transaction = client.get_transaction(sign_msg)
print(transaction)  # GetTransactionResp(None)

```


