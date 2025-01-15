package leetcode

import "strings"

func generateParenthesis(n int) []string {
	var stack []string
	var res []string

	var backtrack func(openN, closeN int)
	backtrack = func(openN, closeN int) {
		if openN == closeN && closeN == n {
			res = append(res, strings.Join(stack, ""))
		}

		if openN < n {
			stack = append(stack, "(")
			backtrack(openN+1, closeN)
			stack = stack[:len(stack)-1]
		}

		if closeN < openN {
			stack = append(stack, ")")
			backtrack(openN, closeN+1)
			stack = stack[:len(stack)-1]
		}
	}

	backtrack(0, 0)

	return res
}
