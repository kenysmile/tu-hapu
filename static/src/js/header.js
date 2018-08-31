$(document).ready(function() {

    // Ẩn hiện header
    function ToggleMenuHeader() {
        $('.em_header').fadeToggle(200);
        $('.em_overlay').fadeToggle(200);
    }
    
    $('.js_open_sidebar').on("click", function() {
        ToggleMenuHeader();
    });
    $('.em_overlay').on("click", function() {
        ToggleMenuHeader();
    });

    // Mở & đóng modal form đang nhập đăng ký
    $('.js_open_reg_form').on("click", function(e) {
        e.preventDefault();
        $('.modal-backdrop').hide();
        $('#reg_form').modal('show');
        $('#login_form').hide();
    });

    // Khởi tạo select2 địa chỉ
    $('.js_city_select').select2();
    
});