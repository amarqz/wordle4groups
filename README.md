# wordle4groups ⬜🟨🟩
This repository is home to a Telegram bot project that processes the daily Wordle results of the users in a group.

Current features:

1. **Wordle result processing:** every time a player inputs their Wordle results in a text message, it is parsed and its important information is stored into .csv files. These files will be named as day#.csv, where # is the played puzzle number.
2. **Ranking system:** if the command */wordlerank* is called, it will return an ordered list with the players and their points.

Future plans: use this information to create and visualize statistics. This will probably be implemented on a Webapp.

**Note:** *In the future, the webpage may include translations into other languages. As it may be released on Github.*

<details>
<summary><b>Project philosophy :thought_balloon:</b></summary>

This project was conceived as a for-fun activity. Thus, commits and advancements on it may not be regular.

This is part of a cross-competence learning initiative.
</details>