#' pal_klee
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
#' pal_klee()(10)
#' pal_klee(alpha = 0.5)(10)
#' pal_klee(alpha = 0.5, reverse = TRUE)(20)
pal_klee = function(alpha = 1, reverse = FALSE) {
	pal <- c("#C1351D", "#F6E1C6", "#C08270", "#875648", "#421F1A")
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

#' rgb_klee
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
#' rgb_klee()
#' rgb_klee(10)
#' rgb_klee(n = 10, alpha = 0.5)
#' rgb_klee(n = 20, alpha = 0.7, reverse = TRUE)
rgb_klee = function(n = 12, alpha = 1, reverse = FALSE){
	return(pal_klee(alpha = alpha, reverse = reverse)(n))
}

#' scale_color_klee
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
#' scale_color_klee()
#' scale_color_klee(FALSE)
#' scale_color_klee(alpha = 0.5)
#' scale_color_klee(FALSE, alpha = 0.7, reverse = TRUE)
scale_color_klee = function(discrete = TRUE, alpha = 1, reverse = FALSE, ...) {
	if(discrete){
		return(discrete_scale("colour", "klee", pal_klee(alpha = alpha, reverse = reverse), ...))
	}
	else{
		return(scale_color_gradientn(colours = rgb_klee(n = 512, alpha = alpha, reverse = reverse), ...))
	}
}

#' scale_colour_klee
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
#' scale_colour_klee()
#' scale_colour_klee(FALSE)
#' scale_colour_klee(alpha = 0.5)
#' scale_colour_klee(FALSE, alpha = 0.7, reverse = TRUE)
scale_colour_klee = scale_color_klee

#' scale_fill_klee
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
#' scale_fill_klee()
#' scale_fill_klee(FALSE)
#' scale_fill_klee(alpha = 0.5)
#' scale_fill_klee(FALSE, alpha = 0.7, reverse = TRUE)
scale_fill_klee = function(discrete = TRUE, alpha = 1, reverse = FALSE, ...) {
	if(discrete){
		return(discrete_scale("fill", "klee", pal_klee(alpha = alpha, reverse = reverse), ...))
	}
	else{
		return(scale_fill_gradientn(colours = rgb_klee(n = 512, alpha = alpha, reverse = reverse), ...))
	}
}
