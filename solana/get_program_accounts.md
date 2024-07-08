
### solana.rpc.api.Client.get_program_accounts
根据指定的程序账户公钥，获取其拥有控制权的所有账户信息，返回的结果是一个列表，包含了所有的账户信息
```python
from solana.rpc.api import Client
from solders.pubkey import Pubkey

client = Client("http://localhost:8899")
demo_pubkey = Pubkey.from_string("1"*32)
program_accounts = client.get_program_accounts(demo_pubkey)
print(program_accounts)
# GetProgramAccountsResp([RpcKeyedAccount { pubkey: Pubkey(7mZVNkgJ19gz3tauPCCXf8N9YDb1PiWeFyKa4d23FyDU), account: Account { lamports: 195075656800, data: [], owner: Pubkey(11111111111111111111111111111111), executable: false, rent_epoch: 18446744073709551615 } }, ……])
print([value.account.lamports/10**9 for value in program_accounts.value])
# [195.0756568, 48.01, 499.7378825, 500000000.0, 1907.119955, 997803.99994, 42.87]
```
