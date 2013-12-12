## upstream project
UPSTREAM=upstream
## repo branches
TI_BRANCH=3_2_X
ALLOY_BRANCH=1_3_X

if [ ! "$TI_ROOT" ]; then
    echo "\$TI_ROOT not defined. Exiting."
    exit 1
fi

TI_DIR=$TI_ROOT/titanium_mobile
ALLOY_DIR=$TI_ROOT/alloy
MOD_DIR=$TI_ROOT/titanium_modules
MAP_DIR=$TI_ROOT/appc_modules/ti.map
NFC_DIR=$TI_ROOT/appc_modules/ti.nfc
NEWSSTAND_DIR=$TI_ROOT/appc_modules/ti.newsstand
TIZEN_DIR=$TI_ROOT/titanium_mobile_tizen


if [ -d $TI_DIR ]; then
    echo "Attempting to update the titanium_mobile repo on $UPSTREAM/$TI_BRANCH..."
    cd $TI_DIR
    git checkout $TI_BRANCH
    git pull $UPSTREAM $TI_BRANCH
else
    echo "Warning: Cannot locate the titanium_mobile repo at $TI_DIR"
fi

if [ -d $ALLOY_DIR ]; then
    echo "Attempting to update the alloy repo on $UPSTREAM/$ALLOY_BRANCH..."
    cd $ALLOY_DIR
    git checkout $ALLOY_BRANCH
    git pull $UPSTREAM $ALLOY_BRANCH
else
    echo "Warning: Cannot locate the alloy repo at $ALLOY_DIR"
fi

if [ -d $MOD_DIR ]; then
    echo "Attempting to update the titanium_modules repo on origin/master..."
    cd $MOD_DIR
    git checkout master
    git pull origin master
else
    echo "Warning: Cannot locate the titanium_modules repo at $MOD_DIR"
fi

if [ -d $MAP_DIR ]; then
    echo "Attempting to update the ti.map repo on origin/master..."
    cd $MAP_DIR
    git checkout master
    git pull origin master
else
    echo "Warning: Cannot locate the ti.map repo at $MAP_DIR"
fi

if [ -d $NFC_DIR ]; then
    echo "Attempting to update the ti.nfc repo on origin/master..."
    cd $NFC_DIR
    git checkout master
    git pull origin master
else
    echo "Warning: Cannot locate the ti.nfc repo at $NFC_DIR"
fi

if [ -d $NEWSSTAND_DIR ]; then
    echo "Attempting to update the ti.newsstand repo on origin/master..."
    cd $NEWSSTAND_DIR
    git checkout master
    git pull origin master
else
    echo "Warning: Cannot locate the ti.newsstand repo at $NEWSSTAND_DIR"
fi

if [ -d $TIZEN_DIR ]; then
    echo "Attempting to update the titanium_mobile_tizen repo on origin/$TI_BRANCH..."
    cd $TIZEN_DIR
    git checkout $TI_BRANCH
    git pull origin $TI_BRANCH
else
    echo "Warning: Cannot locate the titanium_mobile_tizen repo at $TIZEN_DIR"
fi

echo "Repo updates completed"
