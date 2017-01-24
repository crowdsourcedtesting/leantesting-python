from BaseClass.EntityList       import EntityList
from BaseClass.EntityHandler    import EntityHandler
from BaseClass.APIRequest       import APIRequest

from Entity.Project.ProjectWebhook import ProjectWebhook

class ProjectWebhooksHandler(EntityHandler):

	_projectID = None

	def __init__(self, origin, projectID):
		super().__init__(origin)

		self._projectID = projectID

	def create(self, fields):
		super().create(fields)

		supports = {
			'url': True,
            'bug_create': False,
            'bug_create_severity_critical': False,
            'bug_create_severity_major': False,
            'bug_create_priority_critical': False,
            'bug_create_priority_high': False,
            'bug_edit': False,
            'bug_assign': False,
            'bug_assign_target': False,
            'bug_status_change': False,
            'bug_resolved': False,
            'bug_move': False,
            'bug_delete': False,
            'comment_create': False,
            'comment_edit': False,
            'message_create': False,
            'message_edit': False,
            'attachment_create': False,
            'run_start': False,
            'run_finish': False,
		}

		if self.enforce(fields, supports):
			req = APIRequest(
				self._origin,
				'/v1/projects/' + str(self._projectID) + '/integrations/webhooks',
				'POST',
				{'params': fields}
			)

			return ProjectWebhook(self._origin, req.exec_())

	def all(self, filters = None):
		if filters is None:
			filters = {}

		super().all(filters)

		request = APIRequest(self._origin, '/v1/projects/' + str(self._projectID) + '/integrations/webhooks', 'GET')
		return EntityList(self._origin, request, ProjectWebhook, filters)

	def delete(self, id_):
		super().delete(id_)

		req = APIRequest(
			self._origin,
			'/v1/projects/' + str(self._projectID) + '/integrations/webhooks/' + str(id_),
			'DELETE'
		)
		return req.exec_()

	def find(self, id_):
		super().find(id_)

		req = APIRequest(
			self._origin,
			'/v1/projects/' + str(self._projectID) + '/integrations/webhooks/' + str(id_),
			'GET'
		)
		return ProjectWebhook(self._origin, req.exec_())