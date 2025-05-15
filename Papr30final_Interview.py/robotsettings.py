* settings *
| Library | Collections
#| Resource | test1.robot


#| Suite setup | Run keywords |
#| | ... | Test | AND
#| | ... | Test1

#| Suite Teardown | run keywords |
#| | ... | Test | AND
#| | ... | Test1

* variables *
| @{list1} |
| &{dict1} |

* keywords *
| test_func
| | [Arguments] | ${res} | ${res1}
| | Log | Test function
| | [RETURN] | ${res} | ${res1}

* Test cases *
| Test_1
| | ${n1} = | Set Variable | 4
| | ${n2} = | Set Variable | 5
| | ${res} = | Evaluate | ${n1} < ${n2}
| | Log | ${res}

| Test_2
| | [Tags] | Tier1
| | ${t} | ${t1} = | Run keyword | test_func | successful | 200
| | Run keyword if | ${t1} == ${200}
| | ... | LOG | Successful
| | ... | ELSE | Not successful

| Test_3
| | Append To List | ${list1} | apple | banana | orange
| | Log | ${list1}
| | FOR | ${item} | IN | @{list1}
| | | LOG | ${item}
| | | Run keyword if | '${item}' == "apple"
| | | ... | Log | "fruits is appale
| | | ... | ELSE | LOG | "not apple"
| | END
#| | Remove from List | ${list1} | orange
#| | LOG | ${list1}

| Test_4
| | ${dict2} = | Create Dictionary | name=Ram | age=21
| | ${list2} = | Create List | 2 | 3 | 4
| | FOR | ${item} | IN | @{list2}
| | | Exit for loop if | ${item} == ${3}
| | END
| | LOG | ${item}
| | Append to list | ${list1} | grapes | jackfruits
| | ${res} = | Combine lists | ${list1} | ${list2}
| | LOG | ${res}
| | List should contain value | ${res} | jackfruits
| | Set to dictionary | ${dict2} | dept=research
| | LOG | ${dict2}
| | ${keys} = | Get dictionary keys | ${dict2}
| | LOG | ${keys}
| | Remove from dictionary | ${dict2} | age
| | LOG | ${dict2}

| Test_5
| | ${str1} = | Set Variable | Abhi${SPACE}Ram
| | ${str2} = | SEt Variable | Rams
| | ${res} = | Get Length | ${str1}
| | Log | ${res}
| | ${res} = | strip String | ${str1} | ${SPACE}
| | LOG | ${res}