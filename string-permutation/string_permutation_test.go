package main

import (
	"testing"
)

func assertEqual(t *testing.T, expect, result bool) {
	t.Helper()

	if result != expect {
		t.Errorf("expect: %v, but result is %v", expect, result)
	}
}

func TestPermutation1(t *testing.T) {
	assertEqual(t, true, permutation1("abc", "cba"))
	assertEqual(t, true, permutation1("aabc", "abac"))

	assertEqual(t, false, permutation1("aabc", "abcc"))
}

func TestPermutation2(t *testing.T) {
	assertEqual(t, true, permutation1("abc", "cba"))
	assertEqual(t, true, permutation1("aabc", "abac"))

	assertEqual(t, false, permutation1("aabc", "abcc"))
}
