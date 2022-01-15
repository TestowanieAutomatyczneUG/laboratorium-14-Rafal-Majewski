Feature: ISBN number
	Scenario Outline: validation
		When the ISBN number is <ISBN number>
		Then the ISBN number is <validity>

		Examples:
			| ISBN number       | validity |
			| 9780672329388     | valid    |
			| 978-3-16-148410-0 | valid    |
			| 7727183882		| invalid  |
			| 978-3-16-148410   | invalid  |
			| 9999999999990	    | invalid  |
			| 0055100111118	    | valid    |
