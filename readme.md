# Resume Helper

Autofill functionality in browsers often don't work when applying for jobs online. Atleast they didn't for me. As a result I created this small utility which can help me copy my specific details to the clipboard with just a key press: mostly the initial. 

## Run

To run this program. Create a virtual enviornemnt in python or globally you will need to install `pyperclip`: the library which will help us copy things to the keyboard from Python.


## Config

To cater to your information, you'll have to edit [details.py](details.py). Edit the `details` dictionary. Its key being the key you will use to copy the information. The value is a list of two items, the first is always the displayed name of the information and the second item is the actual information. 

So for example, 

```
"c": ["city", "Toronto"]
```

Here we will press "c" to copy "Toronto" to the clipboard. While on display, it will show "city".

## LinkedIn Message Features

There is also a logic to create LinkedIn messages using the "lm" key. There is some logic built into this, feel free to checkout out [main.py](main.py) for more details.