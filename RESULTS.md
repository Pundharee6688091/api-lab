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
- Step A4, status codes when the other user reads, changes and deletes: read 404, change 400, delete 400

## Part B
1. A real-server test can find a wrong answer (the 500) and parts that do not work together (the load balancer). A stub cannot see these. Unit tests with stubs are still useful because they are fast and show which function is broken.
2. Ratings made with the public token belong to everyone, so another student could change them during my test. A new user gives each test its own data. In Project 2 each test will create its own data and never touch other groups' data.
3. The session keeps the cookie, so every request reaches the same server. Without it, a login can go to a server that does not know the new user and fail with 401.
4. The block "all three tools excluded" revealed the defect. A 500 with an empty body gives the app nothing to show, while a 400 with a message says what was wrong. The test stays as xfail so the defect stays visible and the suite stays green, and strict=True tells me when it is fixed.
5. Base choice needs 1 + 2 + 3 + 1 + 2 = 9 tests. All combinations need 3 x 4 x 2 x 3 = 72.
6. Read got 404, change got 400 and delete got 400. All were refused and nothing changed, so it is not a security problem. The difference is a small defect, because 400 (bad request) is the wrong code and 404 would fit.
7. It returns 200 and a list of ratings that are not mine. This is a defect, because a made-up token should get 401 like "token short" did. On a real system a stranger could read other people's data.
8. An API test checks exact status codes and error messages quickly. Only a test through the web pages can check what the user sees on screen.
