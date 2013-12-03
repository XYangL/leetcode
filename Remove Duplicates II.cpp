// Remove Duplicates from Sorted Array II
// Follow up for "Remove Duplicates":
// What if duplicates are allowed at most twice?
// For example,
// Given sorted array A = [1,1,1,2,2,3],
// Your function should return length = 5, and A is now [1,1,2,2,3].
class Solution {
public:
    int removeDuplicates(int A[], int n) {
        int i = 0;
    int j = 1;
    if(n>2)
    {
        int temp = A[1];
       for (i = 2; i<n; i++)
    {   
        if(A[i] != A[i-2])
        {
            A[j] = temp;
            temp = A[i];
            j++;          
        }             
    }
    A[j] = temp;
    j++; 
} else j=n;
    
    return j; 
    }
};