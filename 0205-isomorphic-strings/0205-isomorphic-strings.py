class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        map_s_to_t = {}
        map_t_to_s = {}
        
        for i in range(len(s)):
            char_s = s[i]
            char_t = t[i]
            
  
            if char_s in map_s_to_t:
                if map_s_to_t[char_s] != char_t: 
                    return False
            else:
                map_s_to_t[char_s] = char_t
            
         
            if char_t in map_t_to_s:
                if map_t_to_s[char_t] != char_s:  
                    return False
            else:
                map_t_to_s[char_t] = char_s
        
        return True
