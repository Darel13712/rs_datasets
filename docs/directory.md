# Managing dataset directory

Each dataset creates its folder inside dataset directory. 

Dataset directory is determined by following priorities:

1. `path` parameter from initialization
2. Environment variable `RS_DATASETS`
3. Default folder, which is in your home directory: `~/.rs_datasets/`

So in general case you don't have to do anything 
and files corresponding to `dataset` will be stored in `~/.rs_datasets/dataset/`.
