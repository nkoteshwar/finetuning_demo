import os
print(os.path.join(os.getenv("HF_HOME", os.path.expanduser("~/.cache/huggingface")), "token"))