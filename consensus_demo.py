import random

miner = {"id": "miner1", "power": random.randint(1, 100)}
print("Proof-of-Work:\n", f"Selected miner: {miner['id']} with power: {miner['power']}")
print("Highest power gets selected\n")

stakers = [{"id": f"staker{i+1}", "stake": random.randint(10, 100)} for i in range(3)]
selected_staker = max(stakers, key=lambda x: x['stake'])
print("Proof-of-Stake:\n", f"Selected staker: {selected_staker['id']} with stake: {selected_staker['stake']}")
print("Highest stake gets selected\n")

voters = ["A", "B", "C"]
votes = {"A": 2, "B": 3, "C": 1}
selected_delegate = max(votes, key=votes.get)
print("Delegated Proof-of-Stake:\n", f"Selected delegate: {selected_delegate} with votes: {votes[selected_delegate]}")
print("Most voted delegate gets selected\n")
