import os
import multiprocessing as mp
import shutil
import random
import time


def make_data_directories(dir_name, labels):
    # dir_name - Top level directory name
    # labels - labels names. (e.g. cats, dogs, horses)
    try:
        os.mkdir(dir_name)  # making top level directory
    except OSError as e:
        print(e.filename, 'exists already')
        pass

    train_path = os.path.join(dir_name, 'training')
    testing_path = os.path.join(dir_name, 'testing')

    try:
        os.mkdir(train_path)  # making training subdirectory
    except FileExistsError as e:
        print(e.filename, 'exists already')
        pass

    try:
        os.mkdir(testing_path)  # making testing subdirectory
    except FileExistsError as e:
        print(e.filename, 'exists already')
        pass

    for i in range(len(labels)):  # making training labels and testing labels subdirectory
        try:
            os.mkdir(os.path.join(train_path, str(labels[i])))
        except OSError as e:
            print(e.filename, 'exists already')
            pass

        try:
            os.mkdir(os.path.join(testing_path, str(labels[i])))
        except OSError as e:
            print(e.filename, 'exists already')
            pass


def split_data(SOURCE, TRAINING, TESTING, SPLIT_SIZE):
    # SOURCE - Path location where the images are located
    # TRAINING - Path location where the training data will be moved to
    # TESTING - Path location where the testing data will be moved to
    # SPLIT_SIZE = The amount of images going to the training dataset by %.
    # (e.g. SPLIT_SIZE = .9: total images = 100, 90 images goes to training directory, 10 images goes to test directory)

    testing_file_names = []
    file_names = os.listdir(SOURCE)  #
    t = round(len(file_names) * (1 - SPLIT_SIZE))
    random.shuffle(file_names)
    for i in range(int(t)):
        testing_file_names.append(file_names[i])  # adding the file names for the testing data set
        file_names.remove(file_names[i])  # removing the testing data file names

    for jpg in range(len(testing_file_names)):  # using the testing file names to move from source to testing directory
        shutil.copy2(os.path.join(SOURCE, testing_file_names[jpg]), TESTING)

    for jpg in range(len(file_names)):  # # using the file names to move from source to training directory
        shutil.copy2(os.path.join(SOURCE, file_names[jpg]), TRAINING)


def make_dataset(new_dir, labels, src_directories):
    make_data_directories(new_dir, labels)
    for i in range(len(labels)):
        split_data(SOURCE=src_directories[i],
                   TRAINING=os.path.join(new_dir, 'training', labels[i]),
                   TESTING=os.path.join(new_dir, 'testing', labels[i]),
                   SPLIT_SIZE=0.8)


def multi_process_dataset(new_dir, labels, src_directories):
    make_data_directories(new_dir, labels)
    processes = []
    for i in range(len(labels)):
        training_path = os.path.join(new_dir, 'training', labels[i])
        testing_path = os.path.join(new_dir, 'testing', labels[i])
        p = mp.Process(target=split_data, args=(src_directories[i], training_path, testing_path, 0.9))
        processes.append(p)
        p.start()

    for process in processes:
        process.join()
