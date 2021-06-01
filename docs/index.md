# GET / #
Returns a random hotkey from the list

## Response Format ##
```
{
  "Program":Program used in,
  "Category":What category the hotkey belongs to,
  "Shortcut":String of keys to be pressed, seperated by "+",
  "Action":Description of what the hotkey does,
}
```

## Example Usage ##
Call:
```
url/
```
Response:
```
{
  "Program":"Word",
  "Category":"Fields",
  "Shortcut":"Ctrl+F11"
  "Action":"Lock a field.",
}
```

# GET /hotkeys?program=&category= #
Returns a list of hotkeys that are in that program and category. See below methods to get valid programs and categories

## Response Format ##
```
[List of hotkeys (see above method to see how hotkeys are formatted)]
```

## Errors ##
Will return a 400 error if the arguments aren't provided, or if an invalid program or category is given

# GET /by-keys?keys= #
Returns a list of hotkeys that start with the provided keys, keys should be seperated by a ","

## Response Format ##
```
[List of hotkeys (see first method to see how hotkeys are formatted)]
```

## Errors ##
Will return a 400 error if the argument isn't provided, or if invalid keys are given

## Example Usage ##
Call:
```
url/by-keys?keys=Alt,D
```
Response:
```
[
  {"Action":"Select text in the address bar","Category":"File Explorer","Program":"Windows 10","Shortcut":"Alt+D"},
  {"Action":"Dismiss the reminder.","Category":"Calendar","Program":"Outlook","Shortcut":"Alt+D"},
  {"Action":"Open the Check Address dialog.","Category":"Contacts","Program":"Outlook","Shortcut":"Alt+D"},
  {"Action":"Open the Draw ribbon tab.","Category":"Navigation","Program":"OneNote Windows 10","Shortcut":"Alt+D"}
]
```

# GET /programs "
Returns a list of all programs that it has hotkeys on

## Response Format ##
```
[
  "Program Name 1",
  "Program Name 2",
  "Program Name 3"
]
```

# GET /categories?program= "
Returns a list of all categories that it has hotkeys on for that program

## Response Format ##
```
[
  "Category 1",
  "Category 2",
  "Category 3"
]
```

## Errors ##
Will return a 400 error if the argument isn't provided, or if an invalid program is given
