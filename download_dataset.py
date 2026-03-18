from huggingface_hub import snapshot_download, login


login(token="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")

#snapshot_download(repo_id="ministere-culture/comparia-conversations", repo_type="dataset", local_dir="./data/comparia-conversations")

#snapshot_download(repo_id="ministere-culture/comparia-votes", repo_type="dataset", local_dir="./data/comparia-votes")

#snapshot_download(repo_id="ministere-culture/comparia-reactions", repo_type="dataset", local_dir="./data/comparia-reactions")

snapshot_download(
    repo_id="ministere-culture/comparia-reactions",
    repo_type="dataset",
    local_dir="./data/comparia-reactions"
)

print("Fini")