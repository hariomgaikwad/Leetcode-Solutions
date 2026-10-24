class Solution:
    def frequencySort(self, s: str) -> str:
        result = ""
        hash_map = {}

        for ch in s:
            if ch in hash_map:
                hash_map[ch] += 1
            else:
                hash_map[ch] = 1

        sorted_chars = sorted(
            hash_map.items(),
            key=lambda x: x[1],
            reverse=True
        )


        for ch, freq in sorted_chars:
            result = result + (ch * freq)

        return result
        