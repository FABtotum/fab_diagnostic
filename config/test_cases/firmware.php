<?php
/**
 *
 * @author Krios Mane
 * @version 0.10.0
 * @license https://opensource.org/licenses/GPL-3.0
 *
 */

$config['0001_bootloader'] = array(
    'title' => dgettext('fab_diagnostic', 'Bootloader'),
    'desc' => dgettext('fab_diagnostic', 'Check bootloader communcation'),
    'test' => 'connection',
    "interactive" => false,
    'expected_result' => 'passed',
    'output_format' => 'terminal'
);

$config['0002_baud_115k'] = array(
    'title' => dgettext('fab_diagnostic', 'Baudrate (115k)'),
    'desc' => dgettext('fab_diagnostic', 'Check if totumduino is using 115200 baudrate'),
    'test' => 'baud_115k',
    "interactive" => false,
    'expected_result' => 'failed',
    'output_format' => 'terminal'
);

$config['0003_baud_250k'] = array(
    'title' => dgettext('fab_diagnostic', 'Baudrate (250k)'),
    'desc' => dgettext('fab_diagnostic', 'Check if totumduino is using 250000 baudrate'),
    'test' => 'baud_250k',
    "interactive" => false,
    'expected_result' => 'passed',
    'output_format' => 'terminal'
);

$config['0004_fw_version'] = array(
    'title' => dgettext('fab_diagnostic', 'Firmware version'),
    'desc' => dgettext('fab_diagnostic', 'Get firmware version'),
    'test' => 'version',
    "interactive" => false,
    'expected_result' => 'passed',
    'output_format' => 'terminal'
);

$config['0005_dump_flash'] = array(
    'title' => dgettext('fab_diagnostic', 'Dump flash'),
    'desc' => dgettext('fab_diagnostic', 'Dump totumduino flash content to a file'),
    'test' => 'dump_flash',
    "interactive" => false,
    'expected_result' => 'passed',
    'output_format' => 'terminal'
);

$config['0006_dump_flash'] = array(
    'title' => dgettext('fab_diagnostic', 'Dump EEPROM'),
    'desc' => dgettext('fab_diagnostic', 'Dump totumduino EEPROM content to a file'),
    'test' => 'dump_eeprom',
    "interactive" => false,
    'expected_result' => 'passed',
    'output_format' => 'terminal'
);


?>