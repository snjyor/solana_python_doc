### solana.rpc.api.Client.get_block_height
# 该方法返回当前区块链的高度。可选参数："finalized", "confirmed" or "processed".默认参数为 `finalized`。
# 三者的区别在于finalized是最终确认的区块高度，confirmed是已经确认的区块高度，processed是已经处理的区块高度。
# 最终确认的区块会比刚处理好的区块高度要低一些。


from solana.rpc.api import Client

client = Client("http://localhost:8899")
block_height = client.get_block_height()
print(block_height)
# GetBlockHeightResp(49619)
print(block_height.value)
# 49619

