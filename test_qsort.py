import qsort
import pytest


#Pivot Selection


def test_select_pivot_only_one():
    assert qsort._select_pivot(0 ,0) == 0    

def test_select_pivot_only_two():
    pivot = qsort._select_pivot(1,2)
    assert (pivot <= 2 and pivot >= 1)


#Partitioning

def test_partition_empty_arr():
    with pytest.raises(qsort.InvalidBoundError):
        qsort._partition([], 0, 0, 0) == 0

#Paritioning numbers
def test_partition_num_only_one():
    assert qsort._partition([1], 0, 0, 0) == 0

def test_partition_num_only_two():
    arr = [2,1]
    assert qsort._partition(arr, 0, 1, 0) == 1

def test_parttion_num_all_same_value():
    arr = [2,2,2,2,2,2,2,2,2,2,2]
    assert qsort._partition(arr, 0, 10, 0) == 10

def test_parttion_num_out_of_bound_pos():
    with pytest.raises(qsort.InvalidBoundError):
        qsort._partition([0, 2, 0], 0, 5, 3)

def test_parttion_num_out_of_bound_neg():
    with pytest.raises(qsort.InvalidBoundError):
        qsort._partition([0, 2, 0], -2, 2, 3)

def test_partion_two_same_repeating():
    arr = [3,3,3, 2,2,2]
    part_index = qsort._partition(arr,0,5,4)
    assert part_index == 2
    assert arr == [2,2,2,3,3,3]

def test_partition_num_end_of_arr():
    with pytest.raises(qsort.InvalidBoundError):
        arr = [9, 85, 58, 1, 5]
        qsort._partition(arr,5,5,5)


#Partitioning strings
def test_parttion_str_only_one():
    assert qsort._partition(['test'], 0, 0, 0) == 0

def test_parttion_str_only_two():
    arr = ['test2','test1']
    assert qsort._partition(arr, 0, 1, 0) == 1

def test_parttion_str_all_same_value():
    arr = ['test','test','test','test','test','test','test','test','test','test','test']
    assert qsort._partition(arr, 0, 10, 0) == 10

def test_parttion_str_out_of_bound_pos():
    with pytest.raises(qsort.InvalidBoundError):
        qsort._partition(['test', 'test2', 'test'], 0, 5, 3)

def test_parttion_str_out_of_bound_neg():
    with pytest.raises(qsort.InvalidBoundError):
        qsort._partition(['test', 'test2', 'test'], -2, 2, 3)

def test_partition_str_two_same_repeating():
    arr = ['test3','test3','test3', 'test2','test2','test2']
    part_index = qsort._partition(arr,0,5,4)
    assert part_index == 2
    assert arr == ['test2','test2','test2','test3','test3','test3']

def test_partition_str_end_of_arr():
    with pytest.raises(qsort.InvalidBoundError):
        arr = ['a', 'z', 'g', 'b', 'q']
        qsort._partition(arr,5,5,5)


#quicksort numbers
def test_quicksort_num_all_same():
    arr = [1,1,1,1,1,1,1,1,1,1,1,1]
    qsort.quicksort(arr,0,len(arr)-1)
    assert arr == [1,1,1,1,1,1,1,1,1,1,1,1]

def test_quicksort_num_only_one():
    arr = [1]
    qsort.quicksort(arr,0,len(arr)-1)
    assert arr == [1]

def test_quicksort_num_only_two():
    arr = [1,2]
    qsort.quicksort(arr,0,len(arr)-1)
    assert arr == [1,2]

def test_quicksort_num_inverse_arr():
    arr = [5,4,3,2,1]
    qsort.quicksort(arr,0,len(arr)-1)
    assert arr == [1,2,3,4,5]

def test_quicksort_num_inverse_arr():
    arr = [1,2,3,4,5]
    qsort.quicksort(arr,0,len(arr)-1)
    assert arr == [1,2,3,4,5]

#quicksort strings
def test_quicksort_str_all_same():
    arr = ['test','test','test','test','test','test','test','test','test','test','test']
    qsort.quicksort(arr,0,len(arr)-1)
    assert arr == ['test','test','test','test','test','test','test','test','test','test','test']

def test_quicksort_str_only_one():
    arr = ['test']
    qsort.quicksort(arr,0,len(arr)-1)
    assert arr == ['test']

def test_quicksort_str_only_two():
    arr = ['ab','bc']
    qsort.quicksort(arr,0,len(arr)-1)
    assert arr == ['ab','bc']

def test_quicksort_str_inverse_arr():
    arr = ['e','d','c','b','a']
    qsort.quicksort(arr,0,len(arr)-1)
    assert arr == ['a','b','c','d','e']

def test_quicksort_str_inverse_arr():
    arr = ['a','b','c','d','e']
    qsort.quicksort(arr,0,len(arr)-1)
    assert arr == ['a','b','c','d','e']
