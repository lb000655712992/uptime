function print_value() {
    $('#Duration').val(backend_data[document.getElementById("Duration").value].Duration);
    $('#Threshold').val(backend_data[document.getElementById("Name").value].Threshold);
}
// Create the namespace instance
let ns = {};
let backend_data={};
let ID = 0;
let UserID = 0;
// Create the model instance
ns.model = (function() {
    'use strict';
    let $event_pump = $('body');

    // Return the API
    return {
        'read': function() {
            let ajax_options = {
                type: 'GET',
                url: 'api/config_table',
                accepts: 'application/json',
                dataType: 'json'
            };
            $.ajax(ajax_options)
            .done(function(data) {
                if(data.result=="success"){
                    backend_data = data.data
                    $event_pump.trigger('model_read_success', [data.data]);
                }
            })
            .fail(function(xhr, textStatus, errorThrown) {
                alert("Server connnect fail.");
            })
        },
        put: function(Duration,Threshold) {
            let ajax_options = {
                type: 'PUT',
                url: 'api/config_table',
                accepts: 'application/json',
                contentType: 'application/json',
                dataType: 'json',
                data: JSON.stringify({
                    'Change':"1",
                    'Duration':Duration,
                    'ID':"1",
                    'Threshold':Threshold
                })
            };
            $.ajax(ajax_options)
            .done(function(data) {
                if(data.result=="success"){
                    alert("success");
                }
                else{
                    alert("fail");
                    $event_pump.trigger('model_register_fail', [data]);
                }
    
            })
            .fail(function(xhr, textStatus, errorThrown) {
                $event_pump.trigger('model_error', [xhr, textStatus, errorThrown]);
            })
        }
    };
}());

// Create the view instance
ns.view = (function() {
    'use strict';

    // return the API
    return {
        reset: function() {
            $('#Duration').val('');
            $('#Threshold').val('');
        },
        build_table: function(data) {
            $('#Threshold').val(data[0].Threshold);
            $('#Duration').val(data[0].Duration);
        }
    };
}());

// Create the controller
ns.controller = (function(m, v) {
    'use strict';

    let model = m,
        view = v,
        $event_pump = $('body'),
        $Duration = $('#Duration'),
        $Threshold = $('#Threshold')

    // Get the data from the model after the controller is done initializing
    setTimeout(function() {
        model.read();
    }, 100)
    // Create our event handlers
    $('.send').click(function(e) {
        let Duration = $Duration.val(),
            Threshold = $Threshold.val()
        model.put(Duration,Threshold)
    })
    $('.reset').click(function(e) {
        view.reset();
    })
    // Handle the model events
    $event_pump.on('model_read_success', function(e, data) {
        view.build_table(data);
    });    
}(ns.model, ns.view));
