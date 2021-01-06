import heapq

global list_of_popularity
global list_of_filesID
list_of_popularity = [0] * 100
list_of_cost = [0] * 100
list_of_filesID = []
list_of_size = []
list_of_k_value = []
k_parameter = 0.002
counter = 0
total_cost=0
demand_counter=0
k_value=7
previous_total_cost = 1
positive_negative = True
cache_not_used_enough = 0
g_k_value =7
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
    pass

def guess_k_value():
    global previous_total_cost
    global g_k_value
    previous_total_cost=previous_total_cost
    cost_calc=(total_cost/demand_counter)/previous_total_cost

    if(cost_calc>1):
        g_k_value = k_value + 5
        if(g_k_value>100):
            g_k_value=100
    else:
            g_k_value=k_value
    previous_total_cost=total_cost/demand_counter
    return g_k_value

# You will fill inside this function for part 2. You can only use the information given in the arguments.
def cache_decision_part2(my_cache, file, file_size):
    global list_of_popularity
    global total_cost
    global demand_counter
    global k_value
    global cache_not_used_enough
    demand_counter=demand_counter+1
    list_current_files_popularity = []
    list_of_popularity[file] = list_of_popularity[file] + 1

    if (len(my_cache.stored_files) == 0):
        for i in range(100):
            list_of_popularity[i] = 0
    #try to guess k_value
    if(demand_counter%200==0 and demand_counter!=0):
        k_value=guess_k_value()
    if file not in my_cache.stored_files:
        total_cost = total_cost + file_size

        list_current_files = my_cache.stored_files
        if (len(list_current_files) != 0):
            for i in range(len(list_current_files)):
                list_current_files_popularity.append(list_of_popularity[list_current_files[i]])
        if(max(list_of_popularity)>k_value):
            #clear cache if pop < k_value
            if(min(list_current_files_popularity)<k_value):
                index_min = min(range(len(list_current_files_popularity)),
                                key=list_current_files_popularity.__getitem__)
                my_cache.remove_from_cache(my_cache.stored_files[index_min])
                list_current_files_popularity.pop(index_min)
                if(my_cache.cache_size + file_size < my_cache.cache_capacity):
                    my_cache.store_in_cache(file)
                idx=heapq.nlargest(20, list_of_popularity)
                res = sorted(range(len(list_of_popularity)), key=lambda sub: list_of_popularity[sub])[-20:]
                for i in range(len(list_current_files),0):
                    if(idx[i] not in list_current_files_popularity):
                        if(my_cache.cache_size+ file_size < my_cache.cache_capacity):
                            my_cache.store_in_cache(res[i])


            else:
                if my_cache.cache_size + file_size < my_cache.cache_capacity:
                    my_cache.store_in_cache(file)
        else:
            if my_cache.cache_size + file_size < my_cache.cache_capacity:
                my_cache.store_in_cache(file)