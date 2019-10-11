# add the git information so that we can see what code produced the image
# this extra data will be available via docker inspect like:
# (docker inspect pythonactuary:latest | convertFrom-json).ContainerConfig.labels
$GIT_BRANCH=$(git name-rev --name-only HEAD)
$GIT_COMMIT=$(git rev-parse HEAD).substring(0,7)
$GIT_DIRTY=$false
$BUILD_CREATOR=$(git config user.email)
if ($(git status -s)) {
	$GIT_DIRTY = $true
}

docker build . -t pythonactuary:latest -t pythonactuary:"$GIT_Commit.Dirty.$GIT_DIRTY" --build-arg GIT_BRANCH="$GIT_BRANCH" `
  --build-arg GIT_COMMIT="$GIT_COMMIT" `
  --build-arg GIT_DIRTY="$GIT_DIRTY" `
  --build-arg BUILD_CREATOR="$BUILD_CREATOR"
