// Create the namespace instance
let ns = {};
// Create the model instance
ns.model = (function() {
    'use strict';
    let $event_pump = $('body');
    // Return the API
    return {
        'read': function() {
            let ajax_options = {
                type: 'GET',
                url: 'api/eMail',
                accepts: 'application/json',
                dataType: 'json'
            };
            $.ajax(ajax_options)
            .done(function(data) {
                if(data.result=="success"){
                    $event_pump.trigger('model_read_success', [data.data]);
                }
            })
            .fail(function(xhr, textStatus, errorThrown) {
                alert("Server connnect fail.");
            })
        }
    };
}());

// Create the view instance
ns.view = (function() {
    'use strict';

    let $user = $('#user'),
        $password = $('#password');

    // return the API
    return {
        reset: function() {
            $password.val('');
            $user.val('').focus();
        },
        build_table: function(data) {
            let rows = ''
            if (data) {
                for (let i=0, l=data.length; i < l; i++) {
                    rows += `<tr><td>${data[i].ID}</td>\
                                 <td>${data[i].eMail}</td>`;
                }
                $('.table1 table > tbody').append(rows);
            }
        },
    };
}());

// Create the controller
ns.controller = (function(m, v) {
    'use strict';

    let model = m,
        view = v,
        $event_pump = $('body');

    // Get the data from the model after the controller is done initializing
    setTimeout(function() {
        model.read();
    }, 100)
    // Create our event handlers
    // Handle the model events
    $event_pump.on('model_read_success', function(e, data) {
        view.build_table(data);
    });    
}(ns.model, ns.view));
