### iAlarm - raise alarm when internet goes down.

To set it up, in your newly created Python `venv` or `conda` env run:
* `sudo apt install sox` or install `sox` package for your OS.
* `pip install -r requirements`

To run, simply
* `python alarm.py`

The programs pings an endpoint repeatedly and if there is a timeout it will raise an alarm. By default it pings google which is sort of always up.
