from BaseClass.EntityList       import EntityList
from BaseClass.EntityHandler    import EntityHandler
from BaseClass.APIRequest       import APIRequest

from Entity.Project.ProjectUser import ProjectUser

class ProjectUsersHandler(EntityHandler):

	_projectID = None

	def __init__(self, origin, projectID):
		super().__init__(origin)

		self._projectID = projectID

	def create(self, fields):
		super().create(fields)

		supports = {
			'email': True,
			'role_slug': True
		}

		if self.enforce(fields, supports):
			req = APIRequest(
				self._origin,
				'/v1/projects/' + str(self._projectID) + '/users',
				'POST',
				{'params': fields}
			)

			return ProjectUser(self._origin, req.exec_())

	def delete(self, id_):
		super().delete(id_)

		req = APIRequest(
			self._origin,
			'/v1/projects/' + str(self._projectID) + '/users/' + str(id_),
			'DELETE'
		)
		return req.exec_()

	def all(self, filters = None):
		if filters is None:
			filters = {}

		super().all(filters)

		request = APIRequest(self._origin, '/v1/projects/' + str(self._projectID) + '/users', 'GET')
		return EntityList(self._origin, request, ProjectUser, filters)
