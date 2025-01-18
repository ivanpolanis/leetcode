package leetcode

func searchMatrix(matrix [][]int, target int) bool {
	for _, inner := range matrix {
		n := len(inner)
		if inner[n-1] < target {
			continue
		}

		l, r := 0, n-1

		for l < r {

			i := l + (r-l)/2
			if inner[i] >= target {
				r = i
			} else {
				l = i + 1
			}
		}

		if l < len(inner) && inner[l] == target {
			return true
		}

	}

	return false
}
