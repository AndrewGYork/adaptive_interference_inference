// Figure 1 interactively loads static images, stored locally
function update_figure_1() {
  var options = ['interferometer.svg',
                 'interferometer_x_is_one.svg',
                 'interferometer_a_is_zero.svg',
                 'interferometer_b_is_zero.svg']
  for (var i = 0; i < 4; i++) {
    var radio_button = document.getElementById(options[i]);
    if (radio_button.checked) {
      var filename = "./images/interferometer/" + options[i];
    }
  }
  var image = document.getElementById("Figure_1_image");
  image.src = filename;
}

// Figure 3 interactively loads static animations, stored locally
function update_figure_3() {
  var options = ['positive_phase_contrast/animation.mp4',
                 'negative_phase_contrast/animation.mp4']
  for (var i = 0; i < 2; i++) {
    var radio_button = document.getElementById(options[i]);
    if (radio_button.checked) {
      var filename = "./images/animations/" + options[i];
    }
  }
  var image = document.getElementById("Figure_3_vid");
  image.src = filename;
}
