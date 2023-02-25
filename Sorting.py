def selection_sort(lst):
    #This function takes a list as an argument and sorts it in ascending order using the selection sort algorithm
    """_summary_
     The basic idea behind selection sort is to find the smallest element in the unsorted portion of the list and swap it with the first element in the unsorted portion.
     This process is repeated until the entire list is sorted.
    """
    n=len(lst)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if lst[j]<lst[min_idx]:
                min_idx = j
        lst[i], lst[min_idx] = lst[min_idx],lst[i]
    return lst

li_st = [20, 40, 100, 10, 40, 30, 200, 10, 4]
print(selection_sort(li_st))