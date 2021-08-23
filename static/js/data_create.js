let ns = {};
// Create the model instance
ns.model = (function() {
    'use strict';
    let $event_pump = $('body');

    // Return the API
    return {
        post: function(IP,Hostname,Username,Password,Port,Uptime,Status) {
            let ajax_options = {
                type: 'POST',
                url: '/api/data_table',
                accepts: 'application/json',
                contentType: 'application/json',
                dataType: 'json',
                data: JSON.stringify({
                    'IP':IP,
                    'Hostname':Hostname,
                    'Username':Username,
                    'Password':Password,
                    'Port':Port,
                    'Uptime':Uptime,
                    'Status':Status
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

    let $IP = $('#IP'),
        $Hostname = $('#Hostname'),
        $Username = $('#Username'),
        $Port = $('#Port'),
        $Uptime = $('#Uptime'),
        $Status = $('#Status'),
        $Password = $('#Password');
    // return the API
    return {
        reset: function() {
            $IP.val('');
            $Hostname.val('');
            $Username.val('');
            $Port.val('');
            $Uptime.val('');
            $Status.val('');
            $Password.val('');
        }
    };
}());

// Create the controller
ns.controller = (function(m, v) {
    'use strict';

    let model = m,
        view = v,
        $event_pump = $('body'),
        $IP = $('#IP'),
        $Hostname = $('#Hostname'),
        $Username = $('#Username'),
        $Port = $('#Port'),
        $Uptime = $('#Uptime'),
        $Status = $('#Status'),
        $Password = $('#Password');

    // Get the data from the model after the controller is done initializing

    // Validate input
    function validate(parameter) {
        let flag=true;
        for(let i=0;i<parameter.length;i++){
            if(parameter[i]==""){
                flag=false;
            }
        }
        return flag;
    }
    // Create our event handlers
    $('.send').click(function(e) {
        let IP = $IP.val(),
            Hostname = $Hostname.val(),
            Username = $Username.val(),
            Password = $Password.val(),
            Port = $Port.val(),
            Uptime = $Uptime.val(),
            Status = $Status.val();
        e.preventDefault();
        if (validate([IP,Hostname,Username,Password,Port,Uptime,Status])) {
            model.post(IP,Hostname,Username,Password,Port,Uptime,Status);
        } else {
            alert('error');
        }
    })
    $('.reset').click(function(e) {
        view.reset();
    })
    // Handle the model events
    $event_pump.on('model_register_fail', function(e, data) {
        view.reset();
    });    
}(ns.model, ns.view));
