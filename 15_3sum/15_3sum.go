package leetcode

import (
	"sort"
)

func threeSum(nums []int) [][]int {
	var res [][]int

	sort.Ints(nums)

	for i, v := range nums {
		if i > 0 && v == nums[i-1] {
			continue
		}
		l, r := i+1, len(nums)-1

		target := -1 * nums[i]
		for l < r {
			partial := nums[l] + nums[r]
			if partial < target {
				l++
			} else if partial > target {
				r--
			} else {
				res = append(res, []int{v, nums[l], nums[r]})
				l++
				for nums[l] == nums[l-1] && l < r {
					l++
				}
			}
		}

	}

	return res
}
