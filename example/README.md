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
echo "${output}" | grep -q "50.0%" || {
    echo >&2 "Functions should be 50% covered: '${output}'"
    exit 1
}
~~~

