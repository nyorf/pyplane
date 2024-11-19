from .base import Base


class Comments(Base):
    __endpoint = 'comments'
    # TODO get rid of endpoints variable
    # TODO add functions that return groups, projects etc. in a list
    # TODO add pretty: bool to make output prettier
    
    def add_comment(
        self,
        workspace: str,
        project_id: str,
        issue_id: str,
        comment_html: str,
        access: str = "INTERNAL"): # internal access only by default
        payload = {
                "comment_html": comment_html,
                "access": access,
            }
        return self.client.post(f'workspaces/{workspace}/projects/{project_id}/issues/{issue_id}/{self.__endpoint}/', payload=payload)
