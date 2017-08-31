/*
Author: zouying@gmail.com

1. use map[byte]uint32

2. use sort

*/
package main

import (
	"fmt"
	"sort"
	"strings"
)

// use sort
func permutation1(s1, s2 string) bool {
	if sortString(s1) == sortString(s2) {
		return true
	}

	return false
}

func sortString(s1 string) string {
	s := strings.Split(s1, "")
	sort.Strings(s)

	return strings.Join(s, "")
}

func permutation2(s1, s2 string) bool {
	// to storage count of byte in s1
	map1 := make(map[string]uint32)

	ss := strings.Split(s1, "")

	// count
	for _, s := range ss {
		_, ok := map1[s]
		if !ok {
			map1[s] = 0
		}

		map1[s]++
	}

	// determine
	ss2 := strings.Split(s2, "")
	for _, s := range ss2 {
		// if new byte, then not equal
		_, ok := map1[s]
		if !ok {
			return false
		}

		// found it, reduce
		map1[s]--
		if map1[s] < 0 {
			return false
		}
	}

	// determine
	for _, v := range map1 {
		if v != 0 {
			return false
		}
	}

	return true
}

func main() {
	s := sortString("baclkj")

	fmt.Println(s)
}
