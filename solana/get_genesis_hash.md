
### solana.rpc.api.Client.get_genesis_hash
获取当前区块链的创世哈希。在运行本地节点的终端界面上可以看到创世哈希值。
```python
from solana.rpc.api import Client

client = Client("http://localhost:8899")
genesis_hash = client.get_genesis_hash()
print(genesis_hash)
# GetGenesisHashResp(Hash(5yPZYrZvZ34TpKs8xGRe1M5wibB8vxGZTNPiMnLS6bjB))
print(genesis_hash.value)
# 5yPZYrZvZ34TpKs8xGRe1M5wibB8vxGZTNPiMnLS6bjB
```
