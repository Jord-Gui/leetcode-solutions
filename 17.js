// Letter Combinations of a Phone Number

var letterCombinationsAux = function(digits, outputArray, aString, aDictionary) {
    if (aString.length === digits.length) {
        outputArray.push(aString);
    }
    else {
        let current_number = digits.charAt(aString.length);
        let possible_letters = aDictionary[current_number];
        for (let i = 0; i < possible_letters.length; i++) {
            letterCombinationsAux(digits, outputArray, aString + possible_letters.charAt(i), aDictionary);
        }
    }
}

/**
 * @param {string} digits
 * @return {string[]}
 */
var letterCombinations = function(digits) {
    if (digits === "") {
        return [];
    }
    const output = [];
    const dict = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl", "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"};
    letterCombinationsAux(digits, output, "", dict);
    return output;
};