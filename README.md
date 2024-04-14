## Objaverse Downloader

Reduce the hassle of downloading the 8.9 TB dataset by fetching only the necessary files!

This script only downloads the mesh models selectively based on desired file size criteria.

## Features

- Download meshes based on minimum and maximum file size requirements.
- Filter metadata files and export them into a JSON file containing only relevant metadata for downloaded files.

## Usage

1. Set your desired file size criteria in the provided notebook.
2. Execute the notebook to download meshes and filter metadata accordingly.

## Usecase

While training [MeshGPT](https://github.com/lucidrains/meshgpt-pytorch) I needed to find more mesh models and was interested in using [Objaverse](https://huggingface.co/datasets/allenai/objaverse) which contains 800k+ models.

However, I could not clone the entire repo since the dataset is about 8.9 TB, which I don't have disk or time to download.
I only wanted to download the small mesh models to train the MeshGPT model, e.g., max 80 KB.
Git doesn't offer much support for downloading by filtering the file sizes, so I created this script to download only the mesh files within a file size range.

For getting file sizes, I dumped the entire commit history for Objaverse repo and then parsed the output to get the file sizes for each model. I've left the code and instructions on how to do this in the notebook.

## Moving Large Folders Using Rsync

When dealing with large folders, it's essential to have strategies to move them efficiently. One such strategy is using the `rsync` command in Unix-based systems like Linux and MacOS.

Consider the following example where we want to move files from a local directory to a Google Drive folder:

```bash
find gltf_xmp_json_ld/ -type f -print0 | xargs -0 -I {} rsync -avh --remove-source-files {} /Users/aria/Library/CloudStorage/GoogleDrive-aria@chibifire.com/Shared\ drives/25\ -\ \[External\]\ gltf_xmp_json_ld/
```

In this command:

- `find gltf_xmp_json_ld/ -type f -print0` finds all files in the `gltf_xmp_json_ld/` directory.
- `xargs -0 -I {}` takes the output from the find command and passes it as an argument to the following command.
- `rsync -avh --remove-source-files {} /Users/aria/Library/CloudStorage/GoogleDrive-aria@chibifire.com/Shared\ drives/25\ -\ \[External\]\ gltf_xmp_json_ld/` copies each file to the specified Google Drive folder.

The `-avh` option tells rsync to archive (keeping permissions and other file properties), use a verbose mode (providing detailed information about what the command is doing), and display the progress in a human-readable format.

The `--remove-source-files` option tells rsync to remove the source files after they've been copied. This is useful when you're trying to move (not just copy) files from one location to another.

This approach can save you a lot of time and disk space when dealing with large datasets.
