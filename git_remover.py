
import os
import shutil
import time

from rich import print
import subprocess
def remove_git(file):
    with open(file, 'r') as f:
        lines = f.readlines()
        for i,line in enumerate(lines):
            git_path = line.strip()
            if '\\.git' in git_path :
                parent_path = git_path.replace('\\.git', '')
            else:
                parent_path = git_path
            if os.path.exists(git_path):
                print(git_path)
                # print(parent_path, 'p')
                try:
                    execute = subprocess.call(
                    [f'cmd','/c',"rmdir","/S","/Q",parent_path])
                except Exception as e:
                    print(e)
                    time.sleep(15)
                if not os.path.exists(git_path):
                    print(f"[red]{git_path} removed")
                # return f"{git_path} removed"

            else:
                print(f"{git_path} folder not found")

    input('Press double enter')
    input('Press Enter to close window!!!')
    return f"Scanning ended successfully!!"

    #
    # for root, subFolder, files in os.walk(path):
    #     for folder in subFolder:
    #         if folder == '.git':
    #             subfolder_path = os.path.join(root)
    #             git_folder_path = os.path.join(root,folder)
    #             print(f'[cyan]folder found: {git_folder_path}')
    #             shutil.rmtree(subfolder_path, ignore_errors=True)
    #             print(f'[red]Removed {subfolder_path}')



# remove_git('d:/text.txt')

# rmdir "c:\Users\Administrator\Desktop\test\supabase_examples - Copy" /s /q