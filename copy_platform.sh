pushd $TI_ROOT/appc_web_docs/platform
git rm -rf latest
cp -r $TI_ROOT/doctools/dist/platform/latest .
git add latest
popd
