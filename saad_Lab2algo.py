from typing import TypeVar , Generic
T = TypeVar ( 'T' )
class GArray ( Generic [ T ]):
    # Return the element at position i
    def get ( self , i : int ) -> T :
        pass
    # Set the element at position i
    def set ( self , i : int , e : T ) -> None :
        pass
    # Changes the size of the array to n .
    # If n is less than the current size , the first n elements are kept .
    def resize ( self , n : int ) -> None :
        pass
    # Returns the length of the array .
    def length ( self ) -> int :
        pass
    # Executes selection sort ( increasing order ) on the first n
    # elements of the array until at most k swaps are made .
    def selection_sort ( self , n : int , k : int ) -> None :
        pass