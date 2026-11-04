f"""
	題意 :
	設計一組演算法,能把「字串陣列」編碼成「單一字串」,並在網路上傳輸後,
	還原回原本的字串陣列。

	實作兩個方法 :
	  - encode(strs: List[str]) -> str   將字串陣列編碼成一個字串
	  - decode(s: str) -> List[str]      將編碼後的字串還原成原陣列

	你不需要處理實際的網路傳輸,只要保證 decode(encode(strs)) == strs 即可。
	不得使用任何序列化函式庫(如 eval / pickle / json)。

	LeetCode 271 · Medium 🔒
	URL : https://leetcode.com/problems/encode-and-decode-strings/
	※ 此題在 LeetCode 為 Premium 鎖定題,免費帳號看不到題面。
	  上面的題意採用 NeetCode / LintCode 659 的通用敘述(兩者為同一題)。
	免費可練 : https://neetcode.io/problems/string-encode-and-decode

	Example :
	strs = ["neet","code","love","you"] -> encode -> 某個字串 -> decode -> ["neet","code","love","you"]
	strs = ["we","say",":","yes"]       -> encode -> 某個字串 -> decode -> ["we","say",":","yes"]

	Constraint :
	0 <= strs.length < 100
	0 <= strs[i].length < 200
	strs[i] 由任意 UTF-8 字元組成

	思路 :
	這一題看起來是一個設計題，在不能使用任何序列化庫的情況下要把字串編碼以及還原. 而且內容會是由任意的 UTF8 字串組成的陣列. 
	已知 strs.length 上限為100 , strs[i].length 上限為200 , 整個大串字串應該是可以被處理的

	最 Naive 的做法應該是自訂一個切分符號拿來用,但碰到的難點可能是要用什麼符號!?
	另一個想法是把 UTF-8 的每個字轉成一個數字 , 這個數字唯一映射回 UTF-8. 
	並把題目給的字串,每一個都轉成UTF-8,用一個分隔符號相連最後串成一個大字串. 
	假設 :
	a->1
	b->2
	c->3 
	並使用 "#" 作為字之間的分隔 , "|" 作為單之內分隔
	["abc","ac","c","","b",""] =>  #1|2|3#1|3#3##2# , 其中 [#xxx|xxx] , 這樣是一組,一個元素開頭就是#字號,直到遇見下一個#
	這樣就能還原. 


	複雜度 : 
	時間複雜度上 , 每一個元素需要拆出每個字元來處理.
	因此假捨元素數量為 L , 每個字元長度為S , 
	編碼的時間複雜度就是 O(L x S) , 空間複雜度也是 O(L x S) 
	解碼的時間複雜度 , 由於解碼過程是雙指標定位分隔符中央 , (left/right都只會走一輪) , 然後每一次解碼過程也是分隔符中間的文字長度.
	因此解碼的時間複雜度也是 O(L x S) 




	Trade-off :

"""

from typing import List


class Solution:

	ELEMENT_DELIMITER = "#"
	WORD_DELIMITER = "|"

	def encode(self, strs: List[str]) -> str:
		encoded = ""
		for s in strs : 
			encoded += self.ELEMENT_DELIMITER 
			# 只要字是有內容的 , 就需要拿掉尾端的 WORD_DELIMITER
			for i , char in enumerate(s) : 
				encoded += str(ord(char)) 
				if i < len(s) - 1 :
					encoded += self.WORD_DELIMITER
		# print(f"Input : {strs} , encoded : {encoded}")
		return encoded
	
	def decode(self, s: str) -> List[str]:
		results = [] 
		# Decode 的時候從 # 字號開始. 遇到#字號就是要下一個字串 
		# 用兩個指標逐步定位 ELEMENT_DELIMITER , 用輔助function解出每一組 ELEMENT_DELIMITER 之間的內容
		left , right = 0 , 0 
		while left < len(s) and right < len(s) : 
			while right  < len(s) : 
				right += 1 
				if right  < len(s) and s[right] == self.ELEMENT_DELIMITER : 
					print(f"{left} , {right}")
					decoded_string = self._decode_string(s[left+1:right])
					results.append(decoded_string) 
					left = right
					break 
		if left < len(s) and s[left] == self.ELEMENT_DELIMITER : 
			print(f"{left} , {right}")
			results.append(self._decode_string(s[left+1:right]))
		return results
	
	def _decode_string(self,partial_encoded:str): 
		# print(f"Helper : Decode Target : {partial_encoded}")

		# 1|2|3
		# 1|3
		# 3
		# 
		decoded_string = ""
		temp = ""
		for e in partial_encoded: 
			if e == self.WORD_DELIMITER : 
				decoded_string += chr(int(temp))
				temp = ""
			else : 
				temp += e
		if temp : 
			decoded_string += chr(int(temp)) 
		# print(f"Helper : Decode Result: {partial_encoded}")
		return decoded_string

		


if __name__ == "__main__":
	c = Solution()

	# 本題驗的是「round-trip」:decode(encode(strs)) 必須等於原本的 strs
	# (輸入的字串陣列, 說明)
	test_set = [
		(["neet", "code", "love", "you"], "官方範例"),
		(["we", "say", ":", "yes"], "官方範例,含冒號"),
		([], "邊界:空陣列"),
		([""], "邊界:單一空字串 —— 與空陣列必須能被區分開"),
		(["", ""], "邊界:兩個空字串 —— 長度資訊不能遺失"),
		(["#", "##", "###"], "資料本身就長得像分隔符"),
		(["4#abc", "3#de"], "資料本身就長得像『長度#內容』的編碼格式"),
		([":", ";", ":;:"], "各種標點"),
		(["a" * 199], "邊界:接近長度上限的單一字串"),
		(["中文", "🙂", "a\nb"], "UTF-8 多位元組字元與換行"),
	]

	for strs, note in test_set:
		encoded = c.encode(strs)
		result = c.decode(encoded)
		passed = result == strs
		status = "Pass" if passed else "Failed"
		print(f"{status} | {note}")
		print(f"       input  ={strs}")
		print(f"       encoded={encoded!r}")
		print(f"       decoded={result}")
