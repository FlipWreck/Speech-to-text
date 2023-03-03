import csv, os, shutil

folder_to_new = {
    '19':'1',
    '20':'2',
    '21':'3'}

for i in folder_to_new.keys():
    # Global vars
    old_folder,new_folder = i,folder_to_new[i]
    path = 'C:/Users/donat/OneDrive/Desktop/listener/vhf-archive-export-2022-09-21-134051.708850 (1)/2022/09/' ###folder where we store .wav files
    folder = f'{path}/{new_folder}'

    # Create new folder for organized files
    if not os.path.exists(folder):
        os.makedirs(folder)

    # Read index.csv files
    lines = []
    with open(f'{path}/{old_folder}/index.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            lines.append(row)

    # Copy wav files to another folder + rename them
    operator_index,begin_index,end_index,wav_index = 6,8,9,11
    for x,line in enumerate(lines):
        if not 'operator' in line[operator_index]:
            name = f"{line[begin_index].split(' ')[1]} - {line[end_index].split(' ')[1]}" ##here we will display our .wav file and rename it to beggining time and ending time
            name = name.replace(':','-') 
            shutil.copy(f'{path}/{old_folder}/{line[wav_index]}', f'{folder}/{name}.wav')