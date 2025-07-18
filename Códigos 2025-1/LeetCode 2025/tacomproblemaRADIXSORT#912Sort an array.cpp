//this one is faster than the other algorithm that uses python, mostly because c is faster but too because the 
//method heap sort is faster than merge, got 48ms but with more ram usage
class Solution {
public:
    void heapify(vector<int>& nums, int n, int i) {
        int largest = i;      
        int left = 2 * i + 1; 
        int right = 2 * i + 2; 

        if (left < n && nums[left] > nums[largest])
            largest = left;

        if (right < n && nums[right] > nums[largest])
            largest = right;

        if (largest != i) {
            swap(nums[i], nums[largest]);
            heapify(nums, n, largest); //recursively heapify the affected sub-tree
        }
    }

    void buildMaxHeap(vector<int>& nums) {
        int n = nums.size();
        for (int i = n / 2 - 1; i >= 0; i--)
            heapify(nums, n, i);
    }

    vector<int> sortArray(vector<int>& nums) {
        int n = nums.size();
        buildMaxHeap(nums);

        for (int i = n - 1; i > 0; i--) {
            swap(nums[0], nums[i]); //move max to end
            heapify(nums, i, 0);    //heapify reduced heap
        }

        return nums;
    }
};

if __name__ == "__main__":
    solution = Solution()

    test1 = [9213, 29319, 12931, 19239, 39329, 23, 1, 2332, 123]

    print("Test 1:", solution.sortArray(test1))