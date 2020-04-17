// Generate Parantheses

class Solution {
    public List<String> generateParenthesis(int n) {
        List<String> ourList = new ArrayList<String>();
        generateStrings(ourList, "", 0, 0, n);
        return ourList;
    }
    
    public void generateStrings(List<String> list, String sequence, int open, int close, int max) {
        // add sequence to list of valid strings once it becomes size of max*2 
        if (max * 2 == sequence.length()) {
            list.add(sequence);
            return;
        }
        // ( should be the first thing we add
        // can add up to n opening brackets
        if (open < max) {
            generateStrings(list, sequence + '(', open + 1, close, max);
        }
        // can only add closing bracket up to as much as how many opening brackets exist
        // ) must be the last thing we add
        if (close < open) {
            generateStrings(list, sequence + ')', open, close + 1, max);
        }
    }
}
