from BaseClass.EntityList		import EntityList
from BaseClass.EntityHandler	import EntityHandler
from BaseClass.APIRequest		import APIRequest

from Entity.Project.ProjectTestRun import ProjectTestRun

class ProjectTestRunsHandler(EntityHandler):

	_projectID = None

	def __init__(self, origin, projectID):
		super().__init__(origin)

		self._projectID = projectID

	def create(self, fields):
		super().create(fields)

		supports = {
			'name'      : True,
			'case_id'   : True,
			'version_id': True,
			'creator_id': False,
			'platform'  : False
		}

		if self.enforce(fields, supports):
			req = APIRequest(
				self._origin,
				'/v1/projects/' + str(self._projectID) + '/test-runs',
				'POST',
				{'params': fields}
			)

			return ProjectTestRun(self._origin, req.exec_())

	def all(self, filters=None):
		if filters is None:
			filters = {}

		super().all(filters)

		request = APIRequest(self._origin, '/v1/projects/' + str(self._projectID) + '/test-runs', 'GET')
		return EntityList(self._origin, request, ProjectTestRun, filters)

	def find(self, id_):
		super().find(id_)

		req = APIRequest(
			self._origin,
			'/v1/projects/' + str(self._projectID) + '/test-runs/' + str(id_),
			'GET'
		)
		return ProjectTestRun(self._origin, req.exec_())
