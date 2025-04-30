import java.util.HashSet;

public class FirstMissingPositive {
    public static void main(String[] args) {
        int nums[] = { 1, 2, 0 };
        Solution1 sol = new Solution1();
        sol.firstMissingPositive(nums);
    }
}

class Solution1 {
    public int firstMissingPositive(int[] nums) {
        int count = 1;
        HashSet<Integer> numsSet = new HashSet<>();
        for (int num : nums) {
            numsSet.add(num);
        }
        while (true) {
            if (numsSet.contains(count)) {
                count++;
            } else {
                return count;
            }
        }
    }
}
