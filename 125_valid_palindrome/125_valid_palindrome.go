package leetcode

import (
	"regexp"
	"strings"
)

func isPalindrome(s string) bool {
	r := regexp.MustCompile("[a-zA-Z0-9]+")
	matches := r.FindAllString(s, -1)
	joined := strings.Join(matches, "")
	parsed := strings.ToLower(joined)

	n := len(parsed)
	if n <= 1 {
		return true
	}
	for i := 0; i <= (n-1)/2; i++ {
		if parsed[i] != parsed[n-i-1] {
			return false
		}
	}

	return true
}
