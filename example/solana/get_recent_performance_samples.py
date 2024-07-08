### solana.rpc.api.Client.get_recent_performance_samples
# 该方法返回最近性能样本的列表，性能样本每 60 秒采集一次，包括在这60秒的时间窗口中发生的交易和slot数量。


from solana.rpc.api import Client

client = Client("http://localhost:8899")
performance = client.get_recent_performance_samples(10)
print(performance)
# GetRecentPerformanceSamplesResp([RpcPerfSample(RpcPerfSample { slot: 49326, num_transactions: 70, num_non_vote_transactions: Some(0), num_slots: 70, sample_period_secs: 60 }), ……])
print([slot.slot for slot in performance.value])
# [49326, 49256, 49197, 49141, 49084, 49032, 48990, 48939, 48888, 48834]

