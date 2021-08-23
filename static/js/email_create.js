// Create the namespace instance
let ns = {};
// Create the model instance
ns.model = (function() {
    'use strict';
    let $event_pump = $('body');

    // Return the API
    return {
        post: function(eMail) {
            let ajax_options = {
                type: 'POST',
                url: '/api/eMail',
                accepts: 'application/json',
                contentType: 'application/json',
                dataType: 'json',
                data: JSON.stringify({
                    'eMail':eMail
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

    let $eMail = $('#eMail');
    // return the API
    return {
        reset: function() {
            $eMail.val('');
        }
    };
}());

// Create the controller
ns.controller = (function(m, v) {
    'use strict';

    let model = m,
        view = v,
        $event_pump = $('body'),
        $eMail = $('#eMail');

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
        let eMail = $eMail.val();
        e.preventDefault();
        if (validate([eMail])) {
            model.post(eMail);
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
