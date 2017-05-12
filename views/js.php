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
				$("#log-content").html( html );
				$("#logsModal").modal('show');
				
				$(".test-action").removeClass('disabled');
			});
	}
	
	function runTestCase(subsystem, test_case)
	{
		console.log("run testcase", subsystem, test_case);
		
		var objectString = subsystem + "_" + test_case;
		var obj_check = eval("typeof " + objectString);
		
		if(obj_check == "object")
		{
			var fun_check = eval("typeof " + objectString + ".start");
			if(fun_check == "function")
			{
				eval(objectString+".start()");
			}
		}
		
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
					html='<button class="btn btn-success test-action" data-subsystem="'+subsystem+'" data-test-case="'+test_case+'" data-action="show-log"><i class="fa fa-check-circle" aria-hidden="true"></i> Passed</button>';
				else if(data.test == "skipped")
					html='<button class="btn btn-warning test-action" data-subsystem="'+subsystem+'" data-test-case="'+test_case+'" data-action="show-log"><i class="fa fa-exclamation-triangle" aria-hidden="true"></i> Skipped</button>';
				else
					html='<button class="btn btn-danger test-action" data-subsystem="'+subsystem+'" data-test-case="'+test_case+'" data-action="show-log"><i class="fa fa-times-circle" aria-hidden="true"></i> Failed</button>';
			}
			
			if(obj_check == "object")
			{
				var fun_check = eval("typeof " + objectString + ".end");
				if(fun_check == "function")
				{
					eval(objectString+".end()");
				}
			}
			
			$("#"+subsystem+"_"+test_case+"-result").html(html);
			$('.test-action').removeClass('disabled');
			$('.test-action').unbind('click');
			$('.test-action').on('click', doTestAction);
			
		});
	}
	
	function getPlotTemperatures(source)
	{
		var seriesTemp   = [];
		var seriesTarget = [];
		var data            = new Array();
		
		if(source == undefined)
		{
			source = "ext";
		}
		
		var temp_label = _("Nozzle temperature");
		var target_label = _("Nozzle target");
		
		if(source == "ext")
		{
			$.each( temperaturesPlot.extruder.temp, function( key, plot ) {
				seriesTemp.push([plot.time, plot.value]);
			});
			$.each( temperaturesPlot.extruder.target, function( key, plot ) {
				seriesTarget.push([plot.time, plot.value]);
			});
			
			
		}
		else if(source == "bed")
		{
			$.each( temperaturesPlot.bed.temp, function( key, plot ) {
				seriesTemp.push([plot.time, plot.value]);
			});
			$.each( temperaturesPlot.bed.target, function( key, plot ) {
				seriesTarget.push([plot.time, plot.value]);
			});
			
			temp_label = _("Bed temperature");
			target_label = _("Bed target");
		}
		
		// actual line
		data.push({
			data: seriesTemp,
			lines: { show: true, fill: true, lineWidth:0.5},
			label: temp_label,
			color: "#FF0000",
			points: {"show" : false}
		});
		// target line
		data.push({
			data: seriesTarget,
			lines: { show: true, fill: false, lineWidth:1 },
			label: target_label,
			color: "#33ccff",
			points: {"show" : false}
		});
		return data;
	}

</script>
