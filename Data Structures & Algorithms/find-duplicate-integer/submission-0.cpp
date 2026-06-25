class Solution {
public:
    int findDuplicate(vector<int>& nums) {
        // use floyd's algorithm with a fast and slow pointer.
        // in the first iteration, find where fast and slow pointer meet
        // in the second iteration, iterate another slow pointer until it meets the prev slow pointer, this is the start of the cycle and hence a repeat value
        int fast = 0;
        int slow = 0;
        while (true) {
            slow = nums[slow];
            fast = nums[nums[fast]];
            if (slow == fast) {
                break;
            }
        }

        int slow2 = 0;

        while (true) {
            slow2 = nums[slow2];
            slow = nums[slow];
            if (slow == slow2) {
                return slow;
            }
        }
    }
};
