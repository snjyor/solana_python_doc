## solana.rpc.api.Client
# 实例化 solana.rpc.api.Client 类，用于连接到 Solana RPC 节点。

# |网络|URL|
# |---|---|
# |主网|https://api.mainnet-beta.solana.com|
# |开发网|https://api.devnet.solana.com|
# |测试网|https://api.testnet.solana.com|
# |本地|http://localhost:8899|


from solana.rpc.api import Client

client = Client("http://localhost:8899")

