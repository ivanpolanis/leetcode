package leetcode

func isAnagram(s string, t string) bool {
	if len(s) != len(t) {
		return false
	}

	sMap := make(map[rune]uint)

	for _, letter := range s {
		sMap[letter]++
	}

	for _, letter := range t {
		if sMap[letter] == 0 {
			return false
		}
		sMap[letter]--
	}

	return true
}

func groupAnagrams(strs []string) [][]string {
	res := [][]string{}

	for _, str := range strs {
		insertNew := true

		for idx, anagram := range res {
			if isAnagram(anagram[0], str) {
				res[idx] = append(anagram, str)
				insertNew = false
				break
			}
		}

		if !insertNew {
			continue
		}

		res = append(res, []string{str})

	}

	return res
}
