import subprocess

from copier_templates_extensions import ContextHook

def git_config(configkey):
    command = ['git', 'config', configkey]
    output = subprocess.check_output(command)
    return output.decode('utf-8').strip()

class ContextUpdater(ContextHook):
    def hook(self, context):
        values = {}

        # User Information
        values['git_user_name']= git_config('user.name')
        values['git_user_email'] = git_config('user.email')

        # Project Information
        values['project_name'] = context['name']
        if context['archetype'] == 'plugin':
            values['project_name'] = "dodo-{}".format(context['name'])
        values['github_repo'] = values['project_name']
        values['github_org'] = 'wabenet'
        values['github_url'] = "github.com/{}/{}".format(values['github_org'], values['github_repo'])

        # Components
        components = context['components'] + context['custom_components']

        ## Archetypes
        if context['archetype'] == 'tool':
            components += 'binary'
        if context['archetype'] == 'other':
            if context['archetype_other'] == 'plugin':
                components += 'binary'
                components += 'plugin'

        values['binary'] = 'binary' in components
        values['image'] = 'image' in components
        values['protobuf'] = 'protobuf' in components
        values['plugin'] = 'plugin' in components

        values['binary_name'] = values['project_name']
        values['image_name'] = "{}/{}".format(values['github_org'], values['github_repo'])

        return values
