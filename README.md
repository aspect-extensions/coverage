Replacement for the 'bazel coverage' command:

- we don't accidentally bust the analysis cache with 'coverage' flags differing from 'test'
- forget having a Bazel-specific, Java-based, unmaintained LCOV merger and 'combined report' - that never should have been Bazel's job
- developers really need git-aware diff to show "incremental coverage" - which of the lines I added or modified are covered by tests?
