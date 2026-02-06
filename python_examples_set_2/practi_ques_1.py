# You are given a list of integer exam scores (0–100). First curve every score by adding 5 marks but cap the maximum at 100. Then filter out all scores strictly below 40 (fail). Print the final curated list. Use map for curving and filter for pass selection. Do not use loops.# Include basic input validation: if any score is outside 0–100 before curving, print Invalid input
import sys
parts = input().split()
try:
    raw = list(map(int, parts))
except ValueError:
    print("Invalid input")
    sys.exit()
if any(x < 0 or x > 100 for x in raw):
    print("Invalid input")
else:
    curved = map(lambda s: min(s + 5, 100), raw)
    passed = list(filter(lambda s: s >= 40, curved))
    print(passed)