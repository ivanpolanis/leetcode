package leetcode

func twoSum(numbers []int, target int) []int {
	i, j := 0, len(numbers)-1

	for {
		res := numbers[i] + numbers[j]
		if res == target {
			return []int{i + 1, j + 1}
		}

		if res < target {
			i++
			continue
		}
		j--

	}
}
