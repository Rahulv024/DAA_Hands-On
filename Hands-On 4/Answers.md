Problem 1:
A. The time complexity of merge array-
    -Merge sort array recursively merges K arrays of size N, the overall time complexity is O(K*Nlog(K)), where K is the number os arrays and N is the size of the          array 

    
B. Ways on how to improve implementation-
    Parallelization: We could parallelize the merging of subrays for speeding up the operation.


Problem 2:
A. The time complexity-
  The time complexity is O(N). Where N is the size of input array. All the iterations inside the loop are O(1).

  
B. Ways on how to improve implementation-
    Parallel processing: When we have large arrays, we can split the arrays into segments and process them concurrently, and then merge the result.
    Tracking duplicates for post-processing: if we need to track the elements that were removed, we can maintain them in a different array or maintain a count of       duplicates.
