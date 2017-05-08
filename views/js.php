<?php
/**
 * 
 * @author Daniel Kesler
 * @version 0.10.0
 * @license https://opensource.org/licenses/GPL-3.0
 * 
 */
?>

<script type="text/javascript">

	$(function () {
		$('.test-action').on('click', doTestAction);
	});

	function doTestAction()
	{
		var subsystem = $(this).attr('data-subsystem');
		var test_case = $(this).attr('data-test-case');
		var action = $(this).attr('data-action');
		
		switch(action)
		{
			case "run":
				runTestCase(subsystem, test_case);
				break;
		}
	}
	
	function runTestCase(subsystem, test_case)
	{
		console.log("run testcase", subsystem, test_case);
		
		$.ajax({
			  url: "<?php echo site_url( plugin_url("runTestCase") ) ?>/" + subsystem + "/" + test_case,
			  dataType : 'json',
			  type: "POST",
			  data : {}
		}).done(function(data) {
			console.log(data);
		});
	}

</script>
