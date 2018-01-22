<?php
/**
 *
 * @author Krios Mane
 * @version 0.10.0
 * @license https://opensource.org/licenses/GPL-3.0
 *
 */

$config['0001_system_tools'] = array(
    'title' => dgettext('fab_diagnostic', 'System tools'),
    'desc' => dgettext('fab_diagnostic', 'Check system tools functionality'),
    'test' => 'system_tools',
    "interactive" => false,
    'expected_result' => 'passed',
    'output_format' => 'terminal'
);

$config['0002_bundles_integrity'] = array(
    'title' => dgettext('fab_diagnostic', 'Bundles integrity'),
    'desc' => dgettext('fab_diagnostic', 'Check bundles checksums'),
    'test' => 'bundles_integrity',
    "interactive" => false,
    'expected_result' => 'passed',
    'output_format' => 'terminal'
);

$config['0003_partitions'] = array(
    'title' => dgettext('fab_diagnostic', 'Partitions'),
    'desc' => dgettext('fab_diagnostic', 'Check filesystem partition sizes and metadata'),
    'test' => 'partitions',
    "interactive" => false,
    'expected_result' => 'passed',
    'output_format' => 'terminal'
);

$config['0004_free_space'] = array(
    'title' => dgettext('fab_diagnostic', 'Disk free space'),
    'desc' => dgettext('fab_diagnostic', 'Check filesystem partition have enough free space'),
    'test' => 'free_space',
    "interactive" => false,
    'expected_result' => 'passed',
    'output_format' => 'terminal'
);

$config['0005_python_check'] = array(
    'title' => dgettext('fab_diagnostic', 'Python check'),
    'desc' => dgettext('fab_diagnostic', 'Check for python and required modules'),
    'test' => 'python_check',
    "interactive" => false,
    'expected_result' => 'passed',
    'output_format' => 'terminal'
);

$config['0006_php_check'] = array(
    'title' => dgettext('fab_diagnostic', 'PHP check'),
    'desc' => dgettext('fab_diagnostic', 'Check for php and required modules'),
    'test' => 'php_check',
    "interactive" => false,
    'expected_result' => 'passed',
    'output_format' => 'terminal'
);


?>