class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        refer = strs[0]
        result=""
        for step,char in enumerate(refer):
            plus = True
            for i in range(1,len(strs)): 
                try: 
                    if strs[i][step] == char: 
                        pass
                    else: 
                        plus = False
                        break
                except: 
                    return result
            if plus:
                result += char
            else: 
                return result 
        return result
                