package leetcode

func maxArea(height []int) int {
	i, j := 0, len(height)-1

	maxArea := -1
	for i != j {
		area := min(height[i], height[j]) * (j - i)
		if height[i] > height[j] {
			j--
		} else {
			i++
		}
		maxArea = max(maxArea, area)
	}

	return maxArea
}
