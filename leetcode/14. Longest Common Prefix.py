from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""

        prefix = strs[0]  # 첫 번째 문자열을 기준으로 설정

        for s in strs[1:]:
            while not s.startswith(prefix):  # 접두사가 아닐 경우 줄이기
                prefix = prefix[:-1]
                if not prefix:
                    return ""

        return prefix