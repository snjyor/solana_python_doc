## solana.rpc.api.Client
实例化 solana.rpc.api.Client 类，用于连接到 Solana RPC 节点。

|网络|URL|
|---|---|
|主网|https://api.mainnet-beta.solana.com|
|开发网|https://api.devnet.solana.com|
|测试网|https://api.testnet.solana.com|
|本地|http://localhost:8899|

```python
from solana.rpc.api import Client

client = Client("http://localhost:8899")
```

### solana.rpc.api.Client.is_connected
连接状态检查，判断是否正确连接到 Solana RPC 节点。

```python
from solana.rpc.api import Client

client = Client("http://localhost:8899")
connected = client.is_connected()
print(connected)  # True
```

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

### solana.rpc.api.Client.get_account_info
账户信息内容与余额信息类似，但是返回的是 GetAccountInfoResp 对象，其中value的值为 Account 对象，包含了账户的详细信息。其中：
- lamports为账户余额
- data为账户数据
- owner为账户所有者
- executable为是否可执行，此账户为数据账户，只存储数据状态，不可执行
- rent_epoch为租金周期

```python
from solana.rpc.api import Client
from solders.pubkey import Pubkey

client = Client("http://localhost:8899")
demo_pubkey = Pubkey.from_string("EBziZDuZwJNSMx57fZFqgzXVLssWZSLMQzweVkGzRdVv")
info = client.get_account_info(demo_pubkey)
print(info)
# GetAccountInfoResp { 
#     context: RpcResponseContext { 
#         slot: 47658, api_version: Some("1.17.25") 
#     }, 
#     value: Some(Account { 
#         lamports: 1907119955000, 
#         data: [], 
#         owner: Pubkey(11111111111111111111111111111111), 
#         executable: false, 
#         rent_epoch: 18446744073709551615 
#     }) 
# }
```


### solana.rpc.api.Client.get_account_data
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


### solana.rpc.api.Client.get_block
该方法是查看区块信息，参数为区块高度，返回的是 GetBlockResp 对象，信息比较多，
值得留意的是transactions中的account_keys的值，其中包含了区块中节点公钥，程序账户和投票程序账户三个公钥信息。

meta 字段中包含了交易的元数据信息，其中包含了交易的签名信息，交易费用，交易状态等信息。

rewards 字段包含了本地节点作为打包交易节点和验证交易节点的奖励信息。
```python
from solana.rpc.api import Client

client = Client("http://localhost:8899")
block_info = client.get_block(48100)
print(block_info)
# GetBlockResp(
#   Some(
#       UiConfirmedBlock(
#           UiConfirmedBlock { 
#               previous_blockhash: "9tBjpytev5okapH9k3QL2ffRPaaUUubSF6vqJiAbY4M9", 
#               blockhash: "CSiY8nmJ1DKdsndbw7g5pKq1rDtyVU5jJvHnRwNbUZpH", 
#               parent_slot: 48099, 
#               transactions: Some(
#                   [EncodedTransactionWithStatusMeta { 
#                       transaction: Json(UiTransaction { 
#                           signatures: ["RmeajNAjiKPLyg8iW7RGSKStcbBxjqtGbJMUZ5ZNcQwpFWQ9hW91ri8hc8KnCM9xVUYuVDi5AEdcCpb9uZEU1Nw", "3gmAjB9cErhNWpmbipZT8zSCUwgNK3pyYQ8127pwjsUpwT3nqJbVhBGsp492tV4DgCDTCfVtBhDU1WH3hTdE5YAx"], 
#                           message: Raw(UiRawMessage { 
#                               header: MessageHeader { 
#                                   num_required_signatures: 2, num_readonly_signed_accounts: 0, num_readonly_unsigned_accounts: 1 
#                               }, 
#                           account_keys: ["CnMdLhM1hH6nT8ekAQsLgZ9vigphriWiLbyHTkXnMc8B", "B2EoDTFWwSvZnkX5F8dPRKtUkZseu3hGgApe7PgNsdEQ", "Vote111111111111111111111111111111111111111"], 
#                           recent_blockhash: "9tBjpytev5okapH9k3QL2ffRPaaUUubSF6vqJiAbY4M9", 
#                           instructions: [UiCompiledInstruction { 
#                               program_id_index: 2, accounts: [1, 1], 
#                               data: "Fk63PxRvoQJNufpJeHgetzEe1TqUakDdsB1sCC17RX6TSwSkiotWwQ2azFPEVpWEj7cS3sRzYxa3oCWW8aT7iTBFXBnuqreJ3wt1RLUw18eCpoFM2tjkZtcZZbYCZ28TTeSGtqBTQvtsdDZG1u94GGFny1a5Jo", 
#                               stack_height: None 
#                           }], 
#                           address_table_lookups: None 
#                       }) 
#                   }
#               ), 
#               meta: Some(
#                   UiTransactionStatusMeta { 
#                       err: None, status: Ok(()), fee: 10000, 
#                       pre_balances: [499761312500, 1000000000000000, 1], 
#                       post_balances: [499761302500, 1000000000000000, 1], 
#                       inner_instructions: Some([]), 
#                       log_messages: Some(["Program Vote111111111111111111111111111111111111111 invoke [1]", "Program Vote111111111111111111111111111111111111111 success"]), 
#                       pre_token_balances: Some([]), 
#                       post_token_balances: Some([]), rewards: Some([]), 
#                       loaded_addresses: Some(UiLoadedAddresses { writable: [], readonly: [] }), 
#                       return_data: Skip, compute_units_consumed: Some(2100) }), version: None 
#                   }
#               ]), 
#               signatures: None, 
#               rewards: Some([Reward { 
#                   pubkey: "CnMdLhM1hH6nT8ekAQsLgZ9vigphriWiLbyHTkXnMc8B", 
#                   lamports: 5000, post_balance: 499761307500, reward_type: Some(Fee), commission: None }]), 
#                block_time: Some(1720148099), block_height: Some(48097) }
#           )
#      )
# )
```

### solana.rpc.api.Client.get_recent_performance_samples
该方法返回最近性能样本的列表，性能样本每 60 秒采集一次，包括在这60秒的时间窗口中发生的交易和slot数量。
```python
from solana.rpc.api import Client

client = Client("http://localhost:8899")
performance = client.get_recent_performance_samples(10)
print(performance)
# GetRecentPerformanceSamplesResp([RpcPerfSample(RpcPerfSample { slot: 49326, num_transactions: 70, num_non_vote_transactions: Some(0), num_slots: 70, sample_period_secs: 60 }), ……])
print([slot.slot for slot in performance.value])
# [49326, 49256, 49197, 49141, 49084, 49032, 48990, 48939, 48888, 48834]
```


### solana.rpc.api.Client.get_block_height
该方法返回当前区块链的高度。可选参数："finalized", "confirmed" or "processed".默认参数为 `finalized`。
三者的区别在于finalized是最终确认的区块高度，confirmed是已经确认的区块高度，processed是已经处理的区块高度。
最终确认的区块会比刚处理好的区块高度要低一些。
```python
from solana.rpc.api import Client

client = Client("http://localhost:8899")
block_height = client.get_block_height()
print(block_height)
# GetBlockHeightResp(49619)
print(block_height.value)
# 49619
```

### solana.rpc.api.Client.get_blocks
获取两个区块之间的区块列表。
```python
from solana.rpc.api import Client

client = Client("http://localhost:8899")
blocks = client.get_blocks(49970,49980)
print(blocks)
# GetBlocksResp([49970, 49971, 49972, 49973, 49974, 49975])


```

### solana.rpc.api.Client.get_epoch_info
获取当前epoch的信息。
```python
from solana.rpc.api import Client

client = Client("http://localhost:8899")
epoch_info = client.get_epoch_info()
print(epoch_info)
# GetEpochInfoResp(EpochInfo(EpochInfo { 
#       epoch: 0, slot_index: 50757, 
#       slots_in_epoch: 432000, absolute_slot: 50757, 
#       block_height: 50754, transaction_count: Some(51456) 
#   })
# )
```


### solana.rpc.api.Client.get_epoch_schedule
获取当前epoch的计划。返回的结果包括每个epoch的slot数量，即每个epoch(纪元)包含43200个slot(间隔)
```python
from solana.rpc.api import Client
from solders.pubkey import Pubkey

client = Client("http://localhost:8899")
demo_pubkey = Pubkey.from_string("EBziZDuZwJNSMx57fZFqgzXVLssWZSLMQzweVkGzRdVv")
epoch_schedule = client.get_epoch_schedule()
print(epoch_schedule)
# GetEpochScheduleResp(EpochSchedule(EpochSchedule { 
#       slots_per_epoch: 432000, leader_schedule_slot_offset: 432000, 
#       warmup: false, first_normal_epoch: 0, first_normal_slot: 0 
#   })
# )
```

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

### solana.rpc.api.Client.get_identity
获取当前节点的公钥信息，与上面的get_genesis_hash方法类似，也可以在运行本地节点的终端界面上看到。
```python
from solana.rpc.api import Client

client = Client("http://localhost:8899")
identity = client.get_identity()
print(identity)
# GetIdentityResp(RpcIdentity(RpcIdentity { identity: "CnMdLhM1hH6nT8ekAQsLgZ9vigphriWiLbyHTkXnMc8B" }))
print(identity.value.identity)
# CnMdLhM1hH6nT8ekAQsLgZ9vigphriWiLbyHTkXnMc8B
```

### solana.rpc.api.Client.get_minimum_balance_for_rent_exemption
获取免除账户租金所需的最低余额。
```python
from solana.rpc.api import Client

client = Client("http://localhost:8899")
rent_exemption = client.get_minimum_balance_for_rent_exemption(50)
print(rent_exemption.value)  # 1238880 lamport
print(rent_exemption.value/10**9)  # 0.00123888 sol
```

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

### solana.rpc.api.Client.get_latest_blockhash
获取最新的区块哈希值。
```python
from solana.rpc.api import Client

client = Client("http://localhost:8899")
latest_blockhash = client.get_latest_blockhash()
print(latest_blockhash.value.blockhash)  # 55wn8fYeUVjshxubJJrvBsx9a2nzdiWzKoXotUB1zRoj
```

### solana.rpc.api.Client.get_slot_leader
获取当前槽位的领导者的公钥，即打包交易的节点。该节点进行打包交易，其他节点进行验证。
```python
from solana.rpc.api import Client

client = Client("http://localhost:8899")
slot_leader = client.get_slot_leader()
print(slot_leader)  # GetSlotLeaderResp(Pubkey(CnMdLhM1hH6nT8ekAQsLgZ9vigphriWiLbyHTkXnMc8B))
```


### solana.rpc.api.Client.get_stake_activation
获取质押账户的激活信息。现成的已激活的质押账户可以从节点目录中获取，文件为/path/to/your_validator_node/stake-account-keypair.json，
此文件为质押账户的密钥对，可以通过 Keypair.from_bytes().pubkey() 获取质押账户的公钥。会在keypair章节中详细介绍。

当账户处于未激活状态时，提示信息为 Invalid param: not a stake account 。

当账户处于激活状态时，state 字段为 Active，active 字段为激活的 lamport 数量，inactive 字段为未激活的 lamport 数量。
```python
from solana.rpc.api import Client
from solders.pubkey import Pubkey

client = Client("http://localhost:8899")
demo_pubkey = Pubkey.from_string("8qfgye21nZVt1DSNxxXYx8jGPX8mdz5DjPmPnzGXgjBt")
stake_activation = client.get_stake_activation(demo_pubkey)
print(stake_activation)
# InvalidParamsMessage { message: "Invalid param: not a stake account" }
# GetStakeActivationResp(RpcStakeActivation(RpcStakeActivation { state: Active, active: 999999997717120, inactive: 0 }))
```

### solana.rpc.api.Client.get_vote_accounts
前面有说过，solana 的一组助记词对应多个账户，如上面的质押账户，程序账户和普通账户，以及当前的投票账户。
```python
from solana.rpc.api import Client

client = Client("http://localhost:8899")
vote_accounts = client.get_vote_accounts()
print(vote_accounts.value.current[0].vote_pubkey)
# B2EoDTFWwSvZnkX5F8dPRKtUkZseu3hGgApe7PgNsdEQ
```

