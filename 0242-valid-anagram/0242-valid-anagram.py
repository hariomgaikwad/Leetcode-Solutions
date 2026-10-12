class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
            list_s = list(s)
            list_t = list(t)

            if len(s) != len(t):
                return False 

            for i in list_s:
                if i in list_t:
                    list_t.remove(i)

                else:
                    return False  
                
            return True
        