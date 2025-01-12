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
