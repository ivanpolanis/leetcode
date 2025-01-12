package leetcode

func containsDuplicate(nums []int) bool {
	m := make(map[int]int)

	for _, number := range nums {
		if m[number] > 0 {
			return true
		}
		m[number]++
	}

	return false
}
