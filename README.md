## Selenium fbbot

### Setup

```sh
# install Selenium and ChromeDriver
pip install -U selenium
brew install chromedriver

# download repository
git clone https://github.com/goldsteinsveta/selenium_fbbot

# replace myEmail, myPass, myFriend and myMsg in fbbot.py

# run the script
cd selenium_fbbot
python fbbot.py
```

### To-do: 
- [ ] work around the ._3ixn mask popping up with "Show notifications" alert box. 3xESC should do the trick
- [ ] connect with language processing API
- [ ] deploy