# Table of Contents
* [Week 1](#week-1-feb-20---feb-26)
* [Week 2](#week-2-feb-27---mar-5)
* [Week 3](#week-3-mar-6---mar-12)
* [Week 4](#week-4-mar-13---mar-19)
* [Week 5](#week-5-mar-20---mar-26)
* [Week 6](#week-6-mar-27---april-2)
* [Week 7](#week-7-april-3---april-9)
* [Week 8](#week-8-april-10---april-16)
* [Weeks 9, 10, 11](#weeks-9-10-11-april-17---may-7)
* [Weeks 12, 13, 14](#weeks-12-13-may-8---may-21)
* [Week 15](#week-15-may-29---june-4)
* [Week 16](#week-16-june-5---june-11)
* [Week 17](#week-17-june-12---june-18)
* [Week 18](#week-18-june-19---june-25)
* [Week 19](#week-19-june-26---july-2)
* [Week 20](#week-20-july-3---july-9)

# Week 1: Feb. 20 - Feb 26

## Goals

* Complete first three books in the [YDKJS series on Github](https://github.com/getify/You-Dont-Know-JS/blob/master/up%20%26%20going/README.md), and commit associated practice exercises. 

## Recap 

As with most technical reading, I didn't get truly absorb most of the material that I read this week in the [YDKJS book](https://github.com/getify/You-Dont-Know-JS), but was exposed to several huge concepts when dealing with the Javascript language.  I took notes off and on, but my true intention for the week was to do a quick brush through of the book so that I am familiar with the concepts when I come back to the material later.  My curriculum is set to bring me back to the second half of the YDKJS book, and before reading this second half, I will review the first half with a greater working knowledge of computer science thanks to the CS50 course online.  

Many of the ideas in the book made sense thanks to some of the coding that I have already done, while others went right over my head.  It was frustrating at times, but I kept pushing through knowing that I will eventually be coming back to the concepts again and implementing them in real coding problems. 

# Week 2: Feb 27 - Mar 5

## Goals 

* Read [Learn to Code HTML & CSS](http://learn.shayhowe.com/html-css/)
* Complete [Portfolio Site Front-End Project from Free Code Camp](https://www.freecodecamp.com/challenges/build-a-personal-portfolio-webpage)

This week, my focus is on becoming more practical with my learning.  Last week was informative, but I didn't actually implement most of the things that I "learned."  

## Recap 

* Wednesday - I realized that before I get any further, I ought to learn how to sync local directories with a GitHub repo.  On Wednesday, I ready through the first 3/4 of [Git Immersion](http://gitimmersion.com/lab_16.html), and watched the last section of Udacity's ["How to Use Git and Github"](https://www.udacity.com/course/how-to-use-git-and-github--ud775) course.  I then pulled my finance_to_code repository to my local machine, and setup a remote GIT URL as an alias to the local repository.  I will now be tracking commits and practicing "best commit practices".

This week was frustrating.  Not only was I bogged down by a golf tournament and other schoolwork, but somehow I deleted all of my project files!  I completed my portfolio site Sunday night, had it looking good, and then when I tried to open it up after closing, it was completely gone.  I believe that I mistakenly overwrote the files when I attempted to pull changes from my submodule.  Usually I am careful with my saving practices when working on projects, but as a new user of git, I have to pay extra attention to what I am doing!  I did not realize how easy it was to overwrite files.  When I did the "git pull" command, I was in the submodule directory rather than the submodule copy on the main repo, which caused the version control to overwrite my work with the old files in the master repository.

The only thing I am a bit confused about is why I cannot see this action in the git log?

For now, I am going to stay away from working with submodules, and hone my basic git skills.  Each project will now live in a separate repository with its own version control.  

Unfortunately, I do not have time to redo the portfolio site, as I need to move on to the next modules in the curriculum I have created.  Despite the mishap, I learned a ton about HTML and CSS in regards to layouts and content positioning.

# Week 3: Mar 6 - Mar 12

## Goals 

* Complete CS50 Problem set 2 
* Complete CS50 Problem set 3


## Recap 

I successfully completed both problem sets this week, but they took much longer than expected.  Pset 2 required me to write a program to encrypt a string according to both a single letter "cipher code" and a cipher code made up of a string, where each letter in the string represented a different cipher value.

Relevant files: [caesar.c](https://github.com/zachgoll/finance_to_code/blob/master/cs50/pset2/caesar.c), [initials.c](https://github.com/zachgoll/finance_to_code/blob/master/cs50/pset2/initials.c), [vigenere.c](https://github.com/zachgoll/finance_to_code/blob/master/cs50/pset2/vigenere.c)

Pset3 was a bit trickier, and required a good deal of math.  The problem set aimed to teach the process of sorting arrays (both 1-d and 2-d structures), and searching through those arrays with various methods such as binary search, linear search, selection sort, bubble sort, merge sort, and insertion sort.

I did not write code for all of the sorting methods, but instead wrote my game of fifteen and find programs with selection sort.

Relevant files: [helpers.c](https://github.com/zachgoll/finance_to_code/blob/master/cs50/pset3/helpers.c), [fifteen.c](https://github.com/zachgoll/finance_to_code/blob/master/cs50/pset3/fifteen.c)

Overall, I felt that this week was a wake-up call and was my first week of this project struggling through lines of code.  Until this week, I have dealt with either reading materials or simple HTML and CSS.  This week, I found myself digging to the deepest parts of my brain sorting through all the logic within the C programs.  It seemed like these short programs took way too long, but from what I have read, that is the nature of programming, so I am not too worried about it.

# Week 4: Mar 13 - Mar 19

## Goals 

* Complete CS50 Problem set 4 
* Complete CS50 Problem set 5

## Recap 

If there is anything I can remember from this week, it would be pointers and file manipulation.  I did not even start PSET 5.  I decided that I needed to get clear on the concepts relating to pointer variables, arrays in relation to pointer variables, and all of the file manipulation functions such as fseek(), fread(), fwrite(), fopen(), which was in pset4.  After this problem set, I feel much more comfortable working with files in my C code, iterating through them, and changing parts as necessary. 

Relevant files: [recover.c](https://github.com/zachgoll/finance_to_code/blob/master/cs50/pset4/recover.c), [resize.c](https://github.com/zachgoll/finance_to_code/blob/master/cs50/pset4/resize.c), [whodunit.c](https://github.com/zachgoll/finance_to_code/blob/master/cs50/pset4/whodunit.c)

Overall, I am pleased with my learning progress.  Although these last few weeks and those moving forward won't be the most exciting, I feel that taking CS50 is creating a strong foundation for me when I move towards the realm of javascript and real-world projects.  Many of the concepts in CS50 are tedious, but implant a deep understanding of how computers work via C code. 

# Week 5: Mar 20 - Mar 26

## Goals

* Complete CS50 Problem set 5
* Read CS50 Week 6 Material (no problem set assigned)

**3/23/17 (update)**

Thanks to an intense college golf schedule and a 35 page honors project paper, I have decided to omit the week 6 reading for this week, and pair it up with the week 7 reading for next week.  I hate doing so, but I am on the road for golf for the next 8 days, and will not have sufficient time to continue at this pace.  By assigning only readings for next week, I think this will allow me to finish my honors paper and keep making progress on this project without sacrificing practice time on the golf course since it's in a sense my "full time job" at the moment!

## Recap 

The topics that I worked on were largely a product of last week's problem set.  Not only did I work with files, but also worked a great deal with pointers.  In PSET 5, all of these core concepts were fused together in order to create and work with large data structures.  The problem consisted of three parts, which included *loading* a large list of words into a "dictionary" (I chose to use a hash table as a data structure), *checking* another large file of words to see if they matched those of the dictionary (also involved the retrieval of the hash table addresses via pointers and structs), and finally *unloading*, or "freeing" the dynamically allocated memory that was used to store all of the dictionary words into the hash table.

Relevant files: [dictionary.c](https://github.com/zachgoll/finance_to_code/blob/master/cs50/pset5/dictionary.c)

This week was a tough one thanks to a heavy golf schedule that consumed the majority of my week.  I found myself working on Problem Set 5 from airport terminals at night to hotel rooms at 5 in the morning.  It was a struggle because I was not able to put in a large chunk of time until today, which made it difficult to gain momentum and build on the concepts I was learning. 

Despite this, I feel that this week was a pivotal one in this project.  I thought to myself many times throughout the week that I was never going to finish the problem set due to the difficulty of it (this was by far the most difficult one to date) and the lack of time I had to work on it.  In the end, I made it happen, and saw my problem solving knowledge improve dramatically.  Since I didn't have much time, I had to think critically and work out the most efficient way to get things done.  As a result, I stopped guessing and checking so much and started to truly learn the concepts needed to solve the problem (although it took me a while to even figure out what the problem was!).

# Week 6: Mar 27 - April 2

## Goals 

* Read CS50 Week 6 and Week 7 Material (there is no problem set associated with either of these)

## Recap 

By far the lightest week of this project, I spent time learning about the web as well as machine learning on a high level.  Prior to these two lectures, I had a fairly good understanding of web development in terms of practical application (HTML, CSS, Javascript), but did not fully understand the theory behind it (HTTP, DNS, DHCP, TCP, IP, etc.).  Although I did not learn nearly as much as the prior weeks in which I solved difficult problem sets, I enjoyed connecting the dots between some concepts that have been floating around in my mind as I began to learn web development one year ago.

Next week, I will once again be booked solid with collegiate golf and writing my honors project paper, so it will take some mental fortitude to complete problem set 6!

# Week 7: April 3 - April 9

## Goals 

* Complete CS50 Problem Set #6 

## Recap 

Finished pset6 late this week due to a 30 page Capstone research paper and a three day golf tournament at the end of the week.  This problem set introduced Python, and I enjoyed finally getting into a higher level language.  Although I previously had no experience in Python, many of the concepts from C translated into the implementations, and many of the concepts (classes, data structures, etc.) were fairly intuitive for me since I had previously read the YDKJS book (parts 1-3) and done some work in javascript.

Overall, this week was the first week in which I truly realized the power of high-level programming languages.  After several weeks of working in C, it became apparent that doing even the simplest tasks with a computer can be mundane and difficult in lower level languages.  Before CS50, I had started out with Javascript, but never appreciated or realized the power of it at the time.  Now, it feels like the possibilities are endless given all of the languages, libraries, and code snippets out there!

Below, I have included the two files which I did the most work on.  As with previous problem sets, some of the code had already been written for me, but the two files below contain a large chunk of my own code.

Relevant files: [tweets.py](https://github.com/zachgoll/finance_to_code/blob/master/cs50/pset6/tweets.py), [analyzer.py](https://github.com/zachgoll/finance_to_code/blob/master/cs50/pset6/analyzer.py)

# Week 8: April 10 - April 16

## Goals

* Complete CS50 Problem Set #7 (Finance)

## Recap

By far the longest problem set of CS50 thus far.  I spent over 20 hours putting together this finance application which allows new users to sign up, buy stocks queried from Yahoo Finance with fake money, add money to their account, search for stock quotes, sell stocks, and see their portfolio and transaction history.

I thoroughly enjoyed building this app because I was finally able to see how the front end and back end of things come together.  To build the application, I used Flask, Jinja, Python, and SQLite as my framework, templating language, programming language, and database respectively.  The reason I took so long building the application may have been due to my inexperience with ALL of these!  I had only spent 4 days working in Python prior to building this app, and had zero experience with the others!  

I still haven't figured out a good way to deploy and share my files, but will soon figure this out now that I am finally getting the hang of programming and building things.  To date, I have spent 100% of my time figuring out how to make the code work, so I haven't had the time to deploy anything.

Relevant file: [Finance Application Main File](https://github.com/zachgoll/finance_to_code/blob/master/cs50/pset7/application.py)

# Weeks 9, 10, 11: April 17 - May 7

## Goals

* Complete CS50 Problem Set #8 (Mashup)
* Complete Final Project

I have grouped the final part of CS50 together and given myself just under a month to complete them because for the end of this semester, I will have 7 days of golf tournaments, final projects in all my classes, and graduation.  My goal is to work consistently over this time period, but I will not have a large block of time to knock out the pset or final project until the final week of the semester. 

## Recap 

I was able to finish the final problem set of CS50 this past week, and figured I would make an entry before starting the final project.  The project this week was quite fun because it incorporated several different technologies all in one.  Not only did I use Python, Flask, and SQLite, but also incorporated javascript files with jQuery and AJAX implementations.  At first, it was difficult for me to understand how everything fit together, but after several hours of reading through each file over and over again, I finally came to an understanding of how information is passed from the database through to the Python routes and the HTML, and finally manipulated by javascript on the front end. 

This week is the first time I can say that I genuinely understand the difference between the front-end and the back-end of a web application.  Although still needing lots of practice, I feel that I have finally gotten to the position where I can create useful applications rather than the typical "coding practice" applications that are purely meant to develop skills (much like we did in the beginning problem sets with C coding).  

Relevant file: [main javascript file](https://github.com/zachgoll/finance_to_code/blob/master/cs50/pset8/scripts.js)

# Weeks 12, 13: May 8 - May 21

Although I did a good amount of work during this time period, I did not record any of it in the log, and being my final project for CS50, I have spent longer than a week to work on it.

# Week 14: May 22 - May 28

## *Update*

As I have been able to work more frequently since graduation, I have decided to record a semi-daily log of the various concepts and projects that I am working on in attempts to consolidate and visually see my progress each day.

### Thursday 5/25 

Spent the majority of the day setting up a local development environment with Python, re-learning the basics of programming in Python, and writing pseudocode for writing an assembler for the machine code that I have already written for the Nand2Tetris Hack Machine.  After writing the pseudocode, I realized that I would need to use Python's "re" module.  Already tired, I worked slowly to understand regular expressions via a [friendly Python documentation](https://docs.python.org/3.6/howto/regex.html#more-metacharacters) and [YouTube tutorial](https://www.youtube.com/watch?v=sZyAn2TW7GY).  Tomorrow, I hope to be able to finish writing the Assembler in Python.

### Sunday 5/28

After a few days working with regular expressions, I have begun to understand them better.  Unfortunately, I found myself writing a never-ending function in Python, and spent several hours splitting it up into less complex functions.  The assembler I am writing has several different modules, and I found myself a bit confused as to how all the modules work together.  I ended up breaking things down to the basics and doing a lot of debugging.  Tomorrow I should be able to finish up the assembler!

# Week 15: May 29 - June 4 

### Wednesday 5/31

After struggling for several days with the Assembler I was building in Python, I finally finished it!  Most of the problems I faced were with code organization and getting the regular expressions to isolate the exact part of the data that I needed.  I got the assembler to work with smaller programs written in the Hack machine language ("Hack" being an arbitrarily defined name for the computer that I am building), but it was having trouble scaling up to run the "pong" game supplied as a test file in the Nand2Tetris software suite.  The pong game had close to 25,000 lines of assembly language, and with the program that I had written, I was executing a loop where the each time the assembler translated a line of code, it had to read through the entire program.  I eventually figured out how to globalize a few variables that enabled me to only run through the program twice to build a table of symbols, and then once to execute the actual translation process.  Before, I was running through the entire program thousands of times, which at 25,000 lines of code, this would have taken all day.  As a new programmer, my main goal has been to get programs to work, but this was my first encounter with writing a workable AND efficient program.  After fixing the efficiency problem, I spent several hours debugging to later find out that a single symbol in one of my regular expressions was causing the entire program to break!  

Finally, as I was going to update my Github repository to show the new files, I ran into a problem that I hadn't before.  Since I had updated the remote repository earlier in the week, the local repository that I had to push changes from was not merged/synced with the remote repository.  This led me to several hours working through [Git Immersion](http://gitimmersion.com/lab_16.html) trying to understand how Git works under the hood.  I eventually was able to understand Git well enough to get my local and remote repositories resolved so I could push my [Assembler.py](https://github.com/zachgoll/finance_to_code/tree/master/cs50/final_project/Assembler) to the project repository.  

Completing the Assembler marked the first project that marginally resembled a "real-world" software project.  Although the file tree wasn't very complex and I didn't collaborate with others, creating the Assembler required me to write code from scratch, use Python documentation, test my program extensively, and debug until my brain was about to explode.  Yes, it was frustrating, but in the end, I am proud that I put together this program without any templates or elaborate tutorials.

### Friday 6/02

Spent the day learning about Python modules, classes, and methods via the [Learn Python the Hard Way Ebook](https://learnpythonthehardway.org/book/), and an 11 part [Python video series on YouTube](https://www.youtube.com/watch?v=ctGc6Vl1IjQ), and took [some notes](https://github.com/zachgoll/finance_to_code/tree/master/cs50/final_project/learn_python_the_hard_way).  After struggling through the implementation of the assembler last week, I realized that before moving any further in the Nand2Tetris journey, I needed to get a better grasp of Object Oriented Programming, and more specifically, Python classes.  In addition to watching these tutorial videos, I spent a good amount of time learning [strategies for planning a project](https://jeffknupp.com/blog/2014/02/04/starting-a-python-project-the-right-way/) which included the idea of "[user stories](https://learnpythonthehardway.org/book/ex43.html)."  Prior to reading these two posts, I was completely lost when trying to start a progam such as the [assembler](https://github.com/zachgoll/finance_to_code/tree/master/cs50/final_project/Assembler).  When writing this program, I pretty much dove in and solved the problem in a bottom-up manner, while both of these posts recommend starting in a top-down manner.  I'm sure both methods work for different people, but as a beginner, I feel that the planning stages of a program are crucial for my success.

### Saturday 6/03

In the morning, I learned a [method for setting up a Python project](https://learnpythonthehardway.org/book/ex46.html), which made my head spin a bit.  I didn't understand the idea of the "virtual environment" at first, but eventually realized the power and importance of setting one up for each project.  I then struggled to grasp how a virtual environment works side-by-side with git version control.  I kept thinking that when I did my commits, I would have to add all the dependencies, but finally (after 15 minutes of staring blankly at a wall) realized that this is the job of the setup.py/requirements.txt file!

After setting up the project, I spent the remainder of the day constructing my vm_translator program using classes.  In comparison to last project (assembler) where I didn't use any classes, I am finding things much easier in terms of variable access and program control.  The program itself is more modular, and with the various class methods, I find myself thinking a lot more clearly when reading through the program and deciding what to do next.  Writing the program is still difficult, but I feel more comfortable adding and removing things without breaking the entire program.  This is enormously helpful for quickly testing and iterating on the program because I am not spending all of my time trying to figure out how to get it to compile after altering one part of it.

### Sunday 6/04

I did a slight experiment today with my work.  Yesterday, I read Cal Newport's book, [Deep Work](http://calnewport.com/books/deep-work/), in an attempt to increase the efficiency in which I work.  I have been putting in a lot of hours lately, but have not felt like I have gotten much out of these hours.  Sitting in front of the computer for 8-10 hours is not difficult for me, but doing so while intensely focusing is.  After reading the book, it occurred to me that the human brain is only capable of about 4-5 hours of "deep work" a day.  As described by Newport, deep work can be defined as "professional activities performed in a state of distraction-free concentration that push your cognitive capabilities to their limit."  Evaluating the past weeks, I realized that although I've been putting in long hours, I haven't been putting in quality hours.  10 hours of moderately focused input yields about 3 hours of highly focused input (deep work) for me.  After exploring the idea, I decided to start small and split the day up into two work periods.  Both work periods were 2 hours in length, but during the 4 total hours, I did not touch my phone, email, the internet (except for documentation), or any other distraction, and pushed myself to the limit.  

In the end, these four hours resulted in me knocking out 80% of the Virtual Machine Translator that I have been at a standstill on for several days now.  I was fairly exhausted (although I could probably have done one more focused session), and realized the power of Parkinson's Law.  Tim Ferriss, whom I read his work frequently, has this in his [Not to do list](http://tim.blog/2007/08/16/the-not-to-do-list-9-habits-to-stop-now/): 

9. Do not expect work to fill a void that non-work relationships and activities should.  Work is not all of life. Your co-workers shouldn’t be your only friends. Schedule life and defend it just as you would an important business meeting. Never tell yourself “I’ll just get it done this weekend.” Review Parkinson’s Law in 4HWW and force yourself to cram within tight hours so your per-hour productivity doesn’t fall through the floor. Focus, get the critical few done, and get out. E-mailing all weekend is no way to spend the little time you have on this planet.

Thanks to this experiment, I was able to read for several hours and spend time with family all while finishing just as much work as I would have in an 8-10 hour "unfocused" day of work.  Moving forward, I hope to apply deep work on a regular basis and maximize my per-hour output.

None of these ideas are new, but today was a great reminder for me on the power of true focus.

# Week 16: June 5 - June 11

### Monday 6/05

No new concepts, just worked on writing basic arithmetic commands in machine language which I will later use in my vm_translator.

### Wednesday 6/07

Worked on implementing the first stage of the vm_translator, which is capable of translating any .vm file with the commands "push constant [index]", "add," "subtract," "less-than," "greater than," "equal," "and," "or," "not," and "negate."  My main challenge in implementing was figuring out which functions and code should go in which part of the vm_translator.  I am trying to keep the actual vm_translator as small and concise as possible and utilize the Parser and CodeWriter classes for most of the intricate code.  This was still a bit challenging because I was initially struggling to keep track of and pass variables around.

### Saturday 6/10

FINALLY finished the virtual machine translator stage 1!!  This was an exciting moment because this is my first ever Python program which utilizes classes, and works in a rather efficient, understandable way.  I still would like to improve on my commenting throughout the code, and will need to refactor the code that I have written, but I have a great sense of satisfaction finishing this program.  This program was a test of my ability to take it step by step, because trying to plan out and write the entire program at once would have been impossible.  By constantly building and testing, building and testing, I was able to make it to the end with no major roadblocks along the way.  There were certainly difficult moments throughout the process, but I was always able to debug quickly and move forward.

In comparison to the assembler that I wrote for the last chapter of the Nand2Tetris project, I spent far less time randomly debugging because of the architecture of the program.  By using Python classes and methods, it was easy to test each individual part without breaking the program.

### Sunday 6/11

Backtracked a bit today... I started the second stage of the VM Translator, and spent a good amount of the day understanding how the stack works to keep variables inherent to their called function, and how to keep functions in order with branching.  After devising a plan for implementation, I realized that some of my code was not extendible enough to accomodate new feature requests.  My parser class could parse the commands given in the first part of the vm translator, but struggled with the commands in the second part.  I ended up redoing most of the Parser class, which was discouraging, but at the same time encouraging.  I used a regular expression to get the various parts of the code that I needed, and surprisingly, I didn't spend much time at all fiddling with the syntax of the regular expression!  On just my second try, I was able to get exactly what I needed, which was exciting considering I spent hours upon hours trying to figure out regular expressions in the last project.  After a long day of re-writing code, I am ready to implement the second part of the VM translator tomorrow!

# Week 17: June 12 - June 18

### Monday 6/12

Today, I nearly completed the final parts of the Virtual Machine Translator, but had a few bugs to work through near the end of the day that I was far too tired to find.  I called it quits after about 6 hours of solid work! 

### Tuesday 6/13 

With a fresh mind, I was able to find the bugs in the VM Translator, and completed it!  After fixing the bugs, I separated and cleaned up the files and wrote a README for the project just for practice. Like the Assembler, this project took a long time to complete for me, although I learned a ton, and became much more comfortable with Python classes, file handling, and regular expressions!

### Wed - Fri 6/14 - 6/16

Moved on to the next chapter of Nand2Tetris, and was tasked with building some sort of game in the "Jack" language.  This is the language (inspired by Java) that is built specifically for compiling in the Nand2Tetris project.  Since the language was built in the interest of easy compilation, there are some serious limitations to writing code in it.  Over the last 3 days, I learned the language, and built a maze game which the user controls a small square and navigates through a maze.  If the user hits a wall, the game is over, and they have an option to reset the game.  If the user gets to the end, a success message is flashed on the screen.  This game utilizes several classes and methods (which are available in Jack).  Today (Fri.), I worked on building the game board with all of the obstacles, and quickly began to appreciate the power of languages like Python, Java, Javascript, and even C!!  Although the Jack language is supposedly a higher level language than C, I found it just as difficult if not more difficult than writing C code.  As I attempted to build a multi-dimensional array and use it throughout my program, I quickly realized that this isn't as simple as enclosing some numbers in brackets.  In the end, I decided that a large part of my code was going to have to be repetitious.  This pained me, but after spending hours and hours trying to write DRY code (without a debugger or any sort of print/printf command at my disposal), I had to call it quits and go for repetition.  In the end, I will never have to write in the Jack programming language again, but attempting to write efficient code in it has opened my eyes to the fact that not all languages have the power to write this so called "beautiful code."  I have just a few tweaks to make to the game, and I'll be moving on to writing the compiler.  I'm looking forward to getting back to some Python!

### Saturday/Sunday 6/17 - 6/18

Completed the Maze Game that I thought was going to be completed much quicker than it was!  Nevertheless, I learned a ton through creating this game.  With the Jack programming language and the simplicity of the computer platform that I was programming on, I had to be extremely careful with the instructions I was writing in the code.  Unlike a language such as Javascript which has asynchronous functionality, this language does not, which made it extremely difficult to get the motion effects on the screen to work all at the same time.  The program I wrote is relatively slow, but I believe it is fairly efficient given the resources I had. 

[Game files here.](https://github.com/zachgoll/finance_to_code/tree/master/cs50/final_project/maze_game)

# Week 18: June 18 - June 25

Took most of the week off for travel, but managed to submit my CS50 final project.

# Week 19: June 26 - July 2

## *Started 42 Piscine in Fremont, CA*

### Monday June 26

Made it through the first day of the 42 piscine.  The project today focused mainly on bash and ldap.  Had several projects to complete, and they were all challenging.  I learned several new commands today, but the main thing that I took away was how to read a man page.  Previous to today, I had never used the man pages in the terminal, but the exercises assigned here at 42 were so dependent on your knowledge of the terminal that I had to learn to read a man page quickly and correctly.  Still have a long way to go, but a great start!

### Tuesday June 27

Today was more rewarding as I began to get into more advanced shell commands and scripts.  Spent the majority of the day working with the grep and sed command, and learning how to pipe commands together.  Understanding how stdin and stdout works was helpful for piping.  After today, I feel much more agile at the command line.  This will hopefully save me a lot of time in the future as I will now be able to manipulate large groups of files, and large files in and of themselves. 

### Wednesday June 28

Did my first corrections here at 42.  I quickly realized how meticulous the grading standards are here.  After failing the first exercise for not having the correct number of bytes in my file, I knew it was going to be a rough day.  After doing corrections, I started the day02 project, which was our introduction to writing C programs.  The majority of my day was spent figuring out how to get a preloaded 42 header (init.el) via emacs.  I switched from vim to emacs as a matter of preference, so this required a little bit of extra work to figure out the basic commands for emacs.  After figuring this out, I wrote a few simple C programs (print the alphabet forwards, print the alphabet backwards only using the function putchar()).  I then spent the remainder of the night trying to get my programs to match 42's "norms."  The format required by 42 can be checked via the "norminette" utility.  I spent at least an hour on my first program sorting through all the errors and re-formatting the file to meet the norms.  Overall a frustrating day, but better days to come!

### Thursday June 29

Today consisted of two primary learning points.

1. The "Mouillenete" bot that checks our work at 42 is extremely specific, and I was once again killed by a small error in my formatting for the second day's work.  A good portion of my day was spent reading through the specifications required for writing C programs to match the bot's requirements.  The project today was to write several basic functions in C, and turn only these functions in.  At first, I had a "main()" function in my files, but found out that the bot would supply this main function.  It took me a while to realize how this was possible, but eventually, after learning how function prototyping in C works, I was able to craft my files to work with the bot.  Previously to today, all of my programs have been rather sloppy in formatting and structure.  Adhering to the bot's standards was a huge lesson in writing "clean" code and using best practices.  Although it was tedious at first, writing clean code not only helps other people read through it, but also myself!  Understanding EXACTLY how the different parts of the program work in conjunction with each other proved invaluable to my understanding of the C programming language.
2. After nailing the formatting of my code down, I moved on to the next project, which required me to brush up on pointers in C.  Going through the Nand2Tetris course was massively helpful in understanding pointers.  I still am working on understanding the concept of passing pointers through functions, but will hopefully get that nailed down tomorrow!

### Friday June 30

Passed a project for the first time here at 42!  I got myself a little behind while meticulously checking my code, but it paid off in a passed project.  In addition, I spent a good chunk of time understanding how to pass C pointers through functions, and how pointers to pointers to pointers etc. work.  Last, I implemented several simple C programs which perform the same operations as various standard library functions such as "strlen()."

I'm getting really quick in the terminal, and comfortable using the Emacs text editor.  when I first started using it I couldn't understand why it would be so useful.  I was used to typing my code in Atom, but when writing simple scripts and C functions, it's much quicker to pull up Vim or Emacs.  Additionally, I created a profile in the terminal which (when launched) automatically launches three separate windows that I can work in.  This was enormously helpful for writing and compiling code from multiple files at a time.  I then found the hotkeys, and became exponentially quicker in the terminal and Emacs because I was then able to press one key to close all terminals, and toggle quickly between them!

Learning a lot here at 42!!


### Saturday July 1

Today was busy!  Backlogged with an entire project and a group project, I stayed busy all day.  This was the first group project here at 42, and I thoroughly enjoyed the experience.  I have never worked with others on a coding project, but found it quite productive; something I have not experienced often thanks to the terribly unproductive group projects during my undergraduate education in Corporate Finance.  It was nice to have multiple eyes on the code, because we spent far less time debugging.

In terms of learning, I spent a good part of today attempting to understand the black box programmers call "recursion."  If you think about it too hard, it get's quite overwhelming.  That said, I walked through several of my programs line by line to see how the recursion was working.

### Sunday July 2

Super frustrating and rewarding day.  I got a good nights rest last night, which kept me sharp all day, but unfortunately, I wasn't quite able to finish the assigned project today.  The project was to print a pyramid with incrementing size and complexity (doors, door handles, etc.) all in the terminal as standard output.  Reflecting back on the day, I think I approached the problem incorrectly.  Although I did careful planning once I figured out the pattern and algorithm, I did not plan my functions.  I should have figured out which functions I needed, and then wrote skeleton code for those functions.  Although I learned a lot today and became more comfortable using pointers in C, I am a bit frustrated that I didn't plan out my program like I did the [vm_translator](https://github.com/zachgoll/finance_to_code/tree/master/cs50/virtual_computer_final_project/software/virtual_machine/vm_translator) several weeks ago.  Yes, C is a much more primitive language than Python (which I wrote the vm_translator in), but planning out a program follows the same principles!  Moving forward, before writing a program that is more than one function, I will plan out my functions and write solid pseudo/skeleton code before jumping in and confusing myself with all sorts of random variables.

# Week 20: July 3 - July 9
