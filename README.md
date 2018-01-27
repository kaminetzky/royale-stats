# royale-stats
The purpose of this project is to easily log a Clash Royale clan's information.

The following values of every player can be saved:
* Current weekly donations
* Last clan chest crowns


The time in the "Datetime" row is UTC.

Please create an issue if you have any doubt, problem, suggestion or comment.

### How to use royale-stats?
1. Get API key
    1. Join the [Clash Royale API Discord server](https://discord.me/cr_api).
    2. Send `!crapikey get` to the `#developer-key` channel.
    3. You will receive a DM with your API key.
2. Insert key in line 13 of `main.py` file.
3. Run `python3 main.py <CLAN ID>` in the command line.