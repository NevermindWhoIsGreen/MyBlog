$(function(){
    $('#search').on('keyup', function(){
       var _this = $(this),
               found = $('#main-search-found');
        if (_this.val().length >= 3) {
            $.ajax({
                type: "POST",
                url: "/search/",
                data: {
                    'search_query': $('#search').val(),
                    'csrfmiddlewaretoken': $("input[name=csrfmiddlewaretoken]").val()
                },
                dataType: 'html',
                success: function(data){
                    found.html(data).slideDown();
                    console.log(data);
                }
            });
        } else {
            found.slideUp();
        }
    }).on('focusout', function(){
        $('#main-search-found').slideUp();
    }).on('focus', function(){
        if ($(this).val().length >= 3) {
            $('#main-search-found').slideDown();
        }
    });
});
