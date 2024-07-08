
### solana.rpc.api.Client.get_multiple_accounts
获取多个账户的信息。
```python
from solana.rpc.api import Client
from solders.pubkey import Pubkey

client = Client("http://localhost:8899")
addresses = [
    "CnMdLhM1hH6nT8ekAQsLgZ9vigphriWiLbyHTkXnMc8B",
    "EBziZDuZwJNSMx57fZFqgzXVLssWZSLMQzweVkGzRdVv",
    "Acs42Xv9kxuVBUeTCN85Vw1cYiiEsCDyaFHnc7rs5YCB"
]
pubkeys = [Pubkey.from_string(address) for address in addresses]
accounts = client.get_multiple_accounts(pubkeys)
print(accounts)
# GetMultipleAccountsResp {
#   context: RpcResponseContext { slot: 52164, api_version: Some("1.17.25") }, value:
#       [Some(Account { lamports: 499740992500, data: [], owner: Pubkey(11111111111111111111111111111111),
#               executable: false, rent_epoch: 18446744073709551615 }),
#       Some(Account { lamports: 1907119955000, data: [], owner: Pubkey(11111111111111111111111111111111),
#               executable: false, rent_epoch: 18446744073709551615 }),
#       Some(Account { lamports: 48010000000, data: [], owner: Pubkey(11111111111111111111111111111111),
#               executable: false, rent_epoch: 18446744073709551615 })] }
print([value.lamports/10**9 for value in accounts.value])
# [499.7399025, 1907.119955, 48.01] 单位 SOL
```
