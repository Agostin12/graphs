# generic-cache-typing

Small, runnable examples for exploring generic container typing in Python 3.12+.

The project intentionally stays small: it demonstrates how a function can accept
containers with different element types and return a container whose element type
is the union of the input types.

## Requirements

- Python 3.12 or newer
- Optional development tools: `mypy` and `pytest`

## Install development tools

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install -e ".[dev]"
```

On Windows PowerShell, activate the environment with:

```powershell
.venv\Scripts\Activate.ps1
```

## Example

```python
from generic_cache import Cache, combine

numbers = Cache([1, 2, 3])
words = Cache(["one", "two"])

combined = combine(numbers, words)
print(combined.items)  # [1, 2, 3, 'one', 'two']
```

The intended static return type of `combine(numbers, words)` is
`Cache[int | str]`.

## Run the tests

```bash
python -m pytest
```

## Run static type checking

```bash
python -m mypy src tests
```

The exact diagnostic output can vary by mypy version. If a type checker reports
behaviour that differs from the examples, include the Python and type-checker
versions when opening an issue.

## Project scope

This is an educational example, not a claim that mypy or another type checker has
a bug. It does not attempt to solve context-sensitive widening of generic return
types. If you find a reproducible discrepancy, add the smallest failing example
and the exact tool output before describing it as an issue.

## Contributing

Bug reports and focused improvements are welcome. Please include:
- Python version
- Type-checker name and version
- Minimal reproducible code
- Actual output and expected output

## License

MIT. See [LICENSE](LICENSE).
