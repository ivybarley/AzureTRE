from fastapi import Depends, HTTPException, Path
from starlette.status import HTTP_404_NOT_FOUND

from api.dependencies.database import get_repository
from db.errors import EntityDoesNotExist
from db.repositories.resource_templates import ResourceTemplateRepository
from models.domain.resource import ResourceType
from models.domain.resource_template import ResourceTemplate
from resources import strings


async def get_workspace_service_template_by_name_from_path(service_template_name: str = Path(...), template_repo=Depends(get_repository(ResourceTemplateRepository))) -> ResourceTemplate:
    try:
        return template_repo.get_current_template(service_template_name, ResourceType.WorkspaceService)
    except EntityDoesNotExist:
        raise HTTPException(status_code=HTTP_404_NOT_FOUND, detail=strings.TEMPLATE_DOES_NOT_EXIST)
