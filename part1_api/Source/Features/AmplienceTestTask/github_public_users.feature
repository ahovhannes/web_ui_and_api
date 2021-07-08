Feature: github public users api calls
	It is possible
		To Get User info by userId

	Scenario Outline: get user info
		Given I have endpoint with the host=https://api.github.com/users
		When I add the userId=<userId>
		Then I will get appropriate values: name=<name>, id=<id>, company=<company>, location=<location>, public_repos=<public_repos>, public_gists=<public_gists>, followers=<followers>, following=<following>
		Examples:
			|userId     |name             |id       |company   |location   |public_repos |public_gists |followers |following|
			|6wl        |Gregory Loscombe |15330    |None      |Manchester |7            |11           |13        |29       |
			|ahovhannes |Hovhannes        |34022986 |None      |None       |8            |0            |1         |0        |

