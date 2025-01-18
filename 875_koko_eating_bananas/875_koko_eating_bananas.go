package leetcode

import "math"

func minEatingSpeed(piles []int, h int) int {
	l, r := 1, 0
	for _, v := range piles {
		if v > r {
			r = v
		}
	}

	res := r

	for l <= r {
		i := (r + l) / 2
		hours := 0
		for _, p := range piles {
			hours += int(math.Ceil(float64(p) / float64(i)))
		}

		if hours <= h {
			res = min(res, i)
			r = i - 1
		} else {
			l = i + 1
		}

	}

	return res
}
