# HW2_hash_practice
## Python Dictionary and Hash
- A dictionary is actually a list, which contains columns of index, hash, key, and value as shown.
![image](https://github.com/CYchang990148/HW2_hash_practice/assets/161935555/69cfa4c3-0b52-4cfc-a98d-e76853cbff92)
- Keys are hashed to produce indexes so that it can jump to the right values.
[Reference](https://youtu.be/C4Kc8xzcA68?feature=shared)

## How to calculate how many different strings are in the file and the number of occurrences of each string
- Open the file in read mode.
```
with open('hw2_data.txt', 'r') as file:
```
- A variable, n, is set to keep track of the count of different strings.
```
n=0
```
- Initialize an empty dictionary called "dictionary".
```
dictionary = {}
```
- Iterate over each line in the file.
```
for string in file:
```
- Remove any whitespace from the current line and assign the result back to "string".
```
string = string.strip()
```
- If the current string is already in the dictionary, the value is incremented by 1; if the string is not in the dictionary, it is added as a new key and its value is set to 1. Also, "n" is incremented by 1 because of encountering a new string.
```
if string in dictionary:
      dictionary[string] += 1
    else:
      dictionary[string] = 1
      n += 1
```
- Print the results.
```
print(n , "different strings in the file")
print(dictionary)
```

## Result 
