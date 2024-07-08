
### solana.rpc.api.Client.get_stake_activation
# 获取质押账户的激活信息。现成的已激活的质押账户可以从节点目录中获取，文件为/path/to/your_validator_node/stake-account-keypair.json，
# 此文件为质押账户的密钥对，可以通过 Keypair.from_bytes().pubkey() 获取质押账户的公钥。会在keypair章节中详细介绍。

# 当账户处于未激活状态时，提示信息为 Invalid param: not a stake account 。

# 当账户处于激活状态时，state 字段为 Active，active 字段为激活的 lamport 数量，inactive 字段为未激活的 lamport 数量。


from solana.rpc.api import Client
from solders.pubkey import Pubkey

client = Client("http://localhost:8899")
demo_pubkey = Pubkey.from_string("8qfgye21nZVt1DSNxxXYx8jGPX8mdz5DjPmPnzGXgjBt")
stake_activation = client.get_stake_activation(demo_pubkey)
print(stake_activation)
# InvalidParamsMessage { message: "Invalid param: not a stake account" }
# GetStakeActivationResp(RpcStakeActivation(RpcStakeActivation { state: Active, active: 999999997717120, inactive: 0 }))

