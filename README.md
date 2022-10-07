# KeePass Keyfile Generator

Generates bulk KeePass keyfiles in automated and secure way. It will create keyfiles and in addition change the create, update and access timestamp that every file looks identical.

Why?
With this script you can create multiple keyfiles to create more security based on multiple possibilities for the combination of your master password and the linked keyfile. Only with the combination of the correct and linked keefile including your master password it is possible to open the KeePass container.

Howto:
1. Adapt the value how many files you would like to create in the script:
  run_numbers = 10 # will create 10 files
2. Just run the python script and it will create n KeePass keyfiles in the same folder as script is stored
3. Link 1 of the generated keyfiles to your KeePass container

Have fun and make your life more secure by using KeePass and KeePass keyfiles.
