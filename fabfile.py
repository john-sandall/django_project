from __future__ import with_statement
from fabric.api import local, settings, abort, run, cd, lcd
from fabric.contrib.console import confirm

def prepare_deployment(branch_name):
	local('python manage.py test django_project')
	local('git add -p && git commit')
	
def deploy():
	code_dir = '/var/www/vhosts/dev/django_project/'
	with cd(code_dir):
		
		run('git pull')
		run('python manage.py migrate myapp')
		run('python manage.py test myapp')
		run('/etc/init.d/httpd restart')