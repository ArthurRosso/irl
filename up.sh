
export ROOT=/home/arthur/ensimag/irl/MIA
export ARCHS=$ROOT/archs
export PROFILES=$ROOT/examples/profiles

$ROOT/bin/rtAnalyser -arch /home/arthur/ensimag/irl/irl/archs/base-RR.arch \
                     -profiles /home/arthur/ensimag/irl/irl/profiles \
                     -ts /home/arthur/ensimag/irl/irl/input1.yaml \
                     -o /home/arthur/ensimag/irl/irl/result.yaml