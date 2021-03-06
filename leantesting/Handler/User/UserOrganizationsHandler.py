from BaseClass.EntityList       import EntityList
from BaseClass.EntityHandler    import EntityHandler
from BaseClass.APIRequest       import APIRequest

from Entity.User.UserOrganization import UserOrganization

class UserOrganizationsHandler(EntityHandler):

	def all(self, filters = None):
		if filters is None:
			filters = {}

		super().all(filters)

		request = APIRequest(self._origin, '/v1/me/organizations', 'GET')
		return EntityList(self._origin, request, UserOrganization, filters)

	def find(self, id_):
		super().find(id_)

		req = APIRequest(self._origin, '/v1/me/organizations/' + str(id_), 'GET')
		return UserOrganization(self._origin, req.exec_())
