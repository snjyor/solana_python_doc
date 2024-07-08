# 生成助记词
使用 pybip39 库生成助记词并保存，后续会用到。
```python
from pybip39 import Mnemonic
from solders.keypair import Keypair

mnemonic = Mnemonic()
phrase = mnemonic.phrase
print(mnemonic.phrase)  # athlete ordinary improve quit crop hobby normal session deer motor original fine

demo_keypair = Keypair.from_seed_phrase_and_passphrase(phrase, "")
demo_pubkey = demo_keypair.pubkey()
print(demo_pubkey)  # 4YXGAJ5GqCry1MXLrWc7iSAoZcn6Lq458UzUXJ1EdoFf
```

# 空投
在启动了solana节点的前提下，先直接使用以下代码对你的钱包进行空投，代码方法后续会详细介绍。
```python
from solana.rpc.api import Client
from solders.pubkey import Pubkey


def airdrop(rpc_url: str, address: str, amount: float):
    client = Client(rpc_url)
    payer_pubkey = Pubkey.from_string(address)
    lamport = amount * 10**9
    transfer_hash = client.request_airdrop(payer_pubkey, lamport).value
    print(transfer_hash)
    return transfer_hash


if __name__ == '__main__':
    sol = airdrop(
        "http://localhost:8899",
        "4YXGAJ5GqCry1MXLrWc7iSAoZcn6Lq458UzUXJ1EdoFf",
        666  # 需要空投的数量
    )
```

