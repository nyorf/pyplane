from .base import Base


class Labels(Base):
    __endpoint = 'labels'
    # TODO get rid of endpoints variable
    # TODO add functions that return groups, projects etc. in a list
    # TODO add pretty: bool to make output prettier
    
    def add_project_label(
        self,
        workspace: str,
        project_id: str,
        name: str,
        description: str = '', # Empty by default
        color: str = '',  # no color by default
        parent: str = None):
        payload = {
                "name": name,
                "description": description,
                "color": color,
                "parent": parent
            }
        return self.client.post(f'workspaces/{workspace}/projects/{project_id}/{self.__endpoint}/', payload=payload)
    
    def list_project_labels(
            self,
            workspace: str,
            project_id: str
            ):
        return self.client.get(f'workspaces/{workspace}/projects/{project_id}/{self.__endpoint}/')

    def get_label_details(
            self,
            workspace: str,
            project_id: str,
            label_id: str):
        return self.client.get(f'workspaces/{workspace}/projects/{project_id}/{self.__endpoint}/{label_id}')

    def update_label_name(
            self,
            workspace: str,
            project_id: str,
            label_id: str,
            name: str):
        payload = {
            "name": name
        }
        return self.client.patch(f'workspaces/{workspace}/projects/{project_id}/{self.__endpoint}/{label_id}', payload=payload)

    def update_label_description(
            self,
            workspace: str,
            project_id: str,
            label_id: str,
            description: str):
        payload = {
            "descritpion": description
        }
        return self.client.patch(f'workspaces/{workspace}/projects/{project_id}/{self.__endpoint}/{label_id}', payload=payload)

    def update_label_color(
            self,
            workspace: str,
            project_id: str,
            label_id: str,
            hex: str):
        payload = {
            "color": hex
        }
        return self.client.patch(f'workspaces/{workspace}/projects/{project_id}/{self.__endpoint}/{label_id}', payload=payload)
    
    def delete_label(
            self,
            workspace: str,
            project_id: str,
            label_id: str):
        return self.client.delete(f'workspaces/{workspace}/projects/{project_id}/{self.__endpoint}/{label_id}')
