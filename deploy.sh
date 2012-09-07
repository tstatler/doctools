DEBUG_TEMPLATE=template
PROD_TEMPLATE=template-min
VIDEO_LIST="videos.json"
PROCESSED_VIDEO_LIST="build/videos.json"

progname=$0

usage() {
    echo "Usage: $progname [options] [debug|prod]"
    echo ""
    echo "  Options:"
    echo "  -o <optional_project> (currently, only alloy is supported)"
    echo "  -t  Do not generate video thumbnails"
    echo ""
}

while getopts ":to:" opt; do
    case $opt in 
        o)
            if [ $OPTARG == "alloy" ]; then
                include_alloy="include_alloy"
            else
                echo "Unknown optional project, $OPTARG">&2
                usage
                exit 1
            fi
            ;;
        t)  
            no_thumbnails="no_thumbnails"
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
    elif [ $1 == "debug" ]; then
        debug_build="debug"
    fi
    shift
done

if [ ! "$TI_DOCS" ]; then
    if [ "$TI_ROOT" ]; then
        TI_DOCS=${TI_ROOT}/titanium_mobile/apidoc
    else
        echo "No doc root \$TI_DOCS and \$TI_ROOT not defined. Exiting."
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

if [ ! "$ALLOY" ]; then
    if [ "$TI_ROOT" ]; then
        ALLOY=${TI_ROOT}/alloy
    else
        echo "No alloy dir \$ALLOY and \$TI_ROOT not defined. Exiting."
        exit
    fi
fi

if [ $include_alloy ]; then
    alloyDirs="${ALLOY}/alloy/builtins ${ALLOY}/alloy/lib"
fi

python ${TI_DOCS}/docgen.py -f jsduck -o ./build
python ./guides_parser.py --input "./htmlguides/toc.xml" --output "./build/guides"

if [ $no_thumbnails ]; then
    cp $VIDEO_LIST $PROCESSED_VIDEO_LIST
else
    python ./video_thumbs.py --input $VIDEO_LIST --output $PROCESSED_VIDEO_LIST
fi

if [ $production_build ] ; then
    (cd ${JSDUCK}; rake compress)
    TEMPLATE=${JSDUCK}/${PROD_TEMPLATE}
else
    compass compile ${JSDUCK}/template/resources/sass
    TEMPLATE=${JSDUCK}/${DEBUG_TEMPLATE}
fi
ruby ${JSDUCK}/bin/jsduck --template ${TEMPLATE} --config ./jsduck.config $alloyDirs
cp -r "./htmlguides/images" "dist/images"
cp -r "./htmlguides/attachments" "dist/attachments"
cp -r "./htmlguides/css/common.css" "dist/resources/css/common.css"
cp ./resources/mock_video.png dist/resources/images/mock_video.png
cp ./resources/codestrong_logo_short.png dist/resources/images/codestrong_logo_short.png
