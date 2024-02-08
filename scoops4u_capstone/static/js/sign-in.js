$(document).ready(function () {

    $('#password').keyup(function() {
        // If value is not empty
        if ($(this).val().length == 0) {
          // Hide the element
          $('#eye').hide();
          $('#eye').addClass('d-none');
          
        } else {
          // Otherwise show it
            $('#eye').show();
            $('#eye').removeClass('d-none');
        }
      }).keyup();

    $('#eye').click(function(){
    
    if($(this).hasClass("ri-eye-fill")){
        
        $(this).removeClass("ri-eye-fill");
        
        $(this).addClass("ri-eye-off-fill");
        
        $('#password').attr('type','text');
        
    }else{
        
        $(this).removeClass("ri-eye-off-fill");
        
        $(this).addClass("ri-eye-fill");  
        
        $('#password').attr('type','password');
    }
    });
});
