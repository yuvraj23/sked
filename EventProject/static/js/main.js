$(document).ready(function(){

  $nave = $('.nave');

  $toggleCollapse= $('.toggle-collapse');
  /*click event on togle*/
  $toggleCollapse.click(function(){
    $nave.toggleClass('collapse');

  })


});
