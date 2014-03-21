
var ww = document.body.clientWidth;

$(document).ready(function() {
	$("#portal-responsive-globalnav li a").each(function() {
		if ($(this).next().length > 0) {
			$(this).addClass("parent");
		};
	})

	$(".toggleMenu").click(function(e) {
		e.preventDefault();
		$(this).toggleClass("active");
		$("#portal-responsive-globalnav").toggle();
	});
	adjustMenu();
})

$(window).bind('resize orientationchange', function() {
	ww = document.body.clientWidth;
	adjustMenu();
});

var adjustMenu = function() {
	if (ww < (60 * getComputedStyle(document.body,null).fontSize.replace(/[^\d]/g, ''))) {
		$(".toggleMenu").css("display", "inline-block");
		if (!$(".toggleMenu").hasClass("active")) {
			$("#portal-responsive-globalnav").hide();
		} else {
			$("#portal-responsive-globalnav").show();
		}
		$("#portal-responsive-globalnav li").unbind('mouseenter mouseleave');
		$("#portal-responsive-globalnav li a.parent").unbind('click').bind('click', function(e) {
			// must be attached to anchor element to prevent bubbling
			e.preventDefault();
			$(this).parent("li").toggleClass("hover");
		});
	}
	else if (ww >= (60 * getComputedStyle(document.body,null).fontSize.replace(/[^\d]/g, ''))) {
		$(".toggleMenu").css("display", "none");
		$("#portal-responsive-globalnav").show();
		$("#portal-responsive-globalnav li").removeClass("hover");
		$("#portal-responsive-globalnav li a").unbind('click');
		$("#portal-responsive-globalnav li").unbind('mouseenter mouseleave').bind('mouseenter mouseleave', function() {
		 	// must be attached to li so that mouseleave is not triggered when hover over submenu
		 	$(this).toggleClass('hover');
		});
	}
}

