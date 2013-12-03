// Remove Duplicates from Sorted Array
// Given a sorted array, remove the duplicates in place such that each element appear only once and return the new length.
// Do not allocate extra space for another array, you must do this in place with constant memory.
// For example,
// Given input array A = [1,1,2],
// Your function should return length = 2, and A is now [1,2].
// !! PAY ATTENTION TO : [] empty array 

class Solution {
public:
    int removeDuplicates(int A[], int n) 
{
    int i = 0;
    int j = 1;
    if(n!=0)
    {
       for (i = 1; i<n; i++)
    {
        if(A[i] != A[i-1])
        {
            A[j]=A[i];
            j++;          
        }             
    } 
} else j=0;
    
    return j;   
}
};