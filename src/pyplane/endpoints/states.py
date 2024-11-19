from .base import Base


class States(Base):
    __endpoint = 'states'
    # TODO get rid of endpoints variable
    # TODO add functions that return groups, projects etc. in a list
    # TODO add pretty: bool to make output prettier
    
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
        return self.client.post(f'workspaces/{workspace}/projects/{project_id}/{self.__endpoint}/', payload=payload)
    
    def list_project_states(
            self,
            workspace: str,
            project_id: str
            ):
        return self.client.get(f'workspaces/{workspace}/projects/{project_id}/{self.__endpoint}/')

    def get_state_details(
            self,
            workspace: str,
            project_id: str,
            state_id: str):
        return self.client.get(f'workspaces/{workspace}/projects/{project_id}/{self.__endpoint}/{state_id}')

    def update_state_name(
            self,
            workspace: str,
            project_id: str,
            state_id: str,
            name: str):
        payload = {
            "name": name
        }
        return self.client.patch(f'workspaces/{workspace}/projects/{project_id}/{self.__endpoint}/{state_id}', payload=payload)

    def update_state_description(
            self,
            workspace: str,
            project_id: str,
            state_id: str,
            description: str):
        payload = {
            "descritpion": description
        }
        return self.client.patch(f'workspaces/{workspace}/projects/{project_id}/{self.__endpoint}/{state_id}', payload=payload)

    def update_state_color(
            self,
            workspace: str,
            project_id: str,
            state_id: str,
            hex: str):
        payload = {
            "color": hex
        }
        return self.client.patch(f'workspaces/{workspace}/projects/{project_id}/{self.__endpoint}/{state_id}', payload=payload)

    def update_state_group(
            self,
            workspace: str,
            project_id: str,
            state_id: str,
            group: str):
        payload = {
            "group": group
        }
        return self.client.patch(f'workspaces/{workspace}/projects/{project_id}/{self.__endpoint}/{state_id}', payload=payload)
    
    def update_state_isdefault(
            self,
            workspace: str,
            project_id: str,
            state_id: str,
            isdefault: bool):
        payload = {
            "default": isdefault
        }
        return self.client.patch(f'workspaces/{workspace}/projects/{project_id}/{self.__endpoint}/{state_id}', payload=payload)
    
    def delete_state(
            self,
            workspace: str,
            project_id: str,
            state_id: str):
        return self.client.delete(f'workspaces/{workspace}/projects/{project_id}/{self.__endpoint}/{state_id}')
