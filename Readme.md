# Markdown to HTML convertor

This is a tool for converting Markdown I have developed as the first laboratory. My program converts most common 
Markdown such as  bold text (**), monospaced text (`),italic text (_) paragraphs and backticks.My program also handles both
**Cyrillic** and **Latin** letters.
In addition to converting Markdown to HTML, 
the program is designed to output the converted HTML both to a file and to stdout
I also implemented error handling which detects various issues, like not closed tags, invalid combination of tags. 
As an enhancement to main functionality, my program also converts some valid nested tags into html.

# How to install

1. First you must make sure that you have Python installed
(3.10 version is preferable, but it must run on almost all versions, because I did not use any external packages).
2. After that, you have to clone this repository and enter the working folder :
```bash
$ git clone https://github.com/Andry925/Methodologies1.git
$ cd Methodologies1
```
3. In order to start go to the main folder and find convertor.py :
```bash
$ cd main
```

# Usage 
I also decided to add the markdown_files package, which holds some Markdown files with examples to show how my program 
handles different types of tags and catches errors.
1. The application outputs the generated HTML markup to the standard output and to the HTML file you need to specify.
![Screenshot from 2024-03-14 13-39-23](https://github.com/Andry925/Methodologies1/assets/114020399/e94ca478-0c38-497c-88ef-ca55d97b8707)

2. Go to the convertor.py and find this construction. Here, inside HtmlConvertor class, give the **full path** to the 
markdown file you want to convert. For the second argument give the **full path** to an existing html file(if file does
not exist specified html file will be automatically created).Also do not forget to add **<meta charset="utf-8">** to the 
html to correctly display Cyrillic letters.

# Link to revert commit

[Here you will find revert commit](https://github.com/Andry925/Methodologies1/commit/3b6a3e5ba5f09c37cfcc954f8a60d81ae7183de3)
