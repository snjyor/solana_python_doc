### solana.rpc.api.Client.get_vote_accounts
前面有说过，solana 的一组助记词对应多个账户，如上面的质押账户，程序账户和普通账户，以及当前的投票账户。
```python
from solana.rpc.api import Client

client = Client("http://localhost:8899")
vote_accounts = client.get_vote_accounts()
print(vote_accounts.value.current[0].vote_pubkey)
# B2EoDTFWwSvZnkX5F8dPRKtUkZseu3hGgApe7PgNsdEQ
```
