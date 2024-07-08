
### solana.rpc.api.Client.get_latest_blockhash
获取最新的区块哈希值。
```python
from solana.rpc.api import Client

client = Client("http://localhost:8899")
latest_blockhash = client.get_latest_blockhash()
print(latest_blockhash.value.blockhash)  # 55wn8fYeUVjshxubJJrvBsx9a2nzdiWzKoXotUB1zRoj
```
