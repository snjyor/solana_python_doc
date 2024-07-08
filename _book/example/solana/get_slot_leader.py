### solana.rpc.api.Client.get_slot_leader
# 获取当前槽位的领导者的公钥，即打包交易的节点。该节点进行打包交易，其他节点进行验证。


from solana.rpc.api import Client

client = Client("http://localhost:8899")
slot_leader = client.get_slot_leader()
print(slot_leader)  # GetSlotLeaderResp(Pubkey(CnMdLhM1hH6nT8ekAQsLgZ9vigphriWiLbyHTkXnMc8B))

