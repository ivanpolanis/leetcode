package leetcode

type temp struct {
	temperature int
	idx         int
}

func dailyTemperatures(temperatures []int) []int {
	var stack []temp
	res := make([]int, len(temperatures))

	for i, v := range temperatures {
		if len(stack) == 0 {
			stack = append(stack, temp{v, i})
			continue
		}

		for j := len(stack) - 1; j >= 0; j-- {
			t := stack[j]
			if t.temperature >= v {
				continue
			}
			stack = stack[:len(stack)-1]
			res[t.idx] = i - t.idx

		}

		stack = append(stack, temp{v, i})

	}

	return res
}
