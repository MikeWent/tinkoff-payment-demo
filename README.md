# tinkoff payment demo

## install deps

```
pacman -S python-pipenv
pipenv install --dev
```

## run
```
export TINKOFF_TERMINAL_KEY=
export TINKOFF_PASSWORD=
```
`./new.py` — create new invoice (new client)
`./cron.py` — bill existing client

## run unit tests

`pytest`
