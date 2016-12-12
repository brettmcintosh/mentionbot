# Server receives webhook request about new PR
#   Get changes sha and base sha
# Fetch from repo
# Get PR files from repo
# For each file
#   Blame the file with the changes commit and find the lines with the changes sha
#   Blame the file with the base commit and find the author info for the changed lines
#   Count the lines by user excluding the PR author
# Find which users are having their code changed based on thresholds
# Get the contributors for the repo
# Get the emails for each contributor (periodically?)
# Match the emails with the contributor names
# Post PR comment with contributor names to github 

