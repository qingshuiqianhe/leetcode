# coding:utf-8
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        count = 1
        list1 = list(s)
        list2 = []
        for i in range(1, len(list1)):
            if list1[i - 1] != list1[i] and list1[i] not in list2:
                if i == 1:
                    list2.append(list1[i - 1])
                list2.append(list1[i])
                count += 1
            if list1[i] in list2:

                if i == len(list1) - 1:
                    return count


    def test2(self, s):
        list1 = list(s)
        count = 1
        list2 = []
        mm = ''
        for i in range(1, len(list1)):
            if list1[i - 1] != list1[i] and list1[i] not in list2:
                if i == 1:
                    list2.append(list1[i - 1])
                    mm += list1[i-1]
                list2.append(list1[i])
                count += 1
                mm += list1[i]
            if list1[i] in list2:
                if i == len(list1) - 1:
                    return mm, count


if __name__ == "__main__":
    s = 'asdfghjg'
    ss = Solution()
    print ss.lengthOfLongestSubstring(s)
    print ss.test2(s)

