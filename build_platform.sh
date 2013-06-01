fail_on_error() {
    if [ $# -ne 2 ] ; then
        echo "Wrong number of arguments."
        exit 1
    fi
    if [ $1 -ne 0 ] ; then
        echo "Error: " $2
        exit 1
    fi
}

outdir=$TI_ROOT/doctools/dist/platform/latest

cd $TI_ROOT/titanium_mobile 
git checkout 3_1_X 
fail_on_error $? "Could not checkout titanium branch."
git pull appcelerator 3_1_X
fail_on_error $? "Pull failed on titanium branch."
cd $TI_ROOT/alloy
git checkout 1_1_X
fail_on_error $? "Could not checkout alloy branch."
git pull appcelerator 1_1_X
fail_on_error $? "Pull failed on alloy branch."
cd $TI_ROOT/doctools
rm -rf $outdir
sh deploy.sh -o alloy -o modules -g htmlguides-latest -a guides-enterprise -d $outdir -t "Appcelerator Platform - Appcelerator Docs" prod
fail_on_error $? "Deploy failed."
rm -rf ~/Sites/platform/latest
rm -rf ~/Sites/platform/landing/index.html
cp -rf $outdir ~/Sites/platform/latest
cp $TI_ROOT/appc_web_docs/titanium/landing/index.html ~/Sites/platform/landing/index.html
