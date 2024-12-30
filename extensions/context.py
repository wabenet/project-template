import subprocess

from copier_templates_extensions import ContextHook

def git_config(configkey):
    command = ['git', 'config', configkey]
    output = subprocess.check_output(command)
    return output.decode('utf-8').strip()

class ContextUpdater(ContextHook):
    def hook(self, context):
        git_name = git_config('user.name')
        git_email = git_config('user.email')

        name = context['name']
        flavour = context['flavour']

        project_name = "dodo-{}".format(name) if flavour == 'plugin' else name
        github_repo = project_name
        github_org = 'wabenet'

        return {
            'git_user_name': git_name,
            'git_user_email': git_email,
            'project_name': project_name,
            'github_repo': github_repo,
            'github_org': github_org,
            'github_url': "github.com/{}/{}".format(github_org, github_repo),
            'has_binary': flavour in {'tool', 'plugin'},
            'is_plugin': flavour == 'plugin',
            'binary_name': project_name,
        }

