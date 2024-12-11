printf "\33[1;34mWELCOME TO EFTORY.PY INSTALLATION!!\r"

sleep 3
printf "Creating the environment for you......\t :)\r"

sleep 1
SCRIPT_DIR=$( cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )

if ! printf "python $SCRIPT_DIR/eftory.py \$1 \$2 \$3 \$4 \$5 \$6 \$7 \$8" > /usr/bin/eftory; then
    printf "There's something wrong when creating file in '/usr/bin' directory.. Did you run this with 'sudo'? If not please use it :)\n"
else
    if ! chmod +x /usr/bin/eftory; then
        printf "There's something wrong when doing 'chmod'.. Did you run this with 'sudo'? If not please use it :)\n"
    else
        sleep 1
        printf "\33[1;32mDONE! Yeahh, Just it! Easy right?....\t :)\n"
    fi
fi

