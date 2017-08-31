/*
给定 32 (100000)，返回 1

给定 5 (101)，返回 2

给定 1023 (111111111)，返回 10
*/

package main

import (
	"fmt"
)

// count 1  in binary number, return count
func count(num uint32) uint32 {

	var total uint32

	for {
		if num == 0 {
			return total
		}

		// if the smallest is 1
		if num&1 == 1 {
			total += 1
		}

		// num = num >> 1
		num >>= 1
	}

}

func main() {
	fmt.Printf("1023: %b\n", 1023)
}
