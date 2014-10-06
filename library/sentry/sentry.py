
# Created from dockerfile: /space/git/dockerfiles_repos/Dockerfiles/sentry/Dockerfile
from shutit_module import ShutItModule

class sentry(ShutItModule):

	def is_installed(self, shutit):
		return False

	def build(self, shutit):
		shutit.install('lsb-release')
		shutit.send('echo "deb http://archive.ubuntu.com/ubuntu $(lsb_release -c -s) main universe" > /etc/apt/sources.list')
		shutit.send('apt-get update')
		shutit.send('apt-get upgrade -y')
		shutit.install('language-pack-en')
		# locale
		shutit.send('export LANGUAGE=en_US.UTF-8')
		shutit.send('export LANG=en_US.UTF-8')
		shutit.send('export LC_ALL=en_US.UTF-8')
		shutit.send('locale-gen en_US.UTF-8')
		shutit.send('dpkg-reconfigure locales')
		shutit.install('openssh-server')
		shutit.install('git-core')
		shutit.install('libxml2-dev')
		shutit.install('curl')
		shutit.install('python')
		shutit.install('build-essential')
		shutit.install('gcc')
		shutit.install('python-dev')
		shutit.install('wget')
		shutit.install('postgresql-client')
		shutit.install('postgresql-client-common')
		shutit.install('libpq5')
		# broken in 14.04
		#shutit.install('libpq-dev')
		shutit.send('wget http://python-distribute.org/distribute_setup.py')
		shutit.send('python distribute_setup.py')
		shutit.send('wget https://raw.github.com/pypa/pip/master/contrib/get-pip.py')
		shutit.send('python get-pip.py')
		shutit.send('pip install psycopg2')
		shutit.send('pip install sentry')
		shutit.send_host_file('/sentry.conf.py', 'context/sentry.conf.py')
		return True

	def finalize(self, shutit):
		return True

	def test(self, shutit):
		return True

	def is_installed(self, shutit):
		return False

	def get_config(self, shutit):
		return True

def module():
		return sentry(
				'shutit.tk.sentry.sentry', 0.121353315,
				depends=['shutit.tk.setup']
		)