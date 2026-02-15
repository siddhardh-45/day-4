Description
This program analyzes student login activity scores and generates a security report based on predefined risk levels and a personalized filtering rule.
How It Works
The register number is fixed as 668.
The user enters the number of activity scores.
Scores are stored in a list using a loop.
Each score is processed as follows:
Scores less than 0 are ignored.
0–30 → Low Risk
31–60 → Medium Risk
61–100 → High Risk
Greater than 100 → Critical Risk
The program checks whether the register number is even or odd:
Since 668 is even, all Low Risk scores are removed.
Finally, the program displays:
Final categorized risk lists
Total valid entries
Total ignored entries
Number of entries removed due to personalization
Personalization Rule Used
Register Number: 668
Last digit: 8 (Even)
Filtering applied: Low Risk scores removed
Output
The final output shows the updated risk categories and summary counts after applying the personalized security filter.
