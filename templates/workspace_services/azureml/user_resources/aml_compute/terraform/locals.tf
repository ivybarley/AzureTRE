# Random unique id

locals {

  short_user_resource_id         = substr(var.tre_resource_id, -4, -1)
  short_service_id               = substr(var.parent_service_id, -4, -1)
  short_workspace_id             = substr(var.workspace_id, -4, -1)
  core_resource_group_name       = "rg-${var.tre_id}"
  workspace_resource_name_suffix = "${var.tre_id}-ws-${local.short_workspace_id}"
  service_resource_name_suffix   = "${var.tre_id}-ws-${local.short_workspace_id}-svc-${local.short_service_id}"
  user_resource_name_suffix      = "${local.service_resource_name_suffix}-${local.short_user_resource_id}"
  aml_workspace_name             = lower("ml-${substr(local.service_resource_name_suffix, -30, -1)}")
  aml_compute_id                 = "${local.short_service_id}${local.short_user_resource_id}"
  aml_compute_instance_name      = "ci-${local.aml_compute_id}"
}
