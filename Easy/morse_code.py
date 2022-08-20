class Solution(object):
    def uniqueMorseRepresentations(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        ENG_to_MORSE = { 
            'a':".-", 'b':"-...", 'c':"-.-.", 'd':"-..", 'e':".",
            'f':"..-.", 'g':"--.", 'h':"....", 'i':"..", 'j':".---",
            'k':"-.-", 'l':".-..", 'm':"--", 'n':"-.", 'o':"---",
            'p':".--.", 'q':"--.-", 'r':".-.", 's':"...", 't':"-",
            'u':"..-", 'v':"...-", 'w':".--", 'x':"-..-", 'y':"-.--", 'z':"--..",
        }
        
        cnt = {} 
        for word in words:
            letter_to_morse = ""
            for letter in word:
                letter_to_morse += ENG_to_MORSE[letter]
            
            if letter_to_morse not in cnt:
                cnt[letter_to_morse] = 0
            else:
                cnt[letter_to_morse] +=1
        return len(cnt)