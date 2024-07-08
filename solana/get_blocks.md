### solana.rpc.api.Client.get_blocks
获取两个区块之间的区块列表。
```python
from solana.rpc.api import Client

client = Client("http://localhost:8899")
blocks = client.get_blocks(49970,49980)
print(blocks)
# GetBlocksResp([49970, 49971, 49972, 49973, 49974, 49975])
```
