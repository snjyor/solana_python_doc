### solana.rpc.api.Client.get_minimum_balance_for_rent_exemption
获取免除账户租金所需的最低余额。
```python
from solana.rpc.api import Client

client = Client("http://localhost:8899")
rent_exemption = client.get_minimum_balance_for_rent_exemption(50)
print(rent_exemption.value)  # 1238880 lamport
print(rent_exemption.value/10**9)  # 0.00123888 sol
```
