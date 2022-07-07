__winc_id__ = "ae539110d03e49ea8738fd413ac44ba8"
__human_name__ = "files"

import os
import shutil
import zipfile

path = os.path.abspath(os.path.join(os.getcwd(), 'files\\cache'))

# Part 1

def clean_cache():
    directory = "cache"
    if path:
        shutil.rmtree(path)
    os.makedirs(path)
    return print(f"Directory {'%s'} cleaned" % directory)

clean_cache()

# Part 2

def cache_zip(zip_path, cache_path):
    path = cache_path
    if zipfile.is_zipfile(zip_path):
        zipfile.ZipFile(zip_path).extractall(path)#=cache_path)
    else:
        return "No zip-file"

cache_zip("C:/Users/Jacques/Desktop/Winc/files/data.zip", "C:/Users/Jacques/Desktop/Winc/files/cache")


# Part 3

def cached_files():
    filelist = []
    for file in os.listdir(path):
        if file not in filelist:
            filelist.append(os.path.join(path, file))
        else:
            break
    return filelist

print(cached_files())


# Part 4

def find_password(filelist):
    for file in filelist:
        with open(file, mode="r", encoding="utf-8") as f:
            lines = f.readlines()
            for words in lines:
                if "password" in words:
                    return words.split()[1]

print(find_password(cached_files()))
