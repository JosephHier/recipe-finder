$(function() {
  var label = false;
  Dropzone.options.filedrop = {
    init: function() {
      this.on("success", function(file, res) {
        label = res;

        var uppercaseLabel = res.charAt(0).toUpperCase() + res.slice(1)
        $(".dz-size").last().html("<b>" + uppercaseLabel + "</b>");
        $(".dz-filename").remove();
      });
    }
  };

  $("#submit-btn").on("click", function() {
    if (label) {
      var mealType = $('input[name="mealType"]:checked').val();
      window.location.href = '/recipes/' + label + '/' + mealType;
    }
  });
});
