if [ ! "$1" ] ; then
    echo "Usage: $0 <commit message>"
    exit
fi
cd $TI_ROOT/appc_web_docs
git checkout 3.1_docs
git pull appcelerator master
rm -rf $TI_ROOT/appc_web_docs/titanium/3.0
cp -r $TI_ROOT/doctools/dist/titanium/3.0 $TI_ROOT/appc_web_docs/titanium/3.0
git add titanium/3.0
git commit -m "$1"
git push origin 3.1_docs
