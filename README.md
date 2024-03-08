## Objaverse Downloader
Reduce the hassle of downloading the entire 8.9 TB dataset by fetching only the necessary files!

This is a script to only download the  mesh models selectively based on desired file size criteria.

## Features

- Download meshes based on minimum and maximum file size requirements.
- Filter metadata files and export them into a JSON file containing only relevant metadata for downloaded files.

## Usage

1. Set your desired file size criteria in the provided notebook.
2. Execute the notebook to download meshes and filter metadata accordingly.

## Usecase

While training [MeshGPT](https://github.com/lucidrains/meshgpt-pytorch) I needed to find more mesh models and was intreseted in using [objaverse](https://huggingface.co/datasets/allenai/objaverse) which contains 800k+ models.

However I could not clone the entire repo since the entire dataset is about 8.9 TB which I don't have disk or time to download.
I also only wanted to download the small mesh models to train the MeshGPT model on e.g. max 80 KB.
Git doesn't offer much support on downloading by filtering the file sizes so I created this script to download only the mesh files that are within a file size range.


For getting file sizes; I dumped the entire commit history for Objaverse repo and then parsed the output to get the file sizes for each model. I've left the code and instructions on how to do this in the notebook.
