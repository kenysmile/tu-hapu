odoo.define('portal.pager', function (require) {
    'use strict';
    require('web.dom_ready');
    var ajax = require('web.ajax');
    var url_args = $('#url_args').val();

    $(".cc-button-gopage").click( function(e) {
        e.preventDefault();
        if (url_args) {
            window.location.pathname = path + $('#page_count').val(); + '?' + $.param(jQuery.parseJSON(url_args));
        } else {
            window.location.pathname = path + $('.input_number_page').val();;
        }
    });
});