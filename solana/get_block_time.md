### solana.rpc.api.Client.get_block_time
该方法是查看区块时间，参数为区块高度，返回的是 GetBlockTimeResp 对象，其中value的值为区块时间戳。
```python
import datetime
from solana.rpc.api import Client

client = Client("http://localhost:8899")
block_time = client.get_block_time(48100)
print(block_time)
# GetBlockTimeResp(Some(1720148099))
print(block_time.value)
# 1720148099
print(datetime.datetime.fromtimestamp(block_time.value))
# 2024-07-05 10:54:59
```
