pushd $TI_ROOT/appc_web_docs/cloud
git rm -rf latest
cp -r $TI_ROOT/doctools/dist/cloud/latest .
git add latest
pushd data/solr
cp $TI_ROOT/doctools/dist/cloud/data/solr/* .
popd
popd
