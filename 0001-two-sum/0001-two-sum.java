class Solution {
    public int[] twoSum(int[] nums, int target) {
        int i, j;
        int[] a = new int[2];
        int n = nums.length;
        for (i = 0; i < n - 1; i++) {
            for (j = i + 1; j < n; j++) {
                if (nums[i] + nums[j] == target) {
                    a[0] = i;
                    a[1] = j;
                }
            }
        }
        return a;
    }
}