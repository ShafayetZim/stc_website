
$(function($) {

    "use strict";

    //===== 01. Main Menu
    function mainMenu() {
        // Variables
        var var_window = $(window),
            navContainer = $('.header-navigation'),
            navbarToggler = $('.navbar-toggler'),
            navMenu = $('.nav-menu'),
            navMenuLi = $('.nav-menu ul li ul li'),
            closeIcon = $('.navbar-close');
        // navbar toggler
        navbarToggler.on('click', function() {
            navbarToggler.toggleClass('active');
            navMenu.toggleClass('menu-on');
        });
        // close icon
        closeIcon.on('click', function() {
            navMenu.removeClass('menu-on');
            navbarToggler.removeClass('active');
        });

        // adds toggle button to li items that have children
        navMenu.find('li a').each(function() {
            if ($(this).next().length > 0) {
                $(this)
                    .parent('li')
                    .append(
                        '<span class="dd-trigger"><i class="fas fa-angle-down"></i></span>'
                    );
            }
        });
        // expands the dropdown menu on each click
        navMenu.find('li .dd-trigger').on('click', function(e) {
            e.preventDefault();
            $(this)
                .parent('li')
                .children('ul')
                .stop(true, true)
                .slideToggle(350);
            $(this).parent('li').toggleClass('active');
        });

        // check browser width in real-time
        function breakpointCheck() {
            var windoWidth = window.innerWidth;
            if (windoWidth <= 1199) {
                navContainer.addClass('breakpoint-on');
            } else {
                navContainer.removeClass('breakpoint-on');
            }
        }

        breakpointCheck();
        var_window.on('resize', function() {
            breakpointCheck();
        });
    };
    // Panel Widget
    var panelIcon = $('.off-menu'),
    panelClose = $('.panel-close'),
    panelWrap = $('.offcanvas-panel');
    panelIcon.on('click', function (e) {
        panelWrap.toggleClass('panel-on');
        e.preventDefault();
    });
    panelClose.on('click', function (e) {
        panelWrap.removeClass('panel-on');
        e.preventDefault();
    });
    // Document Ready
    $(document).ready(function() {
        mainMenu();
    });

    //===== Prealoder
    $(window).on('load', function(event) {
        $('.preloader').delay(500).fadeOut('500');
    })

    //===== Sticky
    $(window).on('scroll', function(event) {
        var scroll = $(window).scrollTop();
        if (scroll < 190) {
            $(".header-navigation").removeClass("sticky");
        } else {
            $(".header-navigation").addClass("sticky");
        }
    });

    //====== Magnific Popup
    $('.video-popup').magnificPopup({
        type: 'iframe'
        // other options
    });
    $('.img-popup').magnificPopup({
        type: 'image',
        gallery: {
            enabled: true
        }
    });
    //===== Back to top
    $(window).on('scroll', function(event) {
        if ($(this).scrollTop() > 600) {
            $('.back-to-top').fadeIn(200)
        } else {
            $('.back-to-top').fadeOut(200)
        }
    });

    //Animate the scroll to top
    $('.back-to-top').on('click', function(event) {
        event.preventDefault();
        $('html, body').animate({
            scrollTop: 0,
        }, 1500);
    });
    //===== counter up

    $('.counter').counterUp({
        delay: 80,
        time: 4000
    });
    
    // jquery nice select js
    $('select').niceSelect();
    
    //=====  Easypiechart js
    $('.chart_1').easyPieChart({
        size: 130,
        barColor: '#ff7554',
        trackColor: '#373f4b',
        easing: 'easeInOut',
        scaleColor: false,
        lineCap: 'circle',
        lineWidth: 10,
        animate: 2000
    });
    
    //=====  Slick Slider js
    $('.hero-slider-one').slick({
        dots: false,
        arrows: true,
        infinite: true,
        autoplay: true,
        Speed: 500,
        fade: true,
        prevArrow: '<div class="prev"><i class="fas fa-angle-left"></i></div>',
        nextArrow: '<div class="next"><i class="fas fa-angle-right"></i></div>',
        slidesToShow: 1,
        slidesToScroll: 1,
        responsive: [
            {
                breakpoint: 1180,
                settings: {
                    arrows: false
                }
            },
            {
                breakpoint: 480,
                settings: {
                    arrows: false
                }
            }
        ]
    });
    $('.hero-slider-two,.hero-slider-three').slick({
        dots: false,
        arrows: true,
        infinite: true,
        autoplay: true,
        Speed: 700,
        fade: true,
        prevArrow: '<div class="prev"><i class="fas fa-angle-left"></i></div>',
        nextArrow: '<div class="next"><i class="fas fa-angle-right"></i></div>',
        slidesToShow: 1,
        slidesToScroll: 1,
        responsive: [
            {
                breakpoint: 1180,
                settings: {
                    arrows: false
                }
            },
            {
                breakpoint: 480,
                settings: {
                    arrows: false
                }
            }
        ]
    });
    var sliderArrows = $('.protfolio-arrows-one');
    $('.protfolio-slider-one').slick({
        dots: false,
        appendArrows: sliderArrows,
        arrows: true,
        infinite: true,
        autoplay: true,
        Speed: 500,
        prevArrow: '<div class="prev"><i class="fas fa-arrow-left"></i></div>',
        nextArrow: '<div class="next"><i class="fas fa-arrow-right"></i></div>',
        slidesToShow: 4,
        slidesToScroll: 1,
        responsive: [
            {
                breakpoint: 1200,
                settings: {
                    slidesToShow: 3
                }
            },
            {
                breakpoint: 991,
                settings: {
                    slidesToShow: 2
                }
            },
            {
                breakpoint: 600,
                settings: {
                    slidesToShow: 1
                }
            }
        ]
    });
    $('.post-thumbnail-slide').slick({
        dots: false,
        arrows: true,
        infinite: true,
        autoplay: true,
        Speed: 500,
        prevArrow: '<div class="prev"><i class="fas fa-arrow-left"></i></div>',
        nextArrow: '<div class="next"><i class="fas fa-arrow-right"></i></div>',
        slidesToShow: 1,
        slidesToScroll: 1
    });
    $('.testimonial-slider-one').slick({
        dots: false,
        arrows: false,
        infinite: true,
        autoplay: true,
        Speed: 500,
        slidesToShow: 3,
        slidesToScroll: 1,
        responsive: [
            {
                breakpoint: 1200,
                settings: {
                    slidesToShow: 2
                }
            },
            {
                breakpoint: 768,
                settings: {
                    slidesToShow: 1
                }
            },
            {
                breakpoint: 480,
                settings: {
                    slidesToShow: 1
                }
            }
        ]
    });
    var slideDots = $('.testimonial-dots-images');
    $('.testimonial-slider-two').slick({
        dots: true,
        arrows: false,
        autoplay: true,
        Speed: 500,
        slidesToShow: 1,
        slidesToScroll: 1,
        appendDots: slideDots,
        customPaging: function (slick, index) {
            var portrait = $(slick.$slides[index]).data('thumb');
            return '<img src=" ' + portrait + ' "/>';
        },
        responsive: [
            {
                breakpoint: 1180,
                settings: {
                    dots: false,
                }
            },
            {
                breakpoint: 480,
                settings: {
                    dots: false,
                }
            }
        ]
    });
    $('.sponsor-slide-one').slick({
        dots: false,
        arrows: false,
        infinite: true,
        autoplay: true,
        speed: 1000,
        slidesToShow: 5,
        slidesToScroll: 1,
        responsive: [
            {
                breakpoint: 1024,
                settings: {
                    slidesToShow: 3
                }
            },
            {
                breakpoint: 768,
                settings: {
                    slidesToShow: 2
                }
            }
        ]
    });
    $('.shop-big-slider').slick({
		dots: false,
		arrows: false,
		infinite: true,
		autoplaySpeed: 1500,
		asNavFor: '.shop-thumb-slider',
        fade: true,
		slidesToShow: 1,
		slidesToScroll: 1,
        responsive: [
            {
                breakpoint: 768,
                settings: {
                    arrows: false
                }
            }
        ]
    });
    $('.shop-thumb-slider').slick({
		dots: false,
		arrows: false,
		autoplaySpeed: 1500,
		focusOnSelect: true,
        vertical: true,
		asNavFor: '.shop-big-slider',
		slidesToShow: 4,
		slidesToScroll: 1,
        responsive: [
            {
                breakpoint: 1200,
                settings: {
                    vertical: false
                }
            }
        ]
    });
    // Isotpe js
    $('#masonry-portfolio').imagesLoaded( function() {
        // items on button click
        $('.filter-btn').on('click', 'li', function () {
            var filterValue = $(this).attr('data-filter');
            $grid.isotope({
                filter: filterValue
            });
        });
        // menu active class
        $('.filter-btn li').on('click', function (e) {
            $(this).siblings('.active').removeClass('active');
            $(this).addClass('active');
            e.preventDefault();
        });
        var $grid = $('.masonry-row').isotope({
            itemSelector: '.product-column',
            percentPosition: true,
            masonry: {
                columnWidth: 1
            }
        });
    });

    // nice number
    $('input[type="number"]').niceNumber({
        buttonDecrement:'<i class="fas fa-minus"></i>',
        buttonIncrement:'<i class="fas fa-plus"></i>'
    });

    // Price ranger
    $( "#slider-range" ).slider({
        range: true,
        min: 0,
        max: 90,
        values: [ 0, 90 ],
        slide: function( event, ui ) {
          $( "#amount" ).val( "$" + ui.values[ 0 ] + " - $" + ui.values[ 1 ] );
        }
    });
    $( "#amount" ).val( "$" + $( "#slider-range" ).slider( "values", 0 ) +
        " - $" + $( "#slider-range" ).slider( "values", 1 ) );
        
    //wow js init
    new WOW().init();
});