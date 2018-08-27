// Figure 1 interactively loads static images, stored locally
function update_figure_1() {
  var options = ['interferometer_1.svg',
                 'interferometer_2.svg',
                 'interferometer_3.svg',
                 'interferometer_4.svg']
  for (var i = 0; i < 4; i++) {
    var radio_button = document.getElementById(options[i]);
    if (radio_button.checked) {
      var filename = "./images/interferometer/" + options[i];
    }
  }
  var image = document.getElementById("Figure_1_image");
  image.src = filename;
}
