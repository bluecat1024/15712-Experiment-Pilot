remote_url="git@github.com:Arceus48/15712-Project.git"
version=$1

git clone --branch $version $remote_url
mv 15712-Project $version
cd $version
./configure
make