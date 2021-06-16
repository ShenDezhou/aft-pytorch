import torch
from aft_pt import AFTFull, AFTSimple, AFTLocal

layer = AFTSimple(
    max_seqlen=20,
    dim=512,
    hidden_dim=200
)

# a batch of 64 sequences with 15 timesteps with embed size 512
x = torch.rand(64, 15, 512)
y = layer(x)

print(y.shape) # [64, 15, 512]