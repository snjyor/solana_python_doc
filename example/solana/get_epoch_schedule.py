
### solana.rpc.api.Client.get_epoch_schedule
# 获取当前epoch的计划。返回的结果包括每个epoch的slot数量，即每个epoch(纪元)包含43200个slot(间隔)


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

