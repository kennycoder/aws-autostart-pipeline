BUCKET_NAME ?= cf-templates-bucket-nikolai

configure:
	@ aws s3api head-bucket --bucket "$(BUCKET_NAME)" || aws s3 mb "s3://$(BUCKET_NAME)"
	@ aws s3api put-bucket-versioning --bucket "$(BUCKET_NAME)"  --versioning-configuration Status=Enabled

deploy:
	@ aws s3 cp infrastructure.yaml "s3://$(BUCKET_NAME)"
	@ aws s3 cp --recursive templates/ "s3://$(BUCKET_NAME)/templates"

clean:
	@ aws s3 rm "s3://$(BUCKET_NAME)/templates" --recursive
	@ aws s3 rm "s3://$(BUCKET_NAME)/infrastructure.yaml"

.PHONY: clean install build build-lambda configure package deploy describe output
