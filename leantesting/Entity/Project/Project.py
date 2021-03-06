from BaseClass.Entity import Entity

from Handler.Project.ProjectBugPrioritySchemeHandler 		import ProjectBugPrioritySchemeHandler
from Handler.Project.ProjectBugReproducibilitySchemeHandler	import ProjectBugReproducibilitySchemeHandler
from Handler.Project.ProjectBugSeveritySchemeHandler		import ProjectBugSeveritySchemeHandler
from Handler.Project.ProjectBugStatusSchemeHandler			import ProjectBugStatusSchemeHandler
from Handler.Project.ProjectBugTypeSchemeHandler			import ProjectBugTypeSchemeHandler
from Handler.Project.ProjectBugsHandler						import ProjectBugsHandler
from Handler.Project.ProjectSectionsHandler					import ProjectSectionsHandler
from Handler.Project.ProjectTestCasesHandler				import ProjectTestCasesHandler
from Handler.Project.ProjectTestRunsHandler					import ProjectTestRunsHandler
from Handler.Project.ProjectUsersHandler					import ProjectUsersHandler
from Handler.Project.ProjectVersionsHandler					import ProjectVersionsHandler
from Handler.Project.ProjectWebhooksHandler					import ProjectWebhooksHandler

class Project(Entity):

	sections = None
	versions = None
	users    = None

	testRuns  = None
	testCases = None
	webhooks  = None

	bugTypeScheme            = None
	bugStatusScheme          = None
	bugSeverityScheme        = None
	bugReproducibilityScheme = None
	bugPriorityScheme        = None

	bugs = None

	def __init__(self, origin, data):
		super().__init__(origin, data)

		self.sections = ProjectSectionsHandler(origin, data['id'])
		self.versions = ProjectVersionsHandler(origin, data['id'])
		self.users    = ProjectUsersHandler(origin, data['id'])

		self.testRuns  = ProjectTestRunsHandler(origin, data['id'])
		self.testCases = ProjectTestCasesHandler(origin, data['id'])
		self.webhooks  = ProjectWebhooksHandler(origin, data['id'])

		self.bugTypeScheme            = ProjectBugTypeSchemeHandler(origin, data['id'])
		self.bugStatusScheme          = ProjectBugStatusSchemeHandler(origin, data['id'])
		self.bugSeverityScheme        = ProjectBugSeveritySchemeHandler(origin, data['id'])
		self.bugReproducibilityScheme = ProjectBugReproducibilitySchemeHandler(origin, data['id'])
		self.bugPriorityScheme        = ProjectBugPrioritySchemeHandler(origin, data['id'])

		self.bugs = ProjectBugsHandler(origin, data['id'])
