variable "project_name" {
  type        = string
  description = "Resource naming prefix"
  default     = "northstar-rag"
}

variable "aws_region" {
  type        = string
  description = "AWS region"
  default     = "us-east-1"
}
