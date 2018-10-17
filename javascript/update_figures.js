// Figure 1 interactively loads static images, stored locally
function update_figure_1() {
  var options = ['interferometer.png',
                 'interferometer_x_is_one.png',
                 'interferometer_a_is_zero.png',
                 'interferometer_b_is_zero.png']
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
  var options = ['positive_phase_contrast/animation.gif',
                 'negative_phase_contrast/animation.gif']
  for (var i = 0; i < 2; i++) {
    var radio_button = document.getElementById(options[i]);
    if (radio_button.checked) {
      var filename = "./images/animations/" + options[i];
    }
  }
  var image = document.getElementById("Figure_3_vid");
  image.src = filename;
}
