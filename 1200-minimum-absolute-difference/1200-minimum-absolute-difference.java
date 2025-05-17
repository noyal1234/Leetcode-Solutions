class Solution {
    public List<List<Integer>> minimumAbsDifference(int[] arr) {
        int n = arr.length;
        List<List<Integer>> res = new ArrayList<>();
        int mindiff = Integer.MAX_VALUE;
        Arrays.sort(arr);
        for (int i=1; i<n; i++){
            mindiff = Math.min(mindiff,arr[i]-arr[i-1]);
        }
        for (int i=1; i<n; i++){
           if(arr[i]-arr[i-1] == mindiff){
                res.add(Arrays.asList(arr[i-1],arr[i]));
           }
        }
        return res;
    }
}