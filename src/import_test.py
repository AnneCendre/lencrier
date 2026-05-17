import torch
print(torch.cuda.is_available())
print(torch.version.cuda)
print(torch.cuda.get_device_capability(0))  # Doit afficher (6, 1) pour GT 1030   


