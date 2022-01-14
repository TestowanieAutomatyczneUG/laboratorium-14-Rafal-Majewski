Feature: PasswordValidator
	Scenario Outline: validate password
		Given there is a password validator
		and the password requires a minimum length of <min letters count> letters
		and the password requires a minimum length of <min digits count> digits
		When the password is <password>
		Then the password is <validity>

		Examples:
			| min letters count | min digits count | password | validity |
			|                   | 1                | ab5c     | valid    |
			|                   | 1                | abnc     | invalid  |
			| 3                 |                  | ab       | invalid  |
			| 2                 |                  | abc      | valid    |
			| 2                 | 3                | abc      | invalid  |
			| 2                 | 3                | ab777    | valid    |

