package leetcode

func dailyTemperatures(temperatures []int) []int {
	var stack []int
	res := make([]int, len(temperatures))

	for i := len(temperatures) - 1; i >= 0; i-- {
		for len(stack) > 0 && temperatures[stack[len(stack)-1]] <= temperatures[i] {
			stack = stack[:len(stack)-1]
		}

		if len(stack) > 0 {
			res[i] = stack[len(stack)-1] - i
		}
		stack = append(stack, i)

	}

	return res
}
