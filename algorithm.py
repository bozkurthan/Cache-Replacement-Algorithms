global list_of_popularity
global list_of_filesID
list_of_popularity = [0] * 100
list_of_cost = [0] * 100
list_of_filesID = []
list_of_size = []
list_of_k_value = []
k_parameter = 0.002
total_hit_cost = [0] * 100
counter = 0
number_of_miss_better_files = 0
population_bad_check=0

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
def cache_decision_part1(my_cache, file, file_popularities, file_sizes):
    global counter

    if (counter == 0):
        initCache(my_cache, file_popularities, file_sizes)
    if (counter == 100000):
        counter = 0
    counter = counter + 1


# You will fill inside this function for part 2. You can only use the information given in the arguments.
def cache_decision_part2(my_cache, file, file_sizes):
    global list_of_popularity
    global list_of_cost
    global population_bad_check
    list_current_files_popularity = []
    list_current_files_cost = []
    list_of_popularity[file] = list_of_popularity[file] + 1
    file_size = file_sizes[file]
    if (len(my_cache.stored_files) == 0):
        for i in range(100):
            list_of_popularity[i] = 0
            list_of_cost[i] = 0

    total_hit = 0
    for i in range(100):
        total_hit = list_of_popularity[i] + total_hit

    list_current_files = my_cache.stored_files
    if (len(list_current_files) != 0):
        for i in range(len(list_current_files)):
            list_current_files_popularity.append(list_of_popularity[list_current_files[i]])
    if (len(list_current_files) != 0):
        for i in range(len(list_current_files)):
            list_current_files_cost.append(list_of_cost[list_current_files[i]])
    total_hit = total_hit / 100

    if file not in my_cache.stored_files:
            if(max(list_of_popularity)>100):
                #clear cache if pop <100
                if(min(list_current_files_popularity)<100):
                    index_min = min(range(len(list_current_files_popularity)),
                                    key=list_current_files_popularity.__getitem__)
                    my_cache.remove_from_cache(my_cache.stored_files[index_min])
                    list_current_files_popularity.pop(index_min)
                if(list_of_popularity[file]<100):
                    pass
                else:
                    if my_cache.cache_size + file_size < my_cache.cache_capacity:
                        my_cache.store_in_cache(file)
                    else:
                        if (list_of_cost[file] > max(list_current_files_cost)):
                            while my_cache.cache_size + file_size > my_cache.cache_capacity:
                                index_min = min(range(len(list_current_files_cost)),
                                                key=list_current_files_cost.__getitem__)
                                my_cache.remove_from_cache(my_cache.stored_files[index_min])
                                list_current_files_popularity.pop(index_min)
                                list_current_files_cost.pop(index_min)
                            my_cache.store_in_cache(file)
                    # restore cache
                    if (my_cache.cache_size < 0.05):
                        print("uyari")
                    if (len(list_current_files_popularity) != 0):
                        if (min(list_current_files_popularity) < 100):
                            population_bad_check = population_bad_check + 1
                            print(population_bad_check + 1)
            else:
                if my_cache.cache_size + file_size < my_cache.cache_capacity:
                        my_cache.store_in_cache(file)
                else:
                        if (list_of_cost[file] > max(list_current_files_cost)):
                            while my_cache.cache_size + file_size > my_cache.cache_capacity:
                                index_min = min(range(len(list_current_files_cost)),
                                                key=list_current_files_cost.__getitem__)
                                my_cache.remove_from_cache(my_cache.stored_files[index_min])
                                list_current_files_popularity.pop(index_min)
                                list_current_files_cost.pop(index_min)
                            my_cache.store_in_cache(file)
                #restore cache
                if(my_cache.cache_size<0.05):
                    print("uyari")
                if(len(list_current_files_popularity)!=0):
                    if(min(list_current_files_popularity)<100):
                        population_bad_check=population_bad_check+1
                        print(population_bad_check+1)

                        # list_of_cost[file] = file_sizes[file] + list_of_cost[file]
                        # index_max = max(range(len(list_of_cost)), key=list_of_cost.__getitem__)
                        # while my_cache.cache_size + file_sizes[index_max] > my_cache.cache_capacity:
                        #     index_min = min(range(len(list_current_files_popularity)),
                        #                     key=list_current_files_popularity.__getitem__)
                        #     my_cache.remove_from_cache(my_cache.stored_files[index_min])
                        #     list_current_files_popularity.pop(index_min)
                        # my_cache.store_in_cache(index_max)
                    # if (list_of_popularity[file] > max(list_current_files_popularity)):
                    #     while my_cache.cache_size + file_size > my_cache.cache_capacity:
                    #         index_min = min(range(len(list_current_files_popularity)),
                    #                         key=list_current_files_popularity.__getitem__)
                    #         my_cache.remove_from_cache(my_cache.stored_files[index_min])
                    #         list_current_files_popularity.pop(index_min)
                    #     my_cache.store_in_cache(file)
                    #
                    # else:
                    #
                    #     list_of_cost[file] = file_sizes[file] + list_of_cost[file]
                    #     index_max = max(range(len(list_of_cost)), key=list_of_cost.__getitem__)
                    #     while my_cache.cache_size + file_sizes[index_max] > my_cache.cache_capacity:
                    #         index_min = min(range(len(list_current_files_popularity)),
                    #                         key=list_current_files_popularity.__getitem__)
                    #         my_cache.remove_from_cache(my_cache.stored_files[index_min])
                    #         list_current_files_popularity.pop(index_min)
                    #     my_cache.store_in_cache(index_max)

def initCache(my_cache, val, wt):
    new_val = []
    new_wt = []
    for i in range(len(val)):
        new_val.append(int(val[i] / min(val)))
    W = int(0.1 / min(wt))
    for i in range(len(wt)):
        new_wt.append(int(wt[i] / min(wt)))

    n = len(new_val)
    list_of_store = printknapSack(W, new_wt, new_val, n)
    print(list_of_store)
    n = len(list_of_store)
    for i in range(n - 1, 0, -1):
        my_cache.store_in_cache(list_of_store[i])


def printknapSack(W, wt, val, n):
    list_of_item = []
    K = [[0 for w in range(W + 1)]
         for i in range(n + 1)]

    # Build table K[][] in bottom
    # up manner
    for i in range(n + 1):
        for w in range(W + 1):
            if i == 0 or w == 0:
                K[i][w] = 0
            elif wt[i - 1] <= w:
                K[i][w] = max(val[i - 1]
                              + K[i - 1][w - wt[i - 1]],
                              K[i - 1][w])
            else:
                K[i][w] = K[i - 1][w]

                # stores the result of Knapsack
    res = K[n][W]
    # print(res)

    w = W
    for i in range(n, 0, -1):
        if res <= 0:
            break
        # either the result comes from the
        # top (K[i-1][w]) or from (val[i-1]
        # + K[i-1] [w-wt[i-1]]) as in Knapsack
        # table. If it comes from the latter
        # one/ it means the item is included.
        if res == K[i - 1][w]:
            continue
        else:

            # This item is included.
            list_of_item.append(i - 1)

            # Since this weight is included
            # its value is deducted
            res = res - val[i - 1]
            w = w - wt[i - 1]
    return (list_of_item)
