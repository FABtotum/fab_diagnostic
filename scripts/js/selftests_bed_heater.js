selftests_bed_heater = {
	temperaturesGraph : undefined,
	showExtruderLines : true,
	update: undefined,
	
	start: function () {
		console.log('selftests_bed_heater: START');
		
		$("#modal-graph").show();
		$("#modal-trace").show();
		
		$("#testcaseModal").modal({ keyboard: false, backdrop: 'static' });
		$("#testcaseModal").modal('show');
		$('#testcaseModal').on('shown.bs.modal', function() {
			selftests_bed_heater.initGraph();
		})
	},
	
	end: function () {
		console.log('selftests_bed_heater: END');
		clearInterval(selftests_bed_heater.update);
		selftests_bed_heater.temperaturesGraph.destroy();
		selftests_bed_heater.temperaturesGraph = undefined;
		$("#testcaseModal").modal('hide');
		$('#testcaseModal').unbind('shown.bs.modal');
		$("#modal-graph").hide();
		$("#modal-trace").hide();
	},
	
	initGraph: function() {
		selftests_bed_heater.temperaturesGraph = $.plot("#temperatures-chart", getPlotTemperatures("bed"), {
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
				 timeformat: "%Y/%m/%d",
				 zoomRange: [1,100]
			},
			yaxis: {
				min: 0,
				max: 100,
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
		selftests_bed_heater.update = setInterval(selftests_bed_heater.updateGraph, 1000);
	},
	
	updateGraph: function() {
		var data = getPlotTemperatures("bed");
		if(typeof selftests_bed_heater.temperaturesGraph !== 'undefined' ){
			selftests_bed_heater.temperaturesGraph.setData(data);
			selftests_bed_heater.temperaturesGraph.draw();
			selftests_bed_heater.temperaturesGraph.setupGrid();
		}
	}
};
