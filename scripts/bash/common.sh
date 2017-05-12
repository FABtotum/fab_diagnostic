TEST_CASE_NAME=$(basename $0 | awk -F. '{print $1}')
TEMP_PATH=/tmp/fabui/testcase/${TEST_CASE_NAME}
TEST_CASE_LOG=${TEMP_PATH}/testcase.log
#
# Stop all fabtotum services
#
function stop_fabui_services()
{
	killall -9 php
	killall -9 python
	echo "FABUI services stopped."
}

#
# Start fabtotum services
# 
function start_fabui_services()
{
	/etc/init.d/fabui-ws start &> /dev/null
	/etc/init.d/fabui start    &> /dev/null
	echo "Starting FABUI services."
}

#
# Do hardware totumduino reset
#
function totumduino_reset()
{
	# Configure RESET pin to output
	PIN=17
	STATE=out

	echo "$PIN" > /sys/class/gpio/export 2> /dev/null
	GPIO_DIR="gpio$PIN"
	echo "$STATE" > /sys/class/gpio/$GPIO_DIR/direction 2> /dev/null

	# Reset totumduino
	echo 0 > /sys/class/gpio/$GPIO_DIR/value 2> /dev/null
	sync
	echo 1 > /sys/class/gpio/$GPIO_DIR/value 2> /dev/null
	echo "Totumduino restarted."
}

#
# Cleanup previous test results
#
function testcase_cleanup()
{
	rm -f /tmp/fabui/testcase/${TEST_CASE_NAME}/*
	mkdir -p /tmp/fabui/testcase/${TEST_CASE_NAME}
}

function testcase_evaluate_result()
{
	if [ x"$1" == x"0" ]; then
		echo '{"test":"passed", "log":"'${TEST_CASE_LOG}'", "result":"'$2'"}' | tee ${TEMP_PATH}/run_log.json
	elif [ x"$1" == x"200" ]; then
		echo '{"test":"skipped", "log":"'${TEST_CASE_LOG}'", "result":""}' | tee ${TEMP_PATH}/run_log.json
	else
		echo '{"test":"failed", "log":"'${TEST_CASE_LOG}'", "result":""}' | tee ${TEMP_PATH}/run_log.json
	fi

}
