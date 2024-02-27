import os

from file_processing import extract_id


def create_dataset_from_directory(root_path):
    audios_path, labels = [], []

    for id_dir in os.listdir(root_path):
        for _, dirs, __ in os.walk(os.path.join(root_path, id_dir)):
            for dir in dirs:
                for file in os.listdir(os.path.join(root_path, id_dir, dir)):
                    audios_path.append(os.path.join(
                        root_path, id_dir, dir, file
                    ))
                    labels.append(extract_id(id_dir))

    return audios_path, labels


def create_dataset_from_deeplake(root_path):
    return None
