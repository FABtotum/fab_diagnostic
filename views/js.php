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

	var logs = {};

	$(function () {
		$('.test-action').on('click', doTestAction);
	});

	function doTestAction()
	{
		var subsystem = $(this).attr('data-subsystem');
		var test_case = $(this).attr('data-test-case');
		var action = $(this).attr('data-action');
		
		console.log("doTestAction", action);
		
		switch(action)
		{
			case "run":
				$(".test-action").addClass('disabled');
				runTestCase(subsystem, test_case);
				break;
			case "show-log":
				$(".test-action").addClass('disabled');
				showLog(subsystem, test_case);
				break;
		}
		
		return false;
	}
	
	function showLog(subsystem, test_case)
	{
		console.log("LOG:", "<?php echo site_url(plugin_url("getTestCaseLog"))?>");
		$.get("<?php echo site_url(plugin_url("getTestCaseLog"))?>/"+subsystem+"/"+test_case, 
			function(data){
				var html = "";
				var ansi_up = new AnsiUp;
				$.each(data.split("\n"), function( index, value ) {
					var tmp = ansi_up.ansi_to_html(value);
					html += tmp + "<br>";
				});
				$(".modal-body").html( html );
				$("#logsModal").modal('show');
				
				$(".test-action").removeClass('disabled');
			});
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
			var html = ' <span class="badge label-danger"><i class="fa fa-times-circle" aria-hidden="true"></i> Failed to execute test</span>';
			
			if(data)
			{
				
				if(data.test == "passed")
				{
					html='<button class="btn btn-success test-action" data-subsystem="'+subsystem+'" data-test-case="'+test_case+'" data-action="show-log"><i class="fa fa-check-circle" aria-hidden="true"></i> Passed</button>';
				}
				else
				{
					html='<button class="btn btn-danger test-action" data-subsystem="'+subsystem+'" data-test-case="'+test_case+'" data-action="show-log"><i class="fa fa-times-circle" aria-hidden="true"></i> Failed</button>';
				}
			}
			
			$("#"+subsystem+"_"+test_case+"-result").html(html);
			$('.test-action').removeClass('disabled');
			$('.test-action').unbind('click');
			$('.test-action').on('click', doTestAction);
			
		});
	}

</script>
