# api-lab

## Input domain model for POST /api/ratings

| Characteristic | Blocks | Values in the tests | Test that covers the block |
|---|---|---|---|
| C1 Value of `stars` | 1 to 5 (base) | 3 | `test_base_choice_is_saved` |
| | below 1 | 0 | `test_stars_out_of_range[0]` |
| | above 5 | 6 | `test_stars_out_of_range[6]` |
| C2 Type of `stars` | whole number (base) | 3 | `test_base_choice_is_saved` |
| | decimal | 3.5 | `test_stars_wrong_type[decimal]` |
| | text | "3" | `test_stars_wrong_type[text]` |
| | missing | no field | `test_stars_missing` |
| C3 Pizza | exists (base) | a new pizza | `test_base_choice_is_saved` |
| | does not exist | 999999999 | `test_pizza_does_not_exist` |
| C4 Token | the user's own (base) | from `auth` | `test_base_choice_is_saved` |
| | none | no header | `test_token_is_invalid[no-header]` |
| | wrong length | `token short` | `test_token_is_invalid[short-token]` |
