# coding:utf-8
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """

        max_len = 0
        if s is None or len(s) == 0:
            return max_len
        str_dict = {}

        one_max = 0
        start = 0
        for i in range(len(s)):
            if s[i] in str_dict and str_dict[s[i]] >= start:
                start = str_dict[s[i]] + 1
            one_max = i - start + 1
            str_dict[s[i]] = i
            max_len = max(max_len, one_max)
        return max_len

    def sss(self, s):
        if len(s) == 1:
            return 1
        if s == '':
            return 0
        alllist = []
        a = ''
        for i in range(len(s)):
            if s[i] not in a:
                a += s[i]
                if len(a) == len(s):
                    return len(s)
            else:
                alllist.append(a)
                for j in range(len(a)):
                    if a[j] == s[i]:
                        print a[j + 1:], s[i]
                        a = a[j + 1:] + s[i]
                        break
                continue
        alllist.append(a)
        for i in range(len(alllist)):
            alllist[i] = len(alllist[i])

        lengthsubstring = max(alllist)
        return lengthsubstring



if __name__ == "__main__":
    s = 'aaabaaaaaaaaa'
    ss = Solution()
    # print ss.lengthOfLongestSubstring(s)
    print ss.sss(s)


