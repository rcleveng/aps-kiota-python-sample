import asyncio
from kiota_http.httpx_request_adapter import HttpxRequestAdapter
from aps import DataManagementClient, IssuesClient, BearerTokenAuthenticationProvider

# Assuming APS_ACCESS_TOKEN is set in environment variables
adapter = HttpxRequestAdapter(BearerTokenAuthenticationProvider())
data_management_client = DataManagementClient(adapter)
issues_client = IssuesClient(adapter)

async def get_hubs():
    try:
        response = await data_management_client.project.v1.hubs.get()
        return response.data if response and response.data else []
    except Exception as e:
        print(f"Error fetching hubs: {e}")
        return []

async def get_projects(hub_id: str):
    try:
        response = await data_management_client.project.v1.hubs.by_hub_id(hub_id).projects.get()
        return response.data if response and response.data else []
    except Exception as e:
        print(f"Error fetching projects for hub {hub_id}: {e}")
        return []

async def get_top_folders(hub_id: str, project_id: str):
    try:
        response = await data_management_client.project.v1.hubs.by_hub_id(hub_id).projects.by_project_id(project_id).top_folders.get()
        return response.data if response and response.data else []
    except Exception as e:
        print(f"Error fetching top folders for project {project_id}: {e}")
        return []

async def get_issues(project_id: str):
    try:
        response = await issues_client.construction.issues.v1.projects.by_project_id(project_id).issues.get()
        return response.results if response and response.results else []
    except Exception as e:
        print(f"Error fetching issues for project {project_id}: {e}")
        return []

async def main():
    hubs = await get_hubs()
    for hub in hubs:
        assert hub.id and hub.attributes
        print(f"Hub: {hub.attributes.name} ({hub.id})")
        projects = await get_projects(hub.id)
        for project in projects:
            assert project.id and project.attributes
            print(f"  Project: {project.attributes.name} ({project.id})")
            top_folders = await get_top_folders(hub.id, project.id)
            for folder in top_folders:
                assert folder.id and folder.attributes
                print(f"    Folder: {folder.attributes.display_name} ({folder.id})")
            if project.id.startswith("b."): # Only get issues for ACC projects
                issues = await get_issues(project.id.replace("b.", ""))
                for issue in issues:
                    print(f"    Issue: {issue.title} ({issue.id})")

asyncio.run(main())