// google analytics
var _gaq = _gaq || [];
_gaq.push(['_setAccount', 'UA-306569-3']);
_gaq.push(['_trackPageview']);

(function() {
    var ga = document.createElement('script'),
        s;
    ga.type = 'text/javascript';
    ga.async = true;
    ga.src = ('https:' === document.location.protocol ? 'https://ssl' : 'http://www') + '.google-analytics.com/ga.js';
    s = document.getElementsByTagName('script')[0]; s.parentNode.insertBefore(ga, s);
}());

$(function () {
    $('#search').click(function (e) {
        e.preventDefault();
        $('searchform').submit();
    });
});
