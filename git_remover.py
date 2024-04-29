
import os
import shutil
def remover(path):
    for root, subFolder, files in os.walk(path):
        for folder in subFolder:
            if folder == '.git':
                subfolder_path = os.path.join(root)
                git_folder_path = os.path.join(root,folder)

                print(git_folder_path)
                shutil.rmtree(subfolder_path, ignore_errors=True)
                print(f'Removed {subfolder_path}')


remover('C:/Users/Administrator/Desktop/test')
