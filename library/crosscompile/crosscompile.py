
# Created from dockerfile: /space/git/dockerfiles_repos/Dockerfiles/crosscompile/Dockerfile
from shutit_module import ShutItModule

class crosscompile(ShutItModule):

	def is_installed(self, shutit):
			return False

	def build(self, shutit):
		shutit.install('lsb-release')
		shutit.install('gcc')
		shutit.install('g++')
		shutit.install('mercurial')
		shutit.install('git-core')
		shutit.send('echo "deb http://archive.ubuntu.com/ubuntu $(lsb_release -s -c) main universe" > /etc/apt/sources.list')
		shutit.send('apt-get update')
		#shutit.send('apt-get upgrade -y')
		shutit.install('make build-essential')
		shutit.send('./all.bash')
		shutit.send('/bin/bash -c "git clone git://github.com/davecheney/golang-crosscompile.git && source golang-crosscompile/crosscompile.bash && go-crosscompile-build-all"')
		shutit.send('popd')
		shutit.send('popd')
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
		return crosscompile(
				'shutit.tk.crosscompile.crosscompile', 0.1241325,
				depends=['shutit.tk.setup','shutit.tk.go.go']
		)