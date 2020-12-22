import time

global list_of_popularity
global list_of_filesID
list_of_popularity = []
list_of_filesID = []
list_of_size = []

verbose = False  # Set it to True to print which files are in the cache.
verbose_time = False


def cache_decision_sample(my_cache, file, file_size):
    if file not in my_cache.stored_files:
        # If the cache capacity is full,
        # remove the last accessed files from the cache until there is enough space for the new file.
        if my_cache.cache_size + file_size < my_cache.cache_capacity:
            my_cache.store_in_cache(file)
        else:
            while my_cache.cache_size + file_size > my_cache.cache_capacity:
                my_cache.remove_from_cache(min(my_cache.timestamp, key=my_cache.timestamp.get))
            my_cache.store_in_cache(file)


# You will fill inside this function for part 1. You can only use the information given in the arguments.
def cache_decision_part1(my_cache, file, file_popularity, file_size):
    global list_of_popularity

    if file not in my_cache.stored_files:
        # If the cache capacity is full,
        # remove the least popular from the cache until there is enough space for the new file.
        if my_cache.cache_size + file_size < my_cache.cache_capacity:
            my_cache.store_in_cache(file)
            list_of_popularity.append(file_popularity)
            list_of_filesID.append(file)
            list_of_size.append(file_size)
        else:
            while my_cache.cache_size + file_size > my_cache.cache_capacity:
                index_min = min(range(len(list_of_popularity)), key=list_of_popularity.__getitem__)
                delete_item = list_of_filesID[index_min]
                if (file_size > list_of_size[0]):
                    if (file_popularity > list_of_popularity[0]):
                        index_min = 0
                        delete_item = list_of_filesID[0]

                if (verbose):
                    print("Custom_Index:", index_min)
                    print("Delete item:", delete_item)
                my_cache.remove_from_cache(delete_item)
                list_of_popularity.pop(index_min)
                list_of_filesID.pop(index_min)
                list_of_size.pop(index_min)
                if (verbose):
                    print("Custom List:", list_of_filesID)
                if (verbose_time):
                    time.sleep(1)
            my_cache.store_in_cache(file)
            list_of_popularity.append(file_popularity)
            list_of_filesID.append(file)
            list_of_size.append(file_size)


# You will fill inside this function for part 2. You can only use the information given in the arguments.
def cache_decision_part2(my_cache, file, file_size):
    pass
