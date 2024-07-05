import shutil
import os

def copy(static_folder='static', dist_folder='dist/static'):
    if not os.path.exists(static_folder):
        print(f"The specified static folder '{static_folder}' does not exist.")
        return

    if not os.path.exists(dist_folder):
        os.makedirs(dist_folder)

    for item in os.listdir(static_folder):
        s = os.path.join(static_folder, item)
        d = os.path.join(dist_folder, item)
        if os.path.isdir(s):
            shutil.copytree(s, d, dirs_exist_ok=True)
        else:
            shutil.copy2(s, d)
    print(f"Copied contents of '{static_folder}' to '{dist_folder}'.")