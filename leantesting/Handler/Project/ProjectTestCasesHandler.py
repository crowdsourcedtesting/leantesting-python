from BaseClass.EntityList		import EntityList
from BaseClass.EntityHandler	import EntityHandler
from BaseClass.APIRequest		import APIRequest

from Entity.Project.ProjectTestCase import ProjectTestCase

class ProjectTestCasesHandler(EntityHandler):

	_projectID = None

	def __init__(self, origin, projectID):
		super().__init__(origin)

		self._projectID = projectID

	def all(self, filters=None):
		if filters is None:
			filters = {}

		super().all(filters)

		request = APIRequest(self._origin, '/v1/projects/' + str(self._projectID) + '/test-cases', 'GET')
		return EntityList(self._origin, request, ProjectTestCase, filters)

	def find(self, id_):
		super().find(id_)

		req = APIRequest(
			self._origin,
			'/v1/projects/' + str(self._projectID) + '/test-cases/' + str(id_),
			'GET'
		)
		return ProjectTestCase(self._origin, req.exec_())
