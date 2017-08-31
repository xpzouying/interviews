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
func count(num int32) uint32 {

	var total uint32

	neg := num < 0
	if neg {
		// if number is negtive, neg flag is highest bit and equal 1,
		// then remove neg flag, and +1 to total
		total = 1

		// remove unsigned flag
		num = num & (1<<31 - 1)
	}

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
