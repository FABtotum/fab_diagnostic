selftests_nozzle_heater = {
	temperaturesGraph : undefined,
	showExtruderLines : true,
	update: undefined,
	
	start: function () {
		console.log('selftests_nozzle_heater: START');
		
		$("#modal-graph").show();
		$("#modal-trace").show();
		
		$("#testcaseModal").modal({ keyboard: false, backdrop: 'static' });
		$("#testcaseModal").modal('show');
		$('#testcaseModal').on('shown.bs.modal', function() {
			selftests_nozzle_heater.initGraph();
		})
	},
	
	end: function () {
		console.log('selftests_nozzle_heater: END');
		clearInterval(selftests_nozzle_heater.update);
		selftests_nozzle_heater.temperaturesGraph.destroy();
		selftests_nozzle_heater.temperaturesGraph = undefined;
		$("#testcaseModal").modal('hide');
		$('#testcaseModal').unbind('shown.bs.modal');
		$("#modal-graph").hide();
		$("#modal-trace").hide();
	},
	
	initGraph: function() {
		selftests_nozzle_heater.temperaturesGraph = $.plot("#temperatures-chart", getPlotTemperatures("ext"), {
			series : {
				lines : {
					show : true,
					lineWidth : 1,
					fill : true,
					fillColor : {
						colors : [{
							opacity : 0.1
						}, {
							opacity : 0.15
						}]
					}
				}
			},
			xaxis: {
				mode: "time",
				show: true,
				tickFormatter: function (val, axis) {
					var d = new Date(val);
					return d.getHours() + ":" + d.getMinutes();
				},
				 timeformat: "%Y/%m/%d"
			},
			yaxis: {
				min: 0,
				max: 250,
				tickFormatter: function (v, axis) {
					return v + "&deg;C";
				},
			},
			tooltip : true,
			tooltipOpts : {
				content : "%s: %y &deg;C",
				defaultTheme : false
			},
			legend: {
				show : true
			},
			grid: {
				hoverable : true,
				clickable : true,
				borderWidth : 0,
				borderColor : "#efefef",
				tickColor :  "#efefef"
				
			},
			zoom:{
				interactive: false
			}
			
		});
		selftests_nozzle_heater.update = setInterval(selftests_nozzle_heater.updateGraph, 1000);
	},
	
	updateGraph: function() {
		var data = getPlotTemperatures("ext");
		if(typeof selftests_nozzle_heater.temperaturesGraph !== 'undefined' ){
			selftests_nozzle_heater.temperaturesGraph.setData(data);
			selftests_nozzle_heater.temperaturesGraph.draw();
			selftests_nozzle_heater.temperaturesGraph.setupGrid();
		}
	}
};
