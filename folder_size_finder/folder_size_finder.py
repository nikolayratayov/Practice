import os


def get_immediate_subdirectories(a_dir):
    return [name for name in os.listdir(a_dir)
            if os.path.isdir(os.path.join(a_dir, name))]


def folderpath(folder):
    global dict_sizes
    size = 0
    for path, dirs, files in os.walk(folder):
        for f in files:
            fp = os.path.join(path, f)
            try:
                size += os.path.getsize(fp)
            except:
                continue
    dict_sizes[os.path.basename(folder)] = size / 1024 / 1024


kade = input('Enter directory (for example \'C:\Program Files\\\'): ')
print('It may take a little time...')

dict_sizes = {}

poddir = get_immediate_subdirectories(kade)

for i in poddir:
    size_of_poddir = f'{kade}/{i}'
    folderpath(size_of_poddir)

dict_sizes = sorted(dict_sizes.items(), key=lambda x: x[1], reverse=True)

print()
print()

for i in dict_sizes:
    print(i[0], i[1])

