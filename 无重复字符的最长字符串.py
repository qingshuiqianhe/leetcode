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
                        # print a[j + 1:], s[i]
                        a = a[j + 1:] + s[i]
                        break
                continue
        alllist.append(a)
        for i in range(len(alllist)):
            alllist[i] = len(alllist[i])

        lengthsubstring = max(alllist)
        return lengthsubstring

    def test2(self, s):
        """从第一个字符开始，依次写入list2,在做比较，但增加m直接获取长度，总的运行时间并没有缩减，
        已经减少类list2的增加操作"""
        list1 = list(s)
        list2 = []
        mm = ''
        m = 0
        for i in range(len(list1)):
            if list1[i] not in mm:
                mm += list1[i]
                i += 1
                if mm not in list2:
                # if len(mm) > m:
                #     m = len(mm)
                    list2.append(mm)
            else:
                for j in range(len(mm)):
                    if mm[j] == list1[i]:
                        mm = mm[j+1:] + list1[i]
                        # if len(mm) > m:
                        #     m = len(mm)
                        list2.append(mm)
                        break
            continue

        # print list2
        for mm in list2:
            if len(mm) > m:
                m = len(mm)
        return m


if __name__ == "__main__":
    s = 'adsfasdgferrekokwe'
    ss = Solution()
    # print ss.lengthOfLongestSubstring(s)
    print ss.test2(s)
    # print ss.sss(s)


