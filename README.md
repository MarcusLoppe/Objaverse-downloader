## Objaverse-downloader
Instead of downloading the entire 8.9 TB dataset, download only files you need!

This is a script to only download the mesh models you need by filtering the file size!

The notebook contains instructions and code for:

1. Download meshes as per min and max kb file size. 
3. Download the metadata files, then filter and export it into a json file with only the relevant metadata to the files you have downloaded.

## Usecase

While training [MeshGPT](https://github.com/lucidrains/meshgpt-pytorch) I needed to find more mesh models and was intreseted in using [objaverse](https://huggingface.co/datasets/allenai/objaverse) which contains 800k+ models.

The issue was that the entire dataset is about 8.9 TB, and I only wanted the mesh models which had less then 400 triangles e.g max 80 KB.
There are some support for filtering while cloning but I had no luck, so I created this script to download only the mesh files that are within a file size range.


For getting file sizes; I dumped the entire commit history for Objaverse repo and then parsed the output to get the file sizes for each model, I've left the code and instructions on how to do this in the notebook.
