<h1 align="center">TEST TASK</h1>
<h2 align="center">

[![made by](https://img.shields.io/twitter/url?color=orange&label=telegram&logo=telegram&logoColor=orange&style=social&url=https%3A%2F%2Ft.me%2FArnerPan)](https://t.me/ArnerPan)[![made by](https://img.shields.io/badge/Done%20by-Arner%20Pan-orange)](https://t.me/ArnerPan)

</h2>

<p align="center">

<img src="https://img.shields.io/github/license/ArnerPan/Test_task">

<img src="https://img.shields.io/badge/Pytest-7.1.2-9cf" >

<img src="https://img.shields.io/badge/Python-3-9cf">

<img src="https://img.shields.io/badge/Selenium-4.3.0-9cf">

<img src="https://img.shields.io/badge/Allure--pytest-2.9.45-9cf">

<img src="https://img.shields.io/badge/chromedriver--binaryt-104-9cf">
</p>
<p align="center">
<img src="./readme_stickers/wonder.png" width ="30%" ></p>


## Description

**This repo contains a test task**



This task done according due requirements, used Python with only and  **pytest-allure ,with pure selenium**,
but honestly i'd prefer to use `selene` with some useful stuff like `pydantic` and etc... but  as told your **HR** i have to do what asked, so i just followed the conditions , **let's go on.**

**This project is done for [OTK](https://www.youtube.com/watch?v=dQw4w9WgXcQ&ab_channel=RickAstley) as test task)** .

## How to use

### via  __RUN TESTS.sh__.:-

- **just** run it, if you have installed `Python` and `Bash`

### via __PyCharm__ , or other `IDE`
- **just** run project folder and it **should** get **.venv** automaticaly , because `poetry` provides this oppotunity , **then run** tests with commandline or tap on <img src="./readme_stickers/button.png" >

### via __Command__ type:
```
pytest --alluredir=allure-report/ tests
```
 then to see report use:
 ```
 allure serve allure-report/
 ```


### **ALL** dependencies what you need to run the project are already in `.venv`-

- **if** if `your`**IDE** can't  find virtual enviroment , use **.venv** for it.
(For **PyChram** it's `-> Setting ->Project-> Python interpreter` them set **Scripts/python.exe** from `.venv` as interpreter)

## About the project.
 **Origin of  task :**

` Написать тест с использованием языка программирования Python и библиотек pytest, allure-pytest,` `selenium, chromedriver-binary:`

`1) Перейти на страницу https://www.mos.ru/`

`2) Проверить наличие шапки подвала.`

`3) Вытащить все ссылки со страницы и проверить их на 200 (280 шт.)`

`4) Открыть каждую ссылку и проверить адресную строку браузера, что открывается нужная ссылка`


**My implmentation of this task is**

`Using only Python , and libraries pytest, allure-pytest, selenium,chromedriver-binary`

`1) follow to : https://www.mos.ru/`

`2) Check what footer and header of site exists and visible`

`3) Get All links from site , check every should have responce code "200"`

`4) OPEN every link and CHECK  current url by link exactly matches with url by link`




### **tylko jedno w głowie mam....**
<p align="center">
<img src="https://cdn.discordapp.com/attachments/341525489287954432/992835019842265098/11.23.2020_..gif" width ="30%" > </p>

- Но, если честно и между нами, то искренне надеюсь на фидбек  о своей работе,от тех, для кого этот проект созадн, если вы до сюда дочитали стену из английского текста, то хорошего вам настроения , и удачного дня !:)
- But, if to be honest between us, i honsetly hope so for feedback, about my work, from those, for whom this project created, if had read all of these wall of eng text ,then have a good mood  and great day :)


## If you don't want to run tests and just want to see `Allure-report ` type : 

```
allure serve allure-report_tested_once/

```

<p align="center">
<img src="./readme_stickers/help.png" width ="30%" ></p>