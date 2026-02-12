#!python
import math

def merge(items1, items2):
    """Merge given lists of items, each assumed to already be in sorted order,
    and return a new list containing all items in sorted order.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    p1 = 0
    p2 = 0
    merged_list = []
    
    # TODO: Repeat until one list is empty
    # TODO: Find minimum item in both lists and append it to new list
    # TODO: Append remaining items in non-empty list to new list
    while p1 < len(items1) or p2 < len(items2):
        if not p1 >= len(items1) and (p2 >= len(items2) or items1[p1] < items2[p2]):
            merged_list.append(items1[p1])
            p1 += 1
        else:
            merged_list.append(items2[p2])
            p2 += 1

    return merged_list


def merge_sort(items):
    """Sort given items by splitting list into two approximately equal halves,
    sorting each recursively, and merging results into a list in sorted order.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # TODO: Check if list is so small it's already sorted (base case)
    if len(items) <= 1:
        return items
    
    # TODO: Split items list into approximately equal halves
    middle = math.floor(len(items) / 2)
    left = items[:middle]
    right = items[middle:]

    # TODO: Sort each half by recursively calling merge sort
    # TODO: Merge sorted halves into one list in sorted order
    merged_list = merge(merge_sort(left), merge_sort(right))
    
    for idx in range(len(merged_list)):
        items[idx] = merged_list[idx]
        
    return items


def partition(items, low, high):
    """Return index `p` after in-place partitioning given items in range
    `[low...high]` by choosing a middle pivot from
    that range, moving pivot into index `p`, items less than pivot into range
    `[low...p-1]`, and items greater than pivot into range `[p+1...high]`.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # TODO: Choose a pivot any way and document your method in docstring above
    pivot = math.floor((low + high) / 2)
    pivot_value = items[pivot]
    
    items[pivot] = items[high]
    items[high] = pivot_value
    
    # TODO: Loop through all items in range [low...high]
    # TODO: Move items less than pivot into front of range [low...p-1]
    # TODO: Move items greater than pivot into back of range [p+1...high]
    for idx in range(low, high):
        current_item = items[idx]
        
        if current_item < pivot_value:
            items[idx] = items[low]
            items[low] = current_item
            low += 1
    
    items[high] = items[low]
    items[low] = pivot_value
        
    # TODO: Move pivot item into final position [p] and return index p
    return low

def quick_sort(items, low=None, high=None):
    # print(items, low, high)
    """Sort given items in place by partitioning items in range `[low...high]`
    around a pivot item and recursively sorting each remaining sublist range.
    TODO: Best case running time: ??? Why and under what conditions?
    TODO: Worst case running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # TODO: Check if high and low range bounds have default values (not given)
    if low == None and high == None:
        low = 0
        high = len(items) - 1
        
    # TODO: Check if list or range is so small it's already sorted (base case)
    if len(items) <= 1:
        return items
    
    # TODO: Partition items in-place around a pivot and get index of pivot
    partition_index = partition(items, low, high)
    
    # TODO: Sort each sublist range by recursively calling quick sort
    quick_sort(items, 0, partition_index)
    
quick_sort([1, 2, 5, 6, 0])