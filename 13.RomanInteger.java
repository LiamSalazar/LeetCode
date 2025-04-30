import java.util.HashMap;

public class RomanInteger {
    public static void main(String[] args) { // Método main
        String s = "IV";
        Solution sol = new Solution();
        sol.romanToInt(s);
    }
}

class Solution {
    public int romanToInt(String s) {
        int result = 0;
        HashMap<Character, Integer> romanNumerals = new HashMap<>();
        romanNumerals.put('I', 1);
        romanNumerals.put('V', 5);
        romanNumerals.put('X', 10);
        romanNumerals.put('L', 50);
        romanNumerals.put('C', 100);
        romanNumerals.put('D', 500);
        romanNumerals.put('M', 1000);
        char array[] = s.toCharArray();
        for (int i = array.length - 1; i >= 0; i--) {
            if (i == array.length - 1 || romanNumerals.get(array[i]) >= romanNumerals.get(array[i + 1])) {
                result += romanNumerals.get(array[i]);
            } else {
                result -= romanNumerals.get(array[i]);
            }
        }

        System.out.println(result);
        return result;
    }
}