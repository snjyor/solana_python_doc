### solana.rpc.api.Client.get_epoch_info
# 获取当前epoch的信息。


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

