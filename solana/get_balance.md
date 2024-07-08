### solana.rpc.api.Client.get_balance
使用账户地址封装的公钥对象获取账户余额。公钥对象的具体内容在后面的章节中详细介绍。
> 在Solana链中，每个区块间隔(slot)约为0.4~0.8秒，而每个epoch周期包含43.2万个slot。

该方法返回的是一个 GetBalanceResp 对象，其中slot的值为运行程序时的 Finalized Slot，value的值为账户余额，单位为 lamport，1 Sol = 10^9 lamport。

```python
from solana.rpc.api import Client
from solders.pubkey import Pubkey

client = Client("http://localhost:8899")
demo_pubkey = Pubkey.from_string("EBziZDuZwJNSMx57fZFqgzXVLssWZSLMQzweVkGzRdVv")
balance = client.get_balance(demo_pubkey)
print(balance)
# GetBalanceResp { context: RpcResponseContext { slot: 46966, api_version: Some("1.17.25") }, value: 1907119955000 }
print(balance.value/10**9)
# 1907.119955  --> 这个值才是账户中显示的余额
```
