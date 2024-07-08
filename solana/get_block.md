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
