
set -x
brew install freetype imagemagick@6 ghostscript
export MAGICK_HOME=/usr/local/opt/imagemagick@6

## installing PYENV

curl -L https://raw.githubusercontent.com/pyenv/pyenv-installer/master/bin/pyenv-installer | bash
echo 'eval "$(pyenv init -)"' >> ~/.bash_profile
echo 'eval "$(pyenv virtualenv-init -)"' >> ~/.bash_profile

source ~/.bash_profile

pyenv update
pyenv install 2.7.13

pyenv virtualenv 2.7.13 pdflibspy-2.7.13
pyenv activate pdflibspy-2.7.13
pip install -r ./requirements.txt
