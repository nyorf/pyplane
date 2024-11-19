from .base import Base


class Activities(Base):
    __endpoint = 'activities'
    # TODO get rid of endpoints variable
    # TODO add functions that return groups, projects etc. in a list
    # TODO add pretty: bool to make output prettier
    
    def list_issue_activity(
            self,
            workspace: str,
            project_id: str,
            issue_id: str
            ):
        return self.client.get(f'workspaces/{workspace}/projects/{project_id}/issues/{issue_id}/{self.__endpoint}/')

    def list_issue_activity_details(
            self,
            workspace: str,
            project_id: str,
            issue_id: str,
            activity_id: str
            ):
        return self.client.get(f'workspaces/{workspace}/projects/{project_id}/issues/{issue_id}/{self.__endpoint}/{activity_id}')
