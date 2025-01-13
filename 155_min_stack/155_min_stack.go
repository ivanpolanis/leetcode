package leetcode

type MinStack struct {
	stack    []int
	minStack []int
}

func Constructor() MinStack {
	return MinStack{}
}

func (this *MinStack) Push(val int) {
	this.stack = append(this.stack, val)
	length := len(this.minStack)
	if length > 0 && this.minStack[length-1] < val {
		this.minStack = append(this.minStack, this.minStack[length-1])
	} else {
		this.minStack = append(this.minStack, val)
	}
}

func (this *MinStack) Pop() {
	length := len(this.stack)
	this.stack = this.stack[:length-1]
	this.minStack = this.minStack[:length-1]
}

func (this *MinStack) Top() int {
	length := len(this.stack)
	return this.stack[length-1]
}

func (this *MinStack) GetMin() int {
	length := len(this.stack)
	return this.minStack[length-1]
}
