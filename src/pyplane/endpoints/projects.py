from .base import Base


class Projects(Base):
    endpoint = 'projects/'
    # TODO get rid of endpoints variable
    # TODO add functions that return groups, projects etc. in a list
    # TODO add pretty: bool to make output prettier
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

    def list_projects(
            self, 
            workspace: str):
        return self.client.get(f'workspaces/{workspace}/' + self.endpoint)
    
    def get_project_details(
            self,
            workspace: str,
            project_id: str):
        return self.client.get(f'workspaces/{workspace}/' + self.endpoint + f'{project_id}/')

    def update_project_name(
            self,
            workspace: str,
            project_id: str,
            name: str):
        payload = {
            "name": name
        }
        return self.client.patch(f'workspaces/{workspace}/' + self.endpoint + f'{project_id}/', payload=payload)

    def update_project_identifier(
            self,
            workspace: str,
            project_id: str,
            identifier: str):
        payload = {
            "identifier": identifier
        }
        return self.client.patch(f'workspaces/{workspace}/' + self.endpoint + f'{project_id}/', payload=payload)

    def update_project_description(
            self,
            workspace: str,
            project_id: str,
            description: str):
        payload = {
            "description": description
        }
        return self.client.patch(f'workspaces/{workspace}/' + self.endpoint + f'{project_id}/', payload=payload)

    def add_project_state(
            self,
            workspace: str,
            project_id: str,
            name: str,
            group: str,
            description: str = '', # Empty by default
            color: str = '#4478f9',  # Plane brand main color
            default: bool = False):
        payload = {
                "name": name,
                "description": description,
                "color": color,
                "group": group,
                "default": default
            }
        return self.client.post(f'workspaces/{workspace}/' + self.endpoint + f'{project_id}/states/', payload=payload)
    
    def list_project_states(
            self,
            workspace: str,
            project_id: str
            ):
        return self.client.get(f'workspaces/{workspace}/' + self.endpoint + f'{project_id}/states/')
