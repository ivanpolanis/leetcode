package leetcode

import "strings"

func matchPair(c, v string) bool {
	switch c {
	case "(":
		return v == ")"
	case "{":
		return v == "}"
	case "[":
		return v == "]"
	}
	return false
}

func isValid(s string) bool {
	var stack []string

	for _, v := range s {
		v := string(v)
		if strings.Contains("({[", v) {
			stack = append(stack, v)
		} else {
			length := len(stack)
			if length == 0 {
				return false
			}
			c := stack[length-1]
			if !matchPair(c, v) {
				return false
			}
			stack = stack[:length-1]
		}
	}

	return len(stack) == 0
}
