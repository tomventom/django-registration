$(function () {
    var pathname = window.location.pathname;
    // var current = pathname.split("/")[1];
    if (pathname === "") {
        $("[href='./\']").addClass('active');
    } else {
        $("[href='" + pathname + "']").addClass('active');
    }
});
