# ebi-dev-challenge
This program takes csv input as in [sample.csv](sample.csv) format and generate a json respresentation of it.

## Usage
The program can take input in two modes.

1. **File input mode:** Pass the filename as argument to the program. The program will take exactly one file for processing.
 If multiple files are present, the first file will be taken.
     ```bash
    $ ./jsonformat.py sample.csv 
    {
      "person": [
        {
          "favourite_colour": "red", 
          "first_name": "John", 
          "last_name": "Keynes", 
          "age": "29"
        }, 
        {
          "favourite_colour": "blue", 
          "first_name": "Sarah", 
          "last_name": "Robinson", 
          "age": "54"
        }
      ]
    }
    ```
 2.  **User input mode:** If no filename is given as argument, the program will read the data from the user from STDIN.
  
    ```bash
    $ ./jsonformat.py
    Enter data: Ctrl-D (i.e. EOF) to exit after entering return key
    first_name,surname,age,nationality,favourite_colour
    John,Keynes,29,British,red
    Sarah,Robinson,54,,blue
    ^D
    {
      "person": [
        {
          "favourite_colour": "red", 
          "first_name": "John", 
          "last_name": "Keynes", 
          "age": "29"
        }, 
        {
          "favourite_colour": "blue", 
          "first_name": "Sarah", 
          "last_name": "Robinson", 
          "age": "54"
        }
      ]
    }
    ```
    or like this:
    
    ```bash
    $ echo "first_name,surname,age,nationality,favourite_colour
    > John,Keynes,29,British,red
    > Sarah,Robinson,54,,blue" | ./jsonformat.py
    Enter data: Ctrl-D (i.e. EOF) to exit after entering return key
    {
      "person": [
        {
          "favourite_colour": "red", 
          "first_name": "John", 
          "last_name": "Keynes", 
          "age": "29"
        }, 
        {
          "favourite_colour": "blue", 
          "first_name": "Sarah", 
          "last_name": "Robinson", 
          "age": "54"
        }
      ]
    }
    ```
    