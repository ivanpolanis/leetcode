package leetcode

import "strconv"

func isOperand(token string) bool {
	switch token {
	case "+", "-", "/", "*":
		return true
	}
	return false
}

func makeOperation(token string, n1, n2 int) int {
	switch token {
	case "+":
		return n1 + n2
	case "-":
		return n1 - n2
	case "/":
		return n1 / n2
	case "*":
		return n1 * n2
	}
	return 0
}

func evalRPN(tokens []string) int {
	var stack []int

	for _, token := range tokens {
		if !isOperand(token) {
			v, err := strconv.Atoi(token)
			if err != nil {
				panic(err)
			}
			stack = append(stack, v)
		} else {
			length := len(stack)
			n1, n2 := stack[length-2], stack[length-1]
			result := makeOperation(token, n1, n2)
			stack = stack[:length-1]
			stack[length-2] = result
		}
	}

	return stack[0]
}
