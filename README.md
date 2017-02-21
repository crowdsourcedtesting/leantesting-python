# Lean Testing Python SDK

**Python client for [Lean Testing](https://leantesting.com/) API**

You can sign up for a Lean Testing account at [https://leantesting.com](https://leantesting.com).

## Requirements

* Python 3.0 or greater

## Installation

You don't need this source code unless you want to modify the package. If you just want to use the Lean Testing Python SDK, you should run:

    pip install --upgrade leantesting

or

    easy_install --upgrade leantesting

See http://www.pip-installer.org/en/latest/index.html for instructions
on installing pip. If you are on a system with easy_install but not
pip, you can use easy_install instead. If you're not using virtualenv,
you may have to prefix those commands with `sudo`. You can learn more
about virtualenv at http://www.virtualenv.org/

To install from source, run:

    python setup.py install

## Usage

- Including Lean Testing Python SDK
```python
from leantesting.Client import Client as LeanTestingClient
```

- Creating a new instance
```python
client = LeanTestingClient()
```

----

- Get Current **Token**
```python
client.getCurrentToken()
```

- Attach New **Token**
```python
client.attachToken('9ErdKZXpGPnvHuJ9di92eAFqrp14GKvfHMyclGGh')
```

- Generate **Authorization URL**
```python
generatedURL = client.auth.generateAuthLink(
	'DHxaSvtpl91Xos4vb7d0GKkXRu0GJxd5Rdha2HHx',
	'https://www.example.com/appurl/',
	'admin',
	'a3ahdh2iqhdasdasfdjahf26'
)
print( generatedURL )
```

- Exchange Authorization Code For **Access TOKEN**
```python
token = client.auth.exchangeAuthCode(
	'DHxaSvtpl91Xos4vb7d0GKkXRu0GJxd5Rdha2HHx',
	'DpOZxNbeL1arVbjUINoA9pOhgS8FNQsOkpE4CtXU',
	'authorization_code',
	'sOgY2DT47B2K0bqashnk0E6wUaYgbbspwdy9kGrk',
	'https://www.example.com/appurl/'
)
print( token )
```

----

- Get **User** Information
```python
client.user.getInformation()
```

- Get **User** Organizations
```python
client.user.organizations.all().toArray()
```

- Retrieve An Existing **User** Organization
```python
client.user.organizations.find(31).data
```

----

- List All **Projects**
```python
client.projects.all().toArray()
```

- Create A New **Project**
```python
newProject = client.projects.create({
	'name': 'Project135',
	'organization_id': 5779
})
print( newProject.data )
```

- Retrieve An Existing **Project**
```python
client.projects.find(3515).data
```


- List **Project Sections**
```python
client.projects.find(3515).sections.all().toArray()
```

- Adding A **Project Section**
```python
newSection = client.projects.find(3515).sections.create({
	'name': 'SectionName'
})
print( newSection.data )
```


- List **Project Versions**
```python
client.projects.find(3515).versions.all().toArray()
```

- Adding A **Project Version**
```python
newVersion = client.projects.find(3515).versions.create({
	'number': 'v0.3.1104'
})
print( newVersion.data )
```

- List **Project Test Cases**

```python
client.projects.find(3515).testCases.all().toArray()
```

- List **Project Test Runs**

```python
client.projects.find(3515).testRuns.all().toArray()
```

- Retrieve Results For **Test Run**
```python
client.projects.find(3515).testRuns.find(123).data
```

- List **Project Users**
```python
client.projects.find(3515).users.all().toArray()
```

- Remove A **Project User**
```python
client.projects.find(3515).users.delete(123)
```

- List **Bug Type Scheme**
```python
client.projects.find(3515).bugTypeScheme.all().toArray()
```

- List **Bug Status Scheme**
```python
client.projects.find(3515).bugStatusScheme.all().toArray()
```

- List **Bug Severity Scheme**
```python
client.projects.find(3515).bugSeverityScheme.all().toArray()
```

- List **Bug Reproducibility Scheme**
```python
client.projects.find(3515).bugReproducibilityScheme.all().toArray()
```

----

- List All **Bugs** In A Project
```python
client.projects.find(3515).bugs.all().toArray()
```

- Create A New **Bug**
```python
newBug = client.projects.find(3515).bugs.create({
	'title': 'Something bad happened...',
	'status_id': 1,
	'severity_id': 2,
	'project_version_id': 10242
})
print( newBug.data )
```

- Retrieve Existing **Bug**
```python
client.bugs.find(38483).data
```

- Update A **Bug**
```python
updatedBug = client.bugs.update(118622, {
	'title': 'Updated title',
	'status_id': 1,
	'severity_id': 2,
	'project_version_id': 10242
})
print( updatedBug.data )
```

- Delete A **Bug**
```python
client.bugs.delete(118622)
```

----

- List Bug **Comments**
```python
client.bugs.find(38483).comments.all().toArray()
```

----

- List Bug **Attachments**
```python
client.bugs.find(38483).attachments.all().toArray()
```

- Upload An **Attachment**
```python
filePath = '/place/Downloads/Images/1370240743_2294218.jpg'
newAttachment = client.bugs.find(38483).attachments.upload(filePath)
print( newAttachment.data )
```

- Retrieve An Existing **Attachment**
```python
client.attachments.find(21515).data
```

- Delete An **Attachment**
```python
client.attachments.delete(75258)
```

----

- List **Platform Types**
```python
client.platform.types.all().toArray()
```

- Retrieve **Platform Type**
```python
client.platform.types.find(1).data
```


- List **Platform Devices**
```python
client.platform.types.find(1).devices.all().toArray()
```

- Retrieve Existing **Device**
```python
client.platform.devices.find(11).data
```


- List **OS**
```python
client.platform.os.all().toArray()
```

- Retrieve Existing **OS**
```python
client.platform.os.find(1).data
```

- List **OS Versions**
```python
client.platform.os.find(1).versions.all().toArray()
```


- List **Browsers**
```python
client.platform.browsers.all().toArray()
```

- Retrieve Existing **Browser**
```python
client.platform.browsers.find(1).data
```

- List **Browser Versions**
```python
client.platform.browsers.find(1).versions.all().toArray()
```

----

- Using **Filters**
```python
client.projects.find(3515).bugs.all({'limit': 2, 'page': 5}).toArray()
```

- **Entity List** Functions
```python
browsers = client.platform.browsers.all()
print( browsers.total() )
print( browsers.totalPages() )
print( browsers.count() )
print( browsers.toArray() )
```

- **Entity List** Iterator
When used in for loops, entity lists will automatically cycle to first page, regardless of `page` filter.
After ending the loop, the entity list will **NOT** revert to first page or the initial instancing `page` filter setting in order not to cause useless API request calls.
```python
comments = client.bugs.find(38483).comments.all({'limit': 1})
for page in comments:
	print( page )
```

- **Entity List** Manual Iteration
```python
comments = client.bugs.find(38483).comments.all({'limit': 1})
print( comments.toArray() )

# Will return false if unable to move forwards
comments.next();      print( comments.toArray() )

# Will return false if already on last page
comments.last();      print( comments.toArray() )

# Will return false if unable to move backwards
comments.previous();  print( comments.toArray() )

# Will return false if already on first page
comments.first();     print( comments.toArray() )
```

## Security

Need to report a security vulnerability? Send us an email to support@crowdsourcedtesting.com or go directly to our security bug bounty site [https://hackerone.com/leantesting](https://hackerone.com/leantesting).

## Development

Install dependencies:

```bash
pip install -e .
```

## Tests

Install dependencies as mentioned above, then you can run the test suite:

```bash
python -m unittest2 discover
```

## Contributing

Please see [CONTRIBUTING](https://github.com/crowdsourcedtesting/leantesting-python/blob/master/CONTRIBUTING.md) for details.
