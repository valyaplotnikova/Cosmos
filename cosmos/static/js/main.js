Fancybox.bind('[data-fancybox="gallery"]', {

});


const el = document.querySelector(".test-clc");

console.log('el', el)



$(document).ready(function(){
    $('.slider-for').slick({
        slidesToShow: 1,
        slidesToScroll: 1,
        arrows: false,
        fade: true,
        asNavFor: '.slider-nav',


    });
    $('.slider-nav').slick({
        slidesToShow: 3,
        slidesToScroll: 1,
        asNavFor: '.slider-for',
        dots: true,
        centerMode: true,
        focusOnSelect: true,
        variableWidth: true,

        responsive: [
            {
              breakpoint: 1000,
              settings: {
                arrows: false,
              }
            }
        ]
    });


});