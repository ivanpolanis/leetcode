package leetcode

func productExceptSelf(nums []int) []int {
	result := make([]int, len(nums))

	prefix := 1
	for idx, n := range nums {
		if idx == len(nums)-1 {
			result[0] = 1
			break
		}
		prefix *= n
		result[idx+1] = prefix
	}

	postfix := 1
	for idx := len(nums) - 1; idx > 0; idx-- {
		postfix *= nums[idx]
		result[idx-1] *= postfix
	}

	return result
}
