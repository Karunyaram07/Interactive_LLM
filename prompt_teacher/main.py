from huggingface_hub import HfApi

api = HfApi()
info = api.repo_info("meta-llama/Llama-3.1-8B")
print(info)
