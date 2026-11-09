# API lab results

## Part 0
- Step 0.1, the number of pizza names: 18
- Step 0.3, status code of the request without a token: 401
- Step 0.4, the name of your pizza: The Clever Hawaii
- Step 0.12, results of the three runs without a session (optional):
- Step 0.16, blocks of "how many of the three tools are excluded": none, one, two, all three. I added `[]`, `["Knife", "Scissors"]` and all three.

## Defect report
- Title: Excluding all three tools gives 500
- Request: POST /api/pizza with `{"excludedTools": ["Knife", "Pizza cutter", "Scissors"]}`
- Expected result: 400 and a JSON error message
- Actual result: 500 with an empty body
- Severity: Medium. The server crashes on customer input and the app gets no message.

## Part A
- Step A4, status codes when the other user reads, changes and deletes:

## Part B
1.
2.
3.
4.
5.
6.
7.
8.
