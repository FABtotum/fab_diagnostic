<?php
/**
 *
 * @author Krios Mane
 * @version 0.10.0
 * @license https://opensource.org/licenses/GPL-3.0
 *
 */

$config['0001_ethernet_gw'] = array(
    'title' => dgettext('fab_diagnostic', 'Ethernet gateway'),
    'desc' => dgettext('fab_diagnostic', 'Check if ethernet gateway is configured and accessible'),
    'test' => 'ethernet_gw',
    "interactive" => false,
    'expected_result' => 'passed',
    'output_format' => 'terminal'
);

$config['0003_wifi_gw'] = array(
    'title' => dgettext('fab_diagnostic', 'WiFi gateway'),
    'desc' => dgettext('fab_diagnostic', 'Check if WiFi gateway is configured and accessible'),
    'test' => 'wifi_gw',
    "interactive" => false,
    'expected_result' => 'passed',
    'output_format' => 'terminal'
);

$config['0003_wifi_scan'] = array(
    'title' => dgettext('fab_diagnostic', 'WiFi scan'),
    'desc' => dgettext('fab_diagnostic', 'Check if WiFi scan feature is working'),
    'test' => 'wifi_scan',
    "interactive" => false,
    'expected_result' => 'passed',
    'output_format' => 'terminal'
);

$config['0002_internet_dns'] = array(
    'title' => dgettext('fab_diagnostic', 'Internet DNS'),
    'desc' => dgettext('fab_diagnostic', 'Check if DNS server is configured and accessible'),
    'test' => 'internet_dns',
    "interactive" => false,
    'expected_result' => 'passed',
    'output_format' => 'terminal'
);

$config['0001_internet'] = array(
    'title' => dgettext('fab_diagnostic', 'Internet connection'),
    'desc' => dgettext('fab_diagnostic', 'Check if internet connection is available'),
    'test' => 'internet',
    "interactive" => false,
    'expected_result' => 'passed',
    'output_format' => 'terminal'
);

$config['0002_internet_speed'] = array(
    'title' => dgettext('fab_diagnostic', 'Update server'),
    'desc' => dgettext('fab_diagnostic', 'Check connection to the update server and download speed'),
    'test' => 'update_speed',
    "interactive" => false,
    'expected_result' => 'passed',
    'output_format' => 'terminal'
);


?>