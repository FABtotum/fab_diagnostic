#
# Stop all fabtotum services
#
function stop_fabui_services()
{
	killall -9 php
	killall -9 python
}

#
# Start fabtotum services
# 
function start_fabui_services()
{
	/etc/init.d/fabui-ws start
	/etc/init.d/fabui start
}

#
# Do hardware totumduino reset
#
function totumduino_reset()
{
	# Configure RESET pin to output
	PIN=17
	STATE=out

	echo "$PIN" > /sys/class/gpio/export
	GPIO_DIR="gpio$PIN"
	echo "$STATE" > /sys/class/gpio/$GPIO_DIR/direction

	# Reset totumduino
	echo 0 > /sys/class/gpio/$GPIO_DIR/value
	sync
	echo 1 > /sys/class/gpio/$GPIO_DIR/value
}

#
# Cleanup previous test results
#
function testcase_cleanup()
{
	rm -f /tmp/fabui/testcase.*
}

function testcase_evaluate_result()
{
	if [ x"$1" == x"0" ]; then
		echo '{"test":"passed", "log":"/tmp/fabui/testcase.log", "result":"'$2'", "download": "'$3'"}'
	else
		echo '{"test":"failed", "log":"/tmp/fabui/testcase.log", "result":"", "download":""}'
	fi

}
