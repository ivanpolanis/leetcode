package leetcode

func topKFrequent(nums []int, k int) []int {
	m := make(map[int]int)

	for _, n := range nums {
		m[n]++
	}

	freq := make([][]int, len(nums)+1)

	for key, value := range m {
		freq[value] = append(freq[value], key)
	}

	var res []int
	for i := len(freq) - 1; i >= 0; i-- {
		if k == len(res) {
			break
		}
		res = append(res, freq[i]...)
	}

	return res
}
