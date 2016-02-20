# Hro-Telegram-Bot

Scraper is the main file, Calendar is a module.

## Requirements
python-webkit2png https://github.com/adamn/python-webkit2png
python-telegram-bot https://github.com/python-telegram-bot/python-telegram-bot


## Modules 

You can add more modules by doing the following:

1. Create the following functions within a module
```python
class ExampleModule:
    def getHelpTitle(self):
        return "The title of the module"
    
    def getHelpText(self):
        return "/command returns alls the blabla"
```
2. In the scraper.py add the module to the modules array

```python
def main():
    exampleModule = ExampleModule(dp)

    modules = [calendar, exampleModule]
```

Thats it.
