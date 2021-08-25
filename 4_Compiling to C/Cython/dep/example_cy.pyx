cpdef int function(int x):
    cdef int result = 0
    cdef int index
    for index in range(x):
        result += index
    return result