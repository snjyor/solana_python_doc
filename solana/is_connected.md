### solana.rpc.api.Client.is_connected
连接状态检查，判断是否正确连接到 Solana RPC 节点。

```python
from solana.rpc.api import Client

client = Client("http://localhost:8899")
connected = client.is_connected()
print(connected)  # True
```
