class Solution:
    def longestPalindrome(self, testcase: str) -> int:
        dict = {}
        for word in testcase:
            if(word in dict):
                dict[word] += 1
            else:
                dict[word] = 1

        palindrome_count = 0
        odd_count = 0

        for _key, value in dict.items():
            if(value % 2 == 0):
                palindrome_count += value
            else:
                if(odd_count == 0):
                    odd_count += 1
                    palindrome_count += value
                else:
                    palindrome_count += value-1
        return palindrome_count


testcase = "abccccdd"
longest_testcase = "civilwartestingwhetherthatnaptionoranynartionsoconceivedandsodedicatedcanlongendureWeareqmetonagreatbattlefiemldoftzhatwarWehavecometodedicpateaportionofthatfieldasafinalrestingplaceforthosewhoheregavetheirlivesthatthatnationmightliveItisaltogetherfangandproperthatweshoulddothisButinalargersensewecannotdedicatewecannotconsecratewecannothallowthisgroundThebravelmenlivinganddeadwhostruggledherehaveconsecrateditfaraboveourpoorponwertoaddordetractTgheworldadswfilllittlenotlenorlongrememberwhatwesayherebutitcanneverforgetwhattheydidhereItisforusthelivingrathertobededicatedheretotheulnfinishedworkwhichtheywhofoughtherehavethusfarsonoblyadvancedItisratherforustobeherededicatedtothegreattdafskremainingbeforeusthatfromthesehonoreddeadwetakeincreaseddevotiontothatcauseforwhichtheygavethelastpfullmeasureofdevotionthatweherehighlyresolvethatthesedeadshallnothavediedinvainthatthisnationunsderGodshallhaveanewbirthoffreedomandthatgovernmentofthepeoplebythepeopleforthepeopleshallnotperishfromtheearth"
print(Solution().longestPalindrome(longest_testcase))
