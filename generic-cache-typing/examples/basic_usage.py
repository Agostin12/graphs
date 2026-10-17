from generic_cache import Cache, combine


integers = Cache([1, 2, 3])
strings = Cache(["a", "b"])
mixed = combine(integers, strings)

print(mixed.items)
# Expected runtime output: [1, 2, 3, 'a', 'b']
#
# Static type checkers should infer the result as Cache[int | str].
# Check this with your installed type-checker version.
