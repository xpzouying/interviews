package main

import "testing"

func assertEqual(t *testing.T, expectNum, num uint32) {
	t.Helper()

	if expectNum != num {
		t.Errorf("expect number: %d, but the number is: %d", expectNum, num)
	}
}

func TestCount(t *testing.T) {
	assertEqual(t, 10, count(1023))
	assertEqual(t, 2, count(5))
	assertEqual(t, 1, count(32))
	assertEqual(t, 1, count(1))
	assertEqual(t, 0, count(0))
	assertEqual(t, 1, count(4))

	assertEqual(t, 32, count(-1))
	assertEqual(t, 31, count(-2))
	assertEqual(t, 31, count(-3))
}
