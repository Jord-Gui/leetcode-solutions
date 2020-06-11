# Unique Morse Code Words

class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        transformations = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
        a_dict = {}
        for i in range(len(letters)):
            a_dict[letters[i]] = transformations[i]
            
        converted = []
        transformations = 0
        for word in words:
            mapped = ""
            for char in word:
                mapped += a_dict[char]
            if mapped not in converted:
                converted.append(mapped)
                transformations += 1
        return transformations
