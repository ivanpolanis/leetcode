package leetcode

func search(nums []int, target int) int {
	n := len(nums)

	b, t := 0, n-1

	for b < t {
		i := b + (t-b)/2
		if nums[i] >= target {
			t = i
		} else {
			b = i
		}
	}

	if b < len(nums) && nums[b] == target {
		return b
	}

	return -1
}
