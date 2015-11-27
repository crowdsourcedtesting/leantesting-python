# Lean Testing Python SDK

**Python client for [Lean Testing API](https://leantesting.com/en/api-docs)**

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
LT = LeanTestingClient()
```

----

- Get Current **Token**
```python
leantesting.getCurrentToken()
```

- Attach New **Token**
```python
leantesting.attachToken('9ErdKZXpGPnvHuJ9di92eAFqrp14GKvfHMyclGGh')
```

- Generate **Authorization URL**
```python
generatedURL = leantesting.auth.generateAuthLink(
	'DHxaSvtpl91Xos4vb7d0GKkXRu0GJxd5Rdha2HHx',
	'https://www.example.com/appurl/',
	'admin',
	'a3ahdh2iqhdasdasfdjahf26'
)
print( generatedURL )
```

- Exchange Authorization Code For **Access TOKEN**
```python
token = leantesting.auth.exchangeAuthCode(
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
leantesting.user.getInformation()
```

- Get **User** Organizations
```python
leantesting.user.organizations.all().toArray()
```

----

- List All **Projects**
```python
leantesting.projects.all().toArray()
```

- Create A New **Project**
```python
newProject = leantesting.projects.create({
	'name': 'Project135',
	'organization_id': 5779
})
print( newProject.data )
```

- Retrieve An Existing **Project**
```python
leantesting.projects.find(3515).data
```


- List **Project Sections**
```python
leantesting.projects.find(3515).sections.all().toArray()
```

- Adding A **Project Section**
```python
newSection = leantesting.projects.find(3515).sections.create({
	'name': 'SectionName'
})
print( newSection.data )
```


- List **Project Versions**
```python
leantesting.projects.find(3515).versions.all().toArray()
```

- Adding A **Project Version**
```python
newVersion = leantesting.projects.find(3515).versions.create({
	'number': 'v0.3.1104'
})
print( newVersion.data )
```


- List **Project Users**
```python
leantesting.projects.find(3515).users.all().toArray()
```


- List **Bug Type Scheme**
```python
leantesting.projects.find(3515).bugTypeScheme.all().toArray()
```

- List **Bug Status Scheme**
```python
leantesting.projects.find(3515).bugStatusScheme.all().toArray()
```

- List **Bug Severity Scheme**
```python
leantesting.projects.find(3515).bugSeverityScheme.all().toArray()
```

- List **Bug Reproducibility Scheme**
```python
leantesting.projects.find(3515).bugReproducibilityScheme.all().toArray()
```

----

- List All **Bugs** In A Project
```python
leantesting.projects.find(3515).bugs.all().toArray()
```

- Create A New **Bug**
```python
newBug = leantesting.projects.find(3515).bugs.create({
	'title': 'Something bad happened...',
	'status_id': 1,
	'severity_id': 2,
	'project_version_id': 10242
})
print( newBug.data )
```

- Retrieve Existing **Bug**
```python
leantesting.bugs.find(38483).data
```

- Update A **Bug**
```python
updatedBug = leantesting.bugs.update(118622, {
	'title': 'Updated title',
	'status_id': 1,
	'severity_id': 2,
	'project_version_id': 10242
})
print( updatedBug.data )
```

- Delete A **Bug**
```python
leantesting.bugs.delete(118622)
```

----

- List Bug **Comments**
```python
leantesting.bugs.find(38483).comments.all().toArray()
```

----

- List Bug **Attachments**
```python
leantesting.bugs.find(38483).attachments.all().toArray()
```

- Upload An **Attachment**
```python
filePath = '/place/Downloads/Images/1370240743_2294218.jpg'
newAttachment = leantesting.bugs.find(38483).attachments.upload(filePath)
print( newAttachment.data )
```

- Retrieve An Existing **Attachment**
```python
leantesting.attachments.find(21515).data
```

- Delete An **Attachment**
```python
leantesting.attachments.delete(75258)
```

----

- List **Platform Types**
```python
leantesting.platform.types.all().toArray()
```

- Retrieve **Platform Type**
```python
leantesting.platform.types.find(1).data
```


- List **Platform Devices**
```python
leantesting.platform.types.find(1).devices.all().toArray()
```

- Retrieve Existing **Device**
```python
leantesting.platform.devices.find(11).data
```


- List **OS**
```python
leantesting.platform.os.all().toArray()
```

- Retrieve Existing **OS**
```python
leantesting.platform.os.find(1).data
```

- List **OS Versions**
```python
leantesting.platform.os.find(1).versions.all().toArray()
```


- List **Browsers**
```python
leantesting.platform.browsers.all().toArray()
```

- Retrieve Existing **Browser**
```python
leantesting.platform.browsers.find(1).data
```

- List **Browser Versions**
```python
leantesting.platform.browsers.find(1).versions.all().toArray()
```

----

- Using **Filters**
```python
leantesting.projects.find(3515).bugs.all({'limit': 2, 'page': 5}).toArray()
```

- **Entity List** Functions
```python
browsers = leantesting.platform.browsers.all()
print( browsers.total() )
print( browsers.totalPages() )
print( browsers.count() )
print( browsers.toArray() )
```

- **Entity List** Iterator
When used in for loops, entity lists will automatically cycle to first page, regardless of `page` filter.
After ending the loop, the entity list will **NOT** revert to first page or the initial instancing `page` filter setting in order not to cause useless API request calls.
```python
comments = leantesting.bugs.find(38483).comments.all({'limit': 1})
for page in comments:
	print( page )
```

- **Entity List** Manual Iteration
```python
comments = leantesting.bugs.find(38483).comments.all({'limit': 1})
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
