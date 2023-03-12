#' pal_ayaka
#'
#' Mimicking the pal_XXX function in the ggsci package, it returns a vector of hexadecimal colors.
#'
#' @param alpha the alpha value of each color
#' @param reverse invert the color sequence
#'
#' @importFrom grDevices col2rgb rgb
#'
#' @return a vector of hexadecimal colors
#' @export
#'
#' @examples
#' pal_ayaka()(10)
#' pal_ayaka(alpha = 0.5)(10)
#' pal_ayaka(alpha = 0.5, reverse = TRUE)(20)
pal_ayaka = function(alpha = 1, reverse = FALSE) {
	pal <- c("#222449", "#414C87", "#9CB3D4", "#ECEDEB", "#AF5A76")
	pal_rgb = col2rgb(pal)
	return(function(x){
		vec = 1:x
		if(reverse){
			vec = rev(vec)
		}
		return(sapply(vec, function(y){
			len = length(pal)
			pos = y / x * len
			pos = ifelse(pos < 1, 1, ifelse(pos > len, len, pos))
			rgb = pal_rgb[, floor(pos)] + (pal_rgb[, ceiling(pos)] - pal_rgb[, floor(pos)]) * (pos - floor(pos))
			rgb = rgb / 255
			return(rgb(rgb[1], rgb[2], rgb[3], alpha))
		}))
	})
}

#' rgb_ayaka
#'
#' Mimicking the rgb_XXX function in the ggsci package, it returns a vector of hexadecimal colors.
#'
#' @param n the number of colors generated
#' @param alpha the alpha value of each color
#' @param reverse invert the color sequence
#'
#' @return a vector of hexadecimal colors
#' @export
#'
#' @examples
#' rgb_ayaka()
#' rgb_ayaka(10)
#' rgb_ayaka(n = 10, alpha = 0.5)
#' rgb_ayaka(n = 20, alpha = 0.7, reverse = TRUE)
rgb_ayaka = function(n = 12, alpha = 1, reverse = FALSE){
	return(pal_ayaka(alpha = alpha, reverse = reverse)(n))
}

#' scale_color_ayaka
#'
#' Mimicking the scale_color_XXX function, it returns a ggplot color scale
#'
#' @param discrete if true, returns a discrete palette; if false, returns a continuous color palette.
#' @param alpha the alpha value of each color
#' @param reverse invert the color sequence
#' @param ... passed to the discrete_scale or scale_color_gradientn
#'
#' @importFrom ggplot2 discrete_scale scale_color_gradientn
#'
#' @return a ggplot color scale
#' @export
#'
#' @examples
#' scale_color_ayaka()
#' scale_color_ayaka(FALSE)
#' scale_color_ayaka(alpha = 0.5)
#' scale_color_ayaka(FALSE, alpha = 0.7, reverse = TRUE)
scale_color_ayaka = function(discrete = TRUE, alpha = 1, reverse = FALSE, ...) {
	if(discrete){
		return(discrete_scale("colour", "ayaka", pal_ayaka(alpha = alpha, reverse = reverse), ...))
	}
	else{
		return(scale_color_gradientn(colours = rgb_ayaka(n = 512, alpha = alpha, reverse = reverse), ...))
	}
}

#' scale_colour_ayaka
#'
#' Mimicking the scale_colour_XXX function, it returns a ggplot colour scale
#'
#' @param discrete if true, returns a discrete palette; if false, returns a continuous colour palette.
#' @param alpha the alpha value of each colour
#' @param reverse invert the colour sequence
#' @param ... passed to the discrete_scale or scale_color_gradientn
#'
#' @return a ggplot colour scale
#' @export
#'
#' @examples
#' scale_colour_ayaka()
#' scale_colour_ayaka(FALSE)
#' scale_colour_ayaka(alpha = 0.5)
#' scale_colour_ayaka(FALSE, alpha = 0.7, reverse = TRUE)
scale_colour_ayaka = scale_color_ayaka

#' scale_fill_ayaka
#'
#' Mimicking the scale_fill_XXX function, it returns a ggplot color scale
#'
#' @param discrete if true, returns a discrete palette; if false, returns a continuous color palette.
#' @param alpha the alpha value of each color
#' @param reverse invert the color sequence
#' @param ... passed to the discrete_scale or scale_fill_gradientn
#'
#' @importFrom ggplot2 discrete_scale scale_fill_gradientn
#'
#' @return a ggplot color scale
#' @export
#'
#' @examples
#' scale_fill_ayaka()
#' scale_fill_ayaka(FALSE)
#' scale_fill_ayaka(alpha = 0.5)
#' scale_fill_ayaka(FALSE, alpha = 0.7, reverse = TRUE)
scale_fill_ayaka = function(discrete = TRUE, alpha = 1, reverse = FALSE, ...) {
	if(discrete){
		return(discrete_scale("fill", "ayaka", pal_ayaka(alpha = alpha, reverse = reverse), ...))
	}
	else{
		return(scale_fill_gradientn(colours = rgb_ayaka(n = 512, alpha = alpha, reverse = reverse), ...))
	}
}
