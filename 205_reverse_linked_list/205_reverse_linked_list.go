package leetcode

type ListNode struct {
	Val  int
	Next *ListNode
}

func reverseList(head *ListNode) *ListNode {
	if head == nil {
		return nil
	}
	var act *ListNode
	prev := &ListNode{head.Val, nil}
	for head.Next != nil {
		head = head.Next
		act = &ListNode{head.Val, prev}
		prev = act
	}

	return prev
}
