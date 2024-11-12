$(document).ready(function() {
    $('.slider-for').slick({
        slidesToShow: 1,
        slidesToScroll: 1,
        arrows: false,
        fade: true,
        asNavFor: '.slider-nav',
    });

    $('.slider-nav').slick({
        slidesToShow: 5,
        slidesToScroll: 1,
        asNavFor: '.slider-for',
        dots: false,
        infinity: true,
        centerMode: true,

        focusOnSelect: true,
        arrows: true,
        prevArrow: '<div class="prev"></div>',
        nextArrow: '<div class="next"></div>',

        responsive: [
            {
                breakpoint: 1000,
                settings: {
                    arrows: false,
                }
            }
        ]
    });

    // Инициализация Magnific Popup
    $('.image-link').magnificPopup({
        type: 'image',
        gallery: {
            enabled: true // Включаем галерею
        },
        callbacks: {
            beforeOpen: function() {
                // Устанавливаем текущий индекс для галереи
                this.st.index = $('.image-link').index(this.st.el);
            }
        }

    });
});
