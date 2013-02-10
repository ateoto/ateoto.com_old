import os
from fabric.api import run, cd, env, put, prefix, sudo
from fabric.contrib import files

env.deploy_dir = '/home/ubuntu/ateoto.com'
env.default_deploy_ref = 'origin/master'
env.virtualenv = 'ateoto.com'

def deploy():
    update_code()
    install_requirements()
    collect_static()
    apache('reload')    

def update_code(ref = None):
    ref = ref or env.default_deploy_ref

    with cd(env.deploy_dir):
        run('git pull')
        put('ateoto/settings/secrets.json', 'ateoto/settings/secrets.json')
    
def install_requirements():
    with cd(env.deploy_dir):
        with prefix('workon %s' % (env.virtualenv)):
            run('pip install -r requirements.txt')
            run('python manage.py migrate --settings=ateoto.settings')
            run('python manage.py syncdb --settings=ateoto.settings')

def collect_static(clear = False):
    clear_cmd = ''
    if clear: clear_cmd = '--clear'
    with cd(env.deploy_dir):
        with prefix('workon %s' % (env.virtualenv)):
            run('python manage.py collectstatic --noinput %s --settings=ateoto.settings' % (clear_cmd))

def apache(cmd):
    sudo('invoke-rc.d apache2 %s' % cmd)

