# Markdown to HTML/ANSI

This is a tool for converting Markdown I have developed as the first laboratory. My program converts most common 
Markdown such as  bold text (**), monospaced text (`),italic text (_) paragraphs and backticks.My program also handles both
**Cyrillic** and **Latin** letters.
In addition to converting Markdown to HTML, 
the program is designed to output the converted HTML both to a file and to stdout
I also implemented error handling which detects various issues, like not closed tags, invalid combination of tags. 
As an enhancement to main functionality, my program also converts some valid nested tags into html.
Note in this new version my program also handles ANSI conversion

# How to install

1. First you must make sure that you have Python installed
(3.10 version is preferable, but it must run on almost all versions, because I did not use any external packages).
2. After that, you have to clone this repository and enter the working folder :
```bash
$ git clone https://github.com/Andry925/Methodologies_2.git
$ cd Methodologies_2/
```


# Usage 
I also decided to add the markdown_files package, which holds some Markdown files with examples to show how my program 
handles different types of tags and catches errors.

1. My application has some properties in usage that you must be aware of (Here is the case when you want to print generated ansi from the markdown file).
![Screenshot from 2024-04-02 20-54-40](https://github.com/Andry925/Methodologies_2/assets/114020399/7b583ada-40e7-414e-8529-e81bf2f7b64f)


2. If you want to have html printed, you must specify it in the format flag(because by default it is ansi).
![Screenshot from 2024-04-02 21-00-52](https://github.com/Andry925/Methodologies_2/assets/114020399/cb8a5338-19c9-4e47-9b06-1c1031883943)

3. In case when you want to have converted markdown written to a file. You must specify both format value
   and --out flag(like here for html)
![Screenshot from 2024-04-02 21-05-10](https://github.com/Andry925/Methodologies_2/assets/114020399/c6ca0b45-301c-4f23-8ea4-08095be2d5b7)


4. Or ansi format.
![Screenshot from 2024-04-02 21-06-48](https://github.com/Andry925/Methodologies_2/assets/114020399/1e303cf1-8a4b-48ef-af92-4f8ea99c1c3a)
   

   

# Links

[Here you will find revert commit](https://github.com/Andry925/Methodologies1/commit/3b6a3e5ba5f09c37cfcc954f8a60d81ae7183de3)

[Here you will find commit with failed tests](https://github.com/Andry925/Methodologies_2/commit/34288563ef6e3b0d1a4ebf5b6e91f8ecbefc445f)


# Conclusions
   Особисто я не маю дуже великого досвіду із тестування, лише писав невеличкі юніт-тести для "ендпоінтів" для власного  
   проекту на "Django", завдяки яким мені декілька разів вдалося побачити помилки в своєму коді. Хоча в цій лабараторній роботі
   юніт-тести не відкрили для мене якогось серйозного "бага", але я з впевненістю можу сказати, що вони мені значно допомогли 
   переробити архітектуру мого проекту, при цьому нічого не "зламати".
   В підсумку можу сказати, що після цієї лабараторної роботи я зрозумів, що мені варто підтягнути знання із 
   тестування.
