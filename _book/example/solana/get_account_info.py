### solana.rpc.api.Client.get_account_info
# 账户信息内容与余额信息类似，但是返回的是 GetAccountInfoResp 对象，其中value的值为 Account 对象，包含了账户的详细信息。其中：
# - lamports为账户余额，其值是账户显示余额乘1,000,000,000
# - data为账户数据
# - owner为账户所有者
# - executable为是否可执行，此账户为数据账户，只存储数据状态，不可执行
# - rent_epoch为租金周期

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
