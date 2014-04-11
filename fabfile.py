from fabric.api import *

"""
these functions won't work if you haven't got the outsideline.pem certificate. you can
get it from the amazon aws console. login details are in the hosting doc.
"""

def live():
	"""Set the target to production."""
	env.hosts=['maracuja@setr.co.uk']
	env.remote_app_dir='~/python/setr-co-uk/'


def yeah():
	print "thafe, yeah?"
	
	
def push():
	"""Pushes the code to nominated server - restart included - doesn't touch the db"""
	require('hosts', provided_by=[live,])
	run("cd %s; hg identify" % env.remote_app_dir)
	run("cd %s; hg pull -u" % env.remote_app_dir)

	
def restartserver():
	"""Restarts the nominated server services, apache, memcached and mysql"""
	require('hosts', provided_by=[live,])
	sudo("service mysql restart")
	sudo("/etc/init.d/apache2 restart")


def restartapache():
	"""Restarts the nominated server services, memcached and apache"""
	require('hosts', provided_by=[live,])
	sudo("/etc/init.d/apache2 restart")


def installdb():
	"""This will install the latest db dump into your local mysql"""
	run("mysql -u personal -pallaboutme setr_blog < ~/python/setr-co-uk/database/install.sql")


def localdb():
	"""Installs the latest.sql onto totoro"""
	local("mysql -u root -proot setr_blog < ~/python/setr-co-uk/database/install.sql")


def localstatic():
	local('python manage.py collectstatic')


def updatedb():
	# run update.sql
	pass
	
	
def startlocal():
    local('python manage.py runserver 0.0.0.0:1234')

