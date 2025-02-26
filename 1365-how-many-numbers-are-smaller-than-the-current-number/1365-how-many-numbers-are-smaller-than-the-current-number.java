class Solution {
    public int[] smallerNumbersThanCurrent(int[] nums) {
        int n = nums.length;
        int num[] = new int[n];
        for(int i = 0;i<n;i++)
        {
            int count =0;
            for(int j=0;j<n;j++)
            {
                if(nums[i]>nums[j]  && j !=i)
                {
                    count++;
                }
            }
             num[i]=count;
        }
        return num;
    }
}