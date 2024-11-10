from .base import Base


class Projects(Base):
    endpoint = 'projects/'

    def add_project(
            self,
            workspace: str,
            name: str,
            identifier: str,
            description: str = ""
            ):
        payload = {
                    "name": name,
                    "identifier": identifier,
                    "description": description
                }
        return self.client.post(f'workspaces/{workspace}/' + self.endpoint, payload=payload)

    def list_projects(self, workspace):
        return self.client.get(f'workspaces/{workspace}/' + self.endpoint)
