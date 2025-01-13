package leetcode

import "sort"

func longestConsecutive(nums []int) int {
	if len(nums) == 0 {
		return 0
	}
	sort.Ints(nums)

	maxConsecutive := 1
	act := 1
	var isConsecutive bool
	for idx, n := range nums {
		if idx == 0 {
			continue
		}

		if isConsecutive = n == nums[idx-1]+1 || n == nums[idx-1]; !isConsecutive {
			if maxConsecutive < act {
				maxConsecutive = act
			}
			act = 1
			continue
		}

		if n != nums[idx-1] {
			act++
		}

	}

	if maxConsecutive < act {
		maxConsecutive = act
	}

	return maxConsecutive
}
