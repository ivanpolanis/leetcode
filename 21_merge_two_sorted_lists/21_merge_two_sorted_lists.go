package leetcode

type ListNode struct {
	Val  int
	Next *ListNode
}

func mergeTwoLists(list1 *ListNode, list2 *ListNode) *ListNode {
	if list1 == nil {
		return list2
	}
	if list2 == nil {
		return list1
	}

	var head *ListNode
	if list1.Val <= list2.Val {
		head = list1
		list1 = list1.Next
	} else {
		head = list2
		list2 = list2.Next
	}

	node := head

	for list1 != nil && list2 != nil {
		if list1.Val <= list2.Val {
			node.Next = list1
			list1 = list1.Next
			node = node.Next
		} else {
			node.Next = list2
			list2 = list2.Next
			node = node.Next
		}
	}

	for list1 != nil {
		node.Next = list1
		list1 = list1.Next
		node = node.Next
	}

	for list2 != nil {
		node.Next = list2
		list2 = list2.Next
		node = node.Next
	}

	return head
}
