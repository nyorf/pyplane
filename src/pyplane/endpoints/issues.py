from .base import Base


class Issues(Base):
    __endpoint = 'issues'
    # TODO get rid of endpoints variable
    # TODO add functions that return groups, projects etc. in a list
    # TODO add pretty: bool to make output prettier
    
    def add_issue(
        self,
        workspace: str,
        project_id: str,
        name: str,
        state: str,
        assignees: list,
        labels: list,
        estimate_point: int = None,
        description_html: str = '', # Empty by default
        priority: str = "None",
        parent: str = None):
        payload = {
                "name": name,
                "description_html": description_html,
                "state": state,
                "assignees": assignees,
                "labels": labels,
                "estimate_point": estimate_point,
                "priority": priority,
                "parent": parent
            }
        return self.client.post(f'workspaces/{workspace}/projects/{project_id}/{self.__endpoint}/', payload=payload)
    
    def list_issues(
            self,
            workspace: str,
            project_id: str
            ):
        return self.client.get(f'workspaces/{workspace}/projects/{project_id}/{self.__endpoint}/')

    def get_issue_details(
            self,
            workspace: str,
            project_id: str,
            issue_id: str):
        return self.client.get(f'workspaces/{workspace}/projects/{project_id}/{self.__endpoint}/{issue_id}')

    def update_issue_name(
            self,
            workspace: str,
            project_id: str,
            issue_id: str,
            name: str):
        payload = {
            "name": name
        }
        return self.client.patch(f'workspaces/{workspace}/projects/{project_id}/{self.__endpoint}/{issue_id}', payload=payload)

    def update_issue_description(
            self,
            workspace: str,
            project_id: str,
            issue_id: str,
            description_html: str):
        payload = {
            "descritpion_html": description_html
        }
        return self.client.patch(f'workspaces/{workspace}/projects/{project_id}/{self.__endpoint}/{issue_id}', payload=payload)

    def update_issue_state(
            self,
            workspace: str,
            project_id: str,
            issue_id: str,
            state: str):
        payload = {
            "state": state
        }
        return self.client.patch(f'workspaces/{workspace}/projects/{project_id}/{self.__endpoint}/{issue_id}', payload=payload)

    def update_issue_assignees(
            self,
            workspace: str,
            project_id: str,
            issue_id: str,
            assignees: list):
        payload = {
            "assignees": assignees
        }
        return self.client.patch(f'workspaces/{workspace}/projects/{project_id}/{self.__endpoint}/{issue_id}', payload=payload)

    def update_issue_labels(
            self,
            workspace: str,
            project_id: str,
            issue_id: str,
            labels: list):
        payload = {
            "labels": labels
        }
        return self.client.patch(f'workspaces/{workspace}/projects/{project_id}/{self.__endpoint}/{issue_id}', payload=payload)

    def update_issue_estimate_point(
            self,
            workspace: str,
            project_id: str,
            issue_id: str,
            estimate_point: int):
        payload = {
            "estimate_point": estimate_point
        }
        return self.client.patch(f'workspaces/{workspace}/projects/{project_id}/{self.__endpoint}/{issue_id}', payload=payload)

    def update_issue_priority(
            self,
            workspace: str,
            project_id: str,
            issue_id: str,
            priority: str):
        payload = {
            "priority": priority
        }
        return self.client.patch(f'workspaces/{workspace}/projects/{project_id}/{self.__endpoint}/{issue_id}', payload=payload)

    def update_issue_parent(
            self,
            workspace: str,
            project_id: str,
            issue_id: str,
            parent: str):
        payload = {
            "parent": parent
        }
        return self.client.patch(f'workspaces/{workspace}/projects/{project_id}/{self.__endpoint}/{issue_id}', payload=payload)

    def delete_issue(
            self,
            workspace: str,
            project_id: str,
            issue_id: str):
        return self.client.delete(f'workspaces/{workspace}/projects/{project_id}/{self.__endpoint}/{issue_id}')
