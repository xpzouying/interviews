package main

import (
	"testing"
)

func assertEqual(t *testing.T, expect, result bool) {
	t.Helper()

	if result != expect {
		t.Fatalf("expect: %v, but result is %v", expect, result)
	}
}

func TestPermutation1(t *testing.T) {
	tt := []struct {
		name     string
		expected bool
		ss       [2]string
	}{
		{"abc vs cba is true", true, [2]string{"abc", "cba"}},
		{"aabc vs abac is true", true, [2]string{"aabc", "abac"}},
		{"aabc vs abcc is false", false, [2]string{"aabc", "abcc"}},
	}

	for _, tc := range tt {
		t.Run(tc.name, func(t *testing.T) {
			assertEqual(t, tc.expected, permutation1(tc.ss[0], tc.ss[1]))
		})
	}
}

func TestPermutation2(t *testing.T) {
	tt := []struct {
		name     string
		expected bool
		ss       [2]string
	}{
		{"abc vs cba is true", true, [2]string{"abc", "cba"}},
		{"aabc vs abac is true", true, [2]string{"aabc", "abac"}},
		{"aabc vs abcc is false", false, [2]string{"aabc", "abcc"}},
	}

	for _, tc := range tt {
		t.Run(tc.name, func(t *testing.T) {
			assertEqual(t, tc.expected, permutation2(tc.ss[0], tc.ss[1]))
		})
	}
}
