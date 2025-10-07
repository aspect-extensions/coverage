load("@aspect_rules_py//py:defs.bzl", "py_test", "py_library")
load("@pip//:requirements.bzl", "requirement")

py_library(
    name = "my_lib",
    srcs = ["my.py"],
)

py_test(
    name = "my_test",
    srcs = ["my_test.py"],
    pytest_main = True,
    deps = [
        ":my_lib",
        requirement("coverage"),
        requirement("pytest"),
    ],
)
