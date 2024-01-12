class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_length = 0
        # abcabcbb
        # 문자열과 다음 문자가 중복되지 않으면 해당 문자를 문자열에 추가 후 length 1 증가
        # 다음 문자가 중복되면 length, max_length 더 큰 값으로 갱신
        for i in range(len(s)):
            sub_string = ""
            sub_string += s[i]
            length = 1
            # 마지막 문자 이전
            if i + 1 < len(s):
                j = i + 1
                while(s[j] not in sub_string):
                    sub_string += s[j]
                    length += 1
                    j += 1
                    # indexError 처리
                    if j >= len(s):
                        break
                if length > max_length:
                    max_length = length
            # 마지막 문자 처리
            else:
                if length > max_length:
                    max_length = length

        return max_length