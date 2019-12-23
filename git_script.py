import subprocess
import datetime
subprocess.call(['git', 'init'])
subprocess.call(['git', 'add', '-A'])
commit_tag = input('Enter this commit tag: ')
if commit_tag == '':
    commit_tag = str(datetime.datetime.now())
subprocess.call(['git', 'pull'])
subprocess.call(['git', 'commit', '-m', str(commit_tag)])
subprocess.call(
    ['git', 'push', 'https://github.com/huyong007/post_to_kindle.git', 'master'])
