package main

import "fmt"

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

// record the longest path for now
var longest int = 0

func longestUnivaluePath(root *TreeNode) int {
	travelNode(root)

	return longest
}

// travelNode record the longest path for root
func travelNode(root *TreeNode) int {

	if root == nil {
		return 0
	}

	var leftMax, rightMax int
	leftMax = travelNode(root.Left)
	rightMax = travelNode(root.Right)

	leftPath := 0
	rightPath := 0

	if root.Left != nil && root.Val == root.Left.Val {
		leftPath = leftMax + 1
	}

	if root.Right != nil && root.Val == root.Right.Val {
		rightPath = rightMax + 1
	}

	longest = max(longest, leftPath+rightPath)

	return max(leftPath, rightPath)
}

func max(a, b int) int {
	if a >= b {
		return a
	} else {
		return b
	}
}

func main() {
	node := &TreeNode{Val: 1, Left: nil, Right: nil}
	fmt.Printf("longest [1]: %d\n", longestUnivaluePath(node))
}
