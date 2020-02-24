

# find all python files, then pass each file into cat (4 processed at a time).
find .. -type f -name "*.py" -print0 | xargs -0 -P4 cat
