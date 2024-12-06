import subprocess

from copier_templates_extensions import ContextHook

def git_config(configkey):
    command = ['git', 'config', configkey]
    output = subprocess.check_output(command)
    return output.decode('utf-8').strip()

class ContextUpdater(ContextHook):
    def hook(self, context):
        name = git_config('user.name')
        email = git_config('user.email')
        return {
            "git_user_name": name,
            "git_user_email": email,
        }

