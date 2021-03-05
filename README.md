# My Github repo for IT3038C

### LAB 7 EXAMPLE

Here is how you can run a Python script that I created, which uses a plugin called Char Collection. This plugin is designed to generate a sequence for passwords that generates between 1 to 75 characters, including special characters. 
First, we will create a Virtual ENV.

```bash
virtualenv C:\venv\CharCollection
source C:\venv\webscraping\scripts\activate.ps1
pip install char-collection
```

After this we will test out the initial simple use case 

```python
From char_collection.collect import CharacterSequence

Collect = CharacterSequence()
Collect.collect(10) # Q#,PT^$o&W (random string)
```

This next example would be how you could generate a password.

```python
From char_collection.collect_password 
Import CollectPassword

Generator = CollectPassword()
Generator.collect(8) # B|Gd”;;b
```

Additionally you can also use this plugin to generate a password without special characters like this.

```python
From char_collection.collect_password
Import CollectPasswordNotSpecialSymbol

Generator_not_special_symbol = CollectPasswordNotSpecialSymbol()
Generator_not_special_symbol.collect(8) # L3nAIorm
```
Once you are finished testing out the generator, don't forget to deactivate your virtualenv.

```bash
deactivate
```

#Example code for this lab was referenced from the project description via Beloslav on pypi.org
