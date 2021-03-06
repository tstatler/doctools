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


## $1 - repo name
## $2 - repo dir
## $3 - repo remote name / upstream project
## $4 - repo branch
function repo_update {
    if [ -d $2 ]; then
        echo "Attempting to update the $1 repo on $3/$4..."
        cd $2
        git checkout $4
        git pull $3 $4
    else
        echo "Warning: Cannot locate the $1 repo at $2"
    fi
}

repo_update titanium_mobile $TI_DIR upstream 3_2_X
repo_update alloy $ALLOY_DIR upstream 1_3_X
repo_update titanium_modules $MOD_DIR origin master
repo_update ti.map $MAP_DIR origin master
repo_update ti.nfc $NFC_DIR origin master
repo_update ti.newsstand $NEWSSTAND_DIR origin master
repo_update titanium_mobile_tizen $TIZEN_DIR origin 3_2_X

echo "Repo updates completed"
