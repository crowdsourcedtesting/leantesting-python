from BaseClass.Entity import Entity
from Handler.Project.ProjectTestCasesHandler import ProjectTestCasesHandler

class ProjectSection(Entity):

	tests = None

	def __init__(self, origin, data):
		super().__init__(origin, data)

		self.tests = ProjectTestCasesHandler(origin, data['id'])
