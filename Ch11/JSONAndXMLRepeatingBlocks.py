# Demonstration of repeating blocks in JSON and XML

import json
import xml.etree.ElementTree as etree

# Build a JSON structure as a triple quoted string
myJSON = '''{
  "bandMembers": [
    {
      "name": "Nan Ometer",
      "age": 32,
      "instrument": "keyboards"
    },
    {
      "name": "Al Jeebra",
      "age": 42,
      "instrument": "guitar"
    },
    {
      "name": "Paige Turner",
      "age": 35,
      "instrument": "drums"
    }
  ]
}'''

bandMembersDict = json.loads(myJSON)
memberList = bandMembersDict['bandMembers']
for member in memberList:
    print member['name'], member['age'], member['instrument']


# Build an XML structure as a triple quoted string
myXML = '''
<bandMembers>
    <member>
        <name>Nan Ometer</name>
        <age>32</age>
        <instrument>keyboards</instrument>
    </member>
    <member>
        <name>Al Jeebra</name>
        <age>42</age>
        <instrument>guitar</instrument>
    </member>
    <member>
        <name>Paige Turner</name>
        <age>35</age>
        <instrument>drums</instrument>
    </member>
</bandMembers>'''

tree = etree.fromstring(myXML)
bandMembersList = tree.findall('member')
for member in bandMembersList:
    print member.find('name').text, member.find('age').text, member.find('instrument').text
