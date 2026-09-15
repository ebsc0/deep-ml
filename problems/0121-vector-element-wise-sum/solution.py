def vector_sum(a: list[int|float], b: list[int|float]) -> list[int|float]:
	# If vectors have different lengths, return -1.
	if len(a) != len(b): return -1

	# Return the element-wise sum of vectors 'a' and 'b'.
	return [a_i + b_i for a_i, b_i in zip(a,b)]
		