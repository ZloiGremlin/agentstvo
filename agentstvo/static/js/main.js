$(function () {
    var $pxs_container = $('#pxs_container');
    $pxs_container.parallaxSlider();

    $('.slider').nivoSlider();

    $('.colors a').click(function(){
        $('.colors li').removeClass('active');
        $(this).parent().addClass('active');
        $(this).parents('.decor').find('.thumber a:visible').hide(0);
        $($(this).attr('href')).show();
        return false;
    });


    $('.thumbnails').each(function(){
        $(this).find('.lbox3').iLightBox({
            skin:'dark',
            path: 'vertical',
            infinite: true
        });
    });

    $('.lbox').iLightBox({
        skin:'dark',
        path: 'vertical',
        infinite: true
    });

    $('.decor').each(function(){
        $(this).find('.lbox2').iLightBox({
            skin:'dark',
            path: 'vertical',
            infinite: true
        });

    });



    $comments = $('<div class="comments"></div>');

    $('.lbox-comment').iLightBox({
        skin:'dark rightcom',
        path: 'vertical',
        infinite: true,
        styles: {
            pageOffsetX: 300,
            nextOffsetX: 15,
            nextOpacity: 0,
            prevOffsetX: 15,
            prevOpacity: 0
        },
        callback: {
            onOpen: function(){
                $('body').append($comments);

                var t = this,
                    id = t.itemsObject[t.vars.current].data('cake');
                $comments.html($('#cake-'+id).find('.info').html());
            },
            onHide: function(){
                $comments.hide().remove();
            },
            onAfterChange: function(api){
                var t = this,
                    id = t.itemsObject[api.currentItem].data('cake');
                $comments.html($('#cake-'+id).find('.info').html());
            },
            onAfterLoad: function(api){
                $comments.fadeIn(180);
            },
            onEnterFullScreen: function(){
                $comments.hide();
            },
            onExitFullScreen: function(){
                $comments.show();
            }
        }
    });

});