
### solana.rpc.api.Client.get_block_commitment
该方法是查看区块高度的提交情况，参数为区块高度，如果该区块高度已经提交，则RpcBlockCommitment对象的commitment返回提交信息，否则返回 None。

```python
from solana.rpc.api import Client

client = Client("http://localhost:8899")
commit = client.get_block_commitment(48000)
print(commit)
# 区块高度48000已经提交的返回结果
# GetBlockCommitmentResp(RpcBlockCommitment(RpcBlockCommitment { commitment: Some([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 999999997717120]), total_stake: 999999997717120 }))
commit = client.get_block_commitment(48100)
print(commit)
# 区块高度48100未提交的返回结果
# GetBlockCommitmentResp(RpcBlockCommitment(RpcBlockCommitment { commitment: None, total_stake: 999999997717120 }))
```
