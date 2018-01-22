selftests_ambient_lights = {
	
	start: function () {
		window.customNotificationsHandler = selftests_ambient_lights.customNotificationsHandler;
	},
	
	end: function () {
		window.customNotificationsHandler = undefined;
	},
	
	sendResponse: function (id, response)
	{
		trigger_data = [id, response];
		
		$.ajax({
			type: 'post',
			url: '/fabui/control/trigger/custom',
			data: {'data' : trigger_data},
			dataType: 'json'
		}).done(function(data) {
		});
	},
	
	customNotificationsHandler: function(obj) {
		
		if(obj.type == "selftest")
		{
			switch(obj.data.type)
			{
				case "confirm": {
					var id = obj.data.id;
					var msg = obj.data.msg;
					var buttons = obj.data.buttons;
					
					$.SmartMessageBox({
							title: "<i class='fa fa-warning-circle'></i> " + msg,
							content: '',
							buttons: buttons
						}, function(ButtonPressed) {
							selftests_ambient_lights.sendResponse(id, ButtonPressed);
						});
					
					} break;
				case "question": {
					var id = obj.data.id;
					var msg = obj.data.msg;
					var buttons = obj.data.buttons;
					
					$.SmartMessageBox({
							title: "<i class='fa fa-question-circle'></i> " + msg,
							content: '',
							buttons: buttons
						}, function(ButtonPressed) {
							
							selftests_ambient_lights.sendResponse(id, ButtonPressed);
						});
					
					} break;
			}
		}

	},
};
