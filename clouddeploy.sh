DEBUG_TEMPLATE=template
PROD_TEMPLATE=template-min
VIDEO_LIST="videos.json"
PROCESSED_VIDEO_LIST="build/videos.json"
config="./jsduck.config"

progname=$0

usage() {
    echo "Usage: $progname [options] [debug|prod]"
    echo ""
    echo "  Options:"
    echo "  -c <config_file> (i.e., jsduck_21.config for 2.1 docs build)."
    echo "  -s  Enable --seo flag to jsduck."
    echo ""
}

while getopts ":tso:c:g:" opt; do
    case $opt in 
        c)
            if [ "$OPTARG" ]; then
                config=$OPTARG
            fi
            ;;
        s)  
            seo="--seo"
            ;;
        \?) 
             echo "Invalid option: -$OPTARG">&2
             usage
             exit 1
             ;;
        :)
             echo "Option -$OPTARG requires an argument." >&2
             usage
             exit 1
             ;;
    esac
done

# Skip the options and move on to the positional parameters
shift $((OPTIND-1))


while [ $1 ]; do
    if [ $1 == "prod" ]; then
        production_build="production"
        seo="--seo"
        no_thumbnails=""
    elif [ $1 == "debug" ]; then
        debug_build="debug"
    fi
    shift
done
#
if [ ! "$CLOUD_DOCS" ]; then
    if [ "$TI_ROOT" ]; then
        CLOUD_DOCS=${TI_ROOT}/cloud_docs
    else
        echo "No doc root \$CLOUD_DOCS and \$TI_ROOT not defined. Exiting."
        exit
    fi
fi
if [ ! "$JSDUCK" ]; then
    if [ "$TI_ROOT" ]; then
        JSDUCK=${TI_ROOT}/jsduck
    else
        echo "No JSDuck dir \$JSDUCK and \$TI_ROOT not defined. Exiting."
        exit
    fi
fi

if [ ! "$DOCTOOLS" ]; then
    if [ "$TI_ROOT" ]; then
        DOCTOOLS=${TI_ROOT}/doctools
    else
        echo "No doctools dir \$DOCTOOLS and \$TI_ROOT not defined. Exiting."
        exit
    fi
fi

if [ $production_build ] ; then
    (cd ${JSDUCK}; rake compress)
    TEMPLATE=${JSDUCK}/${PROD_TEMPLATE}
else
    compass compile ${JSDUCK}/template/resources/sass
    TEMPLATE=${JSDUCK}/${DEBUG_TEMPLATE}
fi
ruby ${JSDUCK}/bin/jsduck --template ${TEMPLATE} $seo --config jsduck_cloud.config
