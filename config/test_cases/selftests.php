<?php
/**
 *
 * @author Krios Mane
 * @version 0.10.0
 * @license https://opensource.org/licenses/GPL-3.0
 *
 */

$config['0001_services'] = array(
    'title' => dgettext('fab_diagnostic', 'FABUI services'),
    'desc' => dgettext('fab_diagnostic', 'Check if all fabui services are running'),
    'test' => 'services',
    'expected_result' => 'passed',
    'output_format' => 'html'
);

$config['0002_totumduino'] = array(
    'title' => dgettext('fab_diagnostic', 'Totumduino link'),
    'desc' => dgettext('fab_diagnostic', 'Check if communication with totumduino is working'),
    'test' => 'totumduino_link',
    'expected_result' => 'passed',
    'output_format' => 'html'
);

$config['0003_psu'] = array(
    'title' => dgettext('fab_diagnostic', 'Power supply check'),
    'desc' => dgettext('fab_diagnostic', 'Check power supply voltage and current'),
    'test' => 'psu',
    'expected_result' => 'passed',
    'output_format' => 'html'
);

$config['0004_nozzle_heater'] = array(
    'title' => dgettext('fab_diagnostic', 'Nozzle heater'),
    'desc' => dgettext('fab_diagnostic', 'Check the nozzle heater'),
    'test' => 'nozzle_heater',
    'expected_result' => 'passed',
    'output_format' => 'html'
);

$config['0005_bed_heater'] = array(
    'title' => dgettext('fab_diagnostic', 'Bed heater'),
    'desc' => dgettext('fab_diagnostic', 'Check the bed heater'),
    'test' => 'bed_heater',
    'expected_result' => 'passed',
    'output_format' => 'html'
);

$config['0006_milling_motor'] = array(
    'title' => dgettext('fab_diagnostic', 'Milling motor'),
    'desc' => dgettext('fab_diagnostic', 'Check if all fabui services are running'),
    'test' => 'milling_motor',
    'expected_result' => 'passed',
    'output_format' => 'html'
);

$config['0007_endstops_movement'] = array(
    'title' => dgettext('fab_diagnostic', 'Endstops and movement'),
    'desc' => dgettext('fab_diagnostic', 'Check endstops functionality and XYZ movement'),
    'test' => 'endstops_movement',
    'expected_result' => 'passed',
    'output_format' => 'html'
);

$config['0008_speed'] = array(
    'title' => dgettext('fab_diagnostic', 'Speed test'),
    'desc' => dgettext('fab_diagnostic', 'Check different movement speed'),
    'test' => 'speed_movement',
    'expected_result' => 'passed',
    'output_format' => 'html'
);

$config['0009_probe'] = array(
    'title' => dgettext('fab_diagnostic', 'Touch probe'),
    'desc' => dgettext('fab_diagnostic', 'Check touch probe functionality'),
    'test' => 'probe',
    'expected_result' => 'passed',
    'output_format' => 'html'
);

$config['0010_ambient_lights'] = array(
    'title' => dgettext('fab_diagnostic', 'Ambient lights'),
    'desc' => dgettext('fab_diagnostic', 'Check if the RGB ambient LEDs are working'),
    'test' => 'ambient_lights',
    'expected_result' => 'passed',
    'output_format' => 'html'
);




?>