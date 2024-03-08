import subprocess

def get_commit_details(commit_hash):
    """Get commit details using git show."""
    command = ['git', 'show', commit_hash]
    result = subprocess.run(command, capture_output=True, text=True)
    return result.stdout

def main():
    """Main function to iterate over commit history and display details."""
    commit_hashes = subprocess.run(['git', 'log', '--format=format:%H'], capture_output=True, text=True).stdout.splitlines()
    
    for commit_hash in commit_hashes:
        print(f'Commit: {commit_hash}')
        commit_details = get_commit_details(commit_hash)
        print(commit_details)
        print()

if __name__ == "__main__":
    main()
