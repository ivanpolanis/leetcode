package leetcode

func groupAnagrams(strs []string) [][]string {
	var res [][]string

	m := make(map[[26]int][]string)
	for _, str := range strs {
		count := [26]int{}
		for _, char := range str {
			count[char-'a']++
		}

		m[count] = append(m[count], str)
	}

	for _, value := range m {
		res = append(res, value)
	}

	return res
}
