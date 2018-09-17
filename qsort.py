#!/usr/bin/python
import argparse
from random import randint
import sys


#User Defined Exceptions
class InvalidInputError(Exception):
    """Raised when input values are not accepted by the script"""
    pass


class EmptyArrayError(Exception):
    """Raised when an empty array is passed as input"""
    pass


class InvalidBoundError(Exception):
    """Raised when invalid array bounds are passed to a function"""
    pass


def main():
    sys.setrecursionlimit(2000)
    try:
        arr = _parse_input()
    except InvalidInputError:
        print("The specified input was either formatted incorrectly, an invalid type, or empty.")
        exit(1)
    except Exception as err:
        print("An unknown error has occured: "+repr(err))
        exit(2)

    try:
        quicksort(arr, 0, len(arr) - 1)
        print("\n".join(str(x) for x in arr))
    except InvalidBoundError:
        print("Invalid Bounds were specififed for the array to be sorted.")
        exit(1)

    except EmptyArrayError:
        print("An empty array was passed to quicksort.")
        exit(1)

    except TypeError:
        print("Multiple types are not allowed to be specified in the same input array. Please use alphabetic or numerical input only.\n")
        exit(1)

    except Exception as err:
        print("An unknown error has occured: "+repr(err))
        exit(2)
    exit(0)


def _usage():
    """
    Function to print usage instructions. 
    """
    print("""
        Usage: python qsort.py <-n|-a> <list> <of> <elements> ... 
            Options:
                    -n - numerical sort
                    -a - alphabetical sort
        """)



def _parse_input():
    """
    Function to grab input from the command line and contruct an array. 

    Returns:
        (list) - Array of elements to be sorted

    Raises:
        InvalidInputError: If the input is empty or invalid.

    """
    try:
        #parse stdin using argparse
        parser = argparse.ArgumentParser(description='Quicksort a numberic or alphabetical list.')
        #Create mutual exclusion args for numeric vs alphabetical
        group = parser.add_mutually_exclusive_group(required=True)

        #construct array of strings or array of integers based on option
        group.add_argument('-n', metavar='list', type=int, nargs='+',
                        help='Numerical sort')

        group.add_argument('-a', metavar='list', type=str, nargs='+',
                        help='Alphabetical sort')
        args = parser.parse_args()
    except:
        raise InvalidInputError

    if args.n:
        return args.n
    else:
        return args.a
    
    



def _select_pivot(low, high):
    """
    Function to select a pivot given an array. Pivot will be selected by selecting a random index
    inbetween(inclusive) the two array bound indexes.
    Args:
        low: The lower bound of the array to sort.
        high: The upper bound of the array to sort.

    Returns:
        (int) - index of the selected pivot.

    Raises:
        InvalidBoundError: If invalid bounds are specified the function will throw.
    """
    
    #Return a random index 
    return randint(low, high)



def _partition(arr, low, high, pivot):
    """
    Function to partition an array based on a selected pivot. After paritioning,
    all values left of the pivot will be less than or equal to the pivot,
    and all values to the right of the pivot will be greater than the pivot.
    Args:
        arr: (list) The array being sorted
        low: (int) The lower bound of the array to sort.
        high: (int) The upper bound of the array to sort.
        pivot: (int) The selected pivot for this partioning
    Returns:
        (int) index of the the partition point 
    Raises:
        InvalidBoundError: If invalid bounds are specified the function will throw.
    """
    if(low < 0 or high >= len(arr)):
        raise InvalidBoundError     
    #Swap the high position and the pivot to fit our iterator scheme
    arr[high], arr[pivot] = arr[pivot], arr[high]
    pivot = high
    
    next_swap = low
    
    for current_pos in range(low, high):
        if(arr[current_pos] <= arr[pivot]):
            arr[current_pos], arr[next_swap] = arr[next_swap], arr[current_pos]
            next_swap += 1
    
    arr[next_swap], arr[pivot] = arr[pivot], arr[next_swap]
    return next_swap


def quicksort(arr, low, high):
    if(not(arr)):
        raise EmptyArrayError
    """
    This function accepts an array of elements, the lower and upper bounds in that array to 
    apply the quicksort algorithm to.
    Args:
        arr: The array being sorted
        low: The lower bound of the array to sort.
        high: The upper bound of the array to sort.

    Raises:
        InvalidBoundError: If invalid bounds are specified the function will throw.
        EmptyArrayError: If the array is empty, throw.
        TypeError: If multiple data types are in the array, throw.
    """

    #Base case when low >= high means that the last pivot value is at the end of the array
    #meaning the last value has been pivoted around and all items are in place.
    if low < high:
        pivot = _select_pivot(low, high)
        last_pivot = _partition(arr, low, high, pivot)
        quicksort(arr, last_pivot + 1, high)
        quicksort(arr, low, last_pivot - 1)



if __name__ == "__main__":
    main()
