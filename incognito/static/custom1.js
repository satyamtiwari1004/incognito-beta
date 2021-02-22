$(document).on('submit','#loginform',function(e){
    e.preventDefault();
    $.ajax({
      type:'POST',
      url:'/accounts/verifyuser/',
      
      data:{
        loginusername:$('#loginusername').val(),
        loginpassword:$('#loginpassword').val(),
        next1:$('#next1').val(),
        csrfmiddlewaretoken:$('input[name=csrfmiddlewaretoken]').val()
      },
      success:function(response){
        if(response['userexists']){
          $('#loginusername').trigger('reset');
          swal("Invalid Credentials ","Username and Password didn't Matched","warning");}
        else{
          $('#loginform').trigger('reset');
          window.location=response['urlre'];
        }
        
      },
      statusCode:{
          500:function(){
            $('#loginpassword').trigger('reset');
            swal("Invalid Credentials ","Username and Password didn't Matched","warning");
          }
      },
    });
  });
$(document).on('submit','#registerform',function(e){
    e.preventDefault();
    $.ajax({
      type:'POST',
      url:'/accounts/createaccount/',
      
      data:{
        username:$('#username').val(),
        email:$('#email').val(),
        password:$('#password').val(),
        confirmpassword:$('#confirmpassword').val(),
        csrfmiddlewaretoken:$('input[name=csrfmiddlewaretoken]').val()
      },
      success:function(response){
        if(response['email']){
        $('#registerform').trigger('reset');
        swal("Verification Mail Sent ","Account Verification Mail Has been sent.","success");}
        if(response['sqliteerror']){
        $('#username').trigger('reset');
        swal("Username not available","Kindly choose another username because a user with this username already Exists.","warning");}
        if(response['eemail']){
          $('#email').trigger('reset');
          swal("Email Already Exists","In case if you have forgotten your password or username,Kindly goto Forgot Password Page.","warning");}
          if(response['perror']){
            $('#password').trigger('reset');
            swal("Password Didn't Match.","Password should not be same as Username. Password should contain alphabets, numbers and also have minimum length of 8.","warning");}
      },
      statusCode:{
          500:function(){
            
            swal("Oops ","Something went wrong.","error");
          }
      },
    });
  
  
  
  });

  
//const passwordtoggle=document.getElementById('loginpassword');
//const ptoggle=document.getElementById('toggle');
//function showHide(){
  //if (passwordtoggle.type ==='password'){
    //passwordtoggle.setAttribute('type','text');
    //toggle.classList.add('hide')
  //}
  //else{
    //passwordtoggle.setAttribute('type','text');
    //toggle.classList.remove('hide')
  //}
//}

//var span = document.getElementsByClassName("close")[0];


$(window).on('load',function(){
  
  
  $('.pgbar').fadeOut(1000)

 
}



);