# If you want to use Cisco plugin, you have to manage

* provider (identity.Provider)
* schema   (repository.Schema)

# Create provider

~~~
# Command
spacectl exec create identity.Provider -f provider.yaml
~~~

Example File: provider.yaml

~~~
provider: appdynamics
name: AppDynamics
template:
  service_account:
    schema:
      properties:
        name:
          minLength: 4.0
          title: Account Name
          type: string
      required:
      - name
      type: object
capability:
  supported_schema:
  - appdynamics_client_secret
tags:
  color: '#FF9900'
  external_link_template: https://accounts.appdynamics.com/overview
  icon: https://spaceone-custom-assets.s3.ap-northeast-2.amazonaws.com/console-assets/icons/appdynamics-icon.svg
metadata:
  view:
    layouts:
      help:service_account:create:
        name: Creation Help
        options:
          markdown:
            en: "# Help for AppDynamicsS Users\n## Find Your AppDynamics Account Name\nGet your AppDynamics Account ID.\n\
              [AppDynamics Account Name](https://accounts.appdynamics.com/overview)\n"
~~~

# Create schema

~~~
# Command
spacectl exec create repository.Schema -f schema.yaml
~~~

Example file: schema.yaml

~~~
name: appdynamics_client_secret
schema:
  properties:
    client_name:
      minLength: 4.0
      title: Client Name
      type: string
    account_name:
      minLength: 4.0
      title: Account Name
      type: string
    client_secret:
      minLength: 4.0
      title: Client Secret
      type: string
    controller:
      minLength: 6.0
      title: Controller URL
      type: string
  required:
  - client_name
  - account_name
  - client_secret
  - controller
service_type: secret.credentials
~~~
