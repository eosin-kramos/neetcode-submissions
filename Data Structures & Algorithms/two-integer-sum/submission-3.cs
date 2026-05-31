public class Solution {
    public int[] TwoSum(int[] nums, int target) {
        Dictionary<int, int> indices = new Dictionary<int, int>();

        for (int i = 0; i < nums.Length; i++){
            int twoSum = target - nums[i];
            if (indices.ContainsKey(twoSum)){
                return new int[] { indices[twoSum], i};
            }
            indices[nums[i]] = i;
        }

        throw new InvalidOperationException("No valid pair found.");
    }
}
