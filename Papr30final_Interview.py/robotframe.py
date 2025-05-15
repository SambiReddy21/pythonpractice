Robot framework is open source automation framework.Used to test web applications,APIs and databases.

----------------------------- Key features ----------------------------

keyword driven : Test cases are written in high level and human readable by using keywords.
platform independent : It can run on windows,linux and mac os.
modular : keywords used in test cases for reuse and reduces duplication.
extensible : Can extend Robot framework by using python or java based libraries.
Integration : It can be integrated with various tools like selenium,REST API and databases.

------------------- Limitations ---------------------

Nested loops can't use in robot framework.....


--------------------- Basic test structure ----------------------------

Test cases are organized in to test suite.A test suite contains settings,multiple test cases and test data.

A test file contains four sections.

1. settings : In this section we can define libraries,resources and suite setup/teardown also test setup/teardown.
2. variables : Variables will be define under this section,reusable data can be defined at different levels(test,keyword,suite)
3. keywords : Reusable keywords can be defined under this section.
4. Test cases : Tests can be written under this section by using keywords.

------------------------- keywords -----------------------------------------------------------

Robot framework relies on using keywords to perform actions.We can have built-in keywords from libraries or we can define custom keywords.

------------ commonly used libraries -------------

Robot framework can work with various libraires.Some commonly used libraries are below given.

1. selenimLibrary : Used to automate web browsers
2. RequestsLibrary : To perform API testing
3. AppiumLibrary : for mobile testing
4. SSHLibrary : For ssh connections
5. DatabseLibrary : For database connections
6. Builtin : Set of builtin keywords come from robot.

----------------------- Variables ---------------------

Different types of variables can be defined in robot framework.

1. Scalar variables : To represent single value ex., ${str1} | hello
2. List variables : Represent list of values ex., @{list1} | 3 | 4 | 8
3. Dictionary : Represent keyvalue mappings ex., &{dict1} | username=user1 | password=pwd

---------------- Running robot framework tests-------------------

robot test.robot

to run specific test cases : robot --test <test_name> <test_file>
                             robot --test Test1 test_robot.robot
                             
----------------------- Tags ---------------------------------

Tags will be used to classify test cases and to control test execution.

robot --include <tag_name> test_robot.robot (To include tags)
robot --exclude <tag_name> test_robot.robot (To exclude tags)

--------------------------------------------------------------------

After running test file robot generates log and report files in HTML format and ouput.xml file to analyze test results.


################################################################################################################################################################
BuiltIn library contains generally needed keywords.Imported automatically and always available.
Below are some of the keywords in Builtin library of robot frameowrk.It contains nearly 107 keywords.

Convert To Integer : converts given item to integer
Convert To Number : converts given item to floating point number
Convert To String : convert given item to unicode string.

Create dictionary : Creates and returns a dictionary
Create List : Create list of items

Evaluate : Evaluates given expression

ex., ${status} = | Evaluate | 0 < ${res} < 10

Exit For Loop : Stops execution of for loop and exits

Exit For loop If : Exits from for loop based on a condition with out using a keyword "Run Keyword If"

Fail : Fails the test

Get Count : Gives the count of item as how many times it is present in container

Get Length : Gives the length of given item

Run keyword : Executes the given keyword with the given arguments.

Run Keyword And Continue On Failure : Runs the keyword and continues execution if failures occurs

Run Keyword If : runs the keyword with given arguments if condition is True.

Run keywords : Runs all the keywords in sequence.

The default log level is INFO , but it can be overridden by using --loglevel command.Available levels are TRACE,ERROR,DEBUG,WARN,INFO and NONE(no logging).

Set Variable : This keyword is used to assign values to variables.

Set Variable If : Sets the variable based on condition.

Should Be Empty : Verifies whether the given item is empty

Should Not Be Empty : Verifies the given item is not empty

Should Be Equal : Verifies given objects are equal.

Should Not Be Equal : Fails if given objects are equal.

Should Be True : Fails if the given condition is not True.

Should Not Be True : Fails if the given condition is true.

Should Contain : Fails if the container does not contain item

Should Not Contains : Fails if container contains item.

Should Contain Any : Fails if container does not contain any of items.

Should Match : Fails if the given string does not match with the given pattern.

Should Not Match : Fails if the given string matches with the given pattern.

Should Not Be Empty : Verifies the given item is not empty.

Skip : Skips the rest of the current test.

Sleep : Pauses the test execution for the given time.


############################################################################################################################################################

------------------------------------ Collections -----------------------------


Collections :  This library contains the keywords to handle lists and dictionaries.

---------------- Related keywords in BuiltIn ------------

Following keywords in the BuiltIn library can also be used with lists and dictionaries:

Keyword Name			Applicable With

Create List			lists
Create Dictionary		dicts
Get Length			both
Length Should Be		both
Should Be Empty		both
Should Not Be Empty		both
Should Contain			both
Should Not Contain		both
Should Contain X Times		lists
Should Not Contain X Times	lists
Get Count			lists

Below are some of the keywords from Collections.Contains nearly 43 keywords.

Append To List, Combine Lists , Convert To List , Copy List, List Should Contain Value, List Should Not Contain Value,Lists Should Be Equal,Remove From List,Reverse List,Sort List etc.

Convert To Dictionary, Dictionaries Should Be Equal,Dictionaries Should Contain Item,Dictionary Should Contain Item,Dictionary Should Contain Key,Dictionary Should Contain Value,Get Dictionary Keys,
Get Dictionary Values,Get Dictionary Items,Remove From Dictionary ,Set To Dictionary etc.

------------------------ OperatingSystem ----------------------------------

OperatingSystem : This library contains the keywords to perform operatingsystem related tasks.

Tasks related are Create/remove files,directories and check files/directories exists or contains some thing,manipulate environment variables etc. 

Create File,Append To File, File Should Exist, File Should Not Exist,File Should Be Empty, File Should Not Be Empty,Get File,Remove File,Move file etc

Create Directory,Empty Directory ,List Files In Directory etc.

------------------------------- DateTime -----------------------------------------

DateTime : This library contains keywords to create and verify date and time.

Convert Date,Convert Time,Get Current Date etc

---------------------- String-------------------------------------

String : This library contains keywords to manipulate and verify Strings.

Following keywords from BuiltIn library can also be used with strings:

Catenate
Get Length
Length Should Be
Should (Not) Be Empty
Should (Not) Be Equal (As Strings/Integers/Numbers)
Should (Not) Match (Regexp)
Should (Not) Contain
Should (Not) Start With
Should (Not) End With
Convert To String
Convert To Bytes

Other keywords are below,

Convert To Lowercase, Convert To Uppercase, Should Be String,Should Be Title Case,Get Line,Get Line Count,Get SubString,Remove String,Replace String,Split String,Strip String etc

------------------------------- Telnet ----------------------------------

Telnet : This library provides support for connecting to telnet servers and execute commands on opened connections.

Open Connection,Login,Read,Write,Read Until,Read Until Prompt,Close Connection etc.



########################################################################################################################################################################



