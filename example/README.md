# Aspect coverage example

    # This is executable Markdown that's tested on CI.
    set -o errexit -o nounset -o xtrace
    alias ~~~=":<<'~~~sh'";:<<'~~~sh'

## Try it out

Run the py_test target with `aspect coverage`.
It should locate the coverage.dat files produced by the Python coverage library.

~~~sh
output="$(aspect coverage //src:my_test)"

# Verify that it produces the expected output - half the functions are covered
echo "${output}" | grep -q "FNF:2" || {
    echo >&2 "Functions Found should be 2 '${output}'"
    exit 1
}
echo "${output}" | grep -q "FNH:1" || {
    echo >&2 "Functions Hit should be 1 '${output}'"
    exit 1
}
~~~

