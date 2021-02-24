$(document).on('submit','#beginnerhtmlform',function(e){
    e.preventDefault();
    $.ajax({
      type:'POST',
      url:'/user/createportfolio/beginner/',
      data:{
        bskill:$('#bskill').val(),
        csrfmiddlewaretoken:$('input[name=csrfmiddlewaretoken]').val()
      },
      success:function(response){
        if (response['skill']){
          $('#beginnerhtmlform').trigger('reset');
          swal("Skill Already Added","Unable to save your Skill","warning");
        }
        else{
          $('#beginnerhtmlform').trigger('reset');
          window.location='http://127.0.0.1:8000/user/createportfolio/'
        }
      },
      statusCode:{
          500:function(){
            $('#bskill').trigger('reset');
            swal("Error Occurred","Unable to save your Skill","warning");
          }
      },
    });
  });
$(document).on('submit','#intermiddatehtmlform',function(e){
    e.preventDefault();
    $.ajax({
      type:'POST',
      url:'/user/createportfolio/intermiddate/',
      data:{
        iskill:$('#iskill').val(),
        csrfmiddlewaretoken:$('input[name=csrfmiddlewaretoken]').val()
      },
      success:function(response){
        if (response['skill']){
          $('#intermiddatehtmlform').trigger('reset');
          swal("Skill Already Added","Unable to save your Skill","warning");
        }
        else{
          $('#intermiddaterhtmlform').trigger('reset');
          window.location='http://127.0.0.1:8000/user/createportfolio/'
        }
      },
      statusCode:{
          500:function(){
            $('#iskill').trigger('reset');
            swal("Error Occurred","Unable to save your Skill","warning");
          }
      },
    });
  });
$(document).on('submit','#advancehtmlform',function(e){
    e.preventDefault();
    $.ajax({
      type:'POST',
      url:'/user/createportfolio/advanced/',
      data:{
        askill:$('#askill').val(),
        csrfmiddlewaretoken:$('input[name=csrfmiddlewaretoken]').val()
      },
      success:function(response){
        if (response['skill']){
          $('#advancehtmlform').trigger('reset');
          swal("Skill Already Added","Unable to save your Skill","warning");
        }
        else{
          $('#advancehtmlform').trigger('reset');
          window.location='http://127.0.0.1:8000/user/createportfolio/'
        }
      },
      statusCode:{
          500:function(){
            $('#askill').trigger('reset');
            swal("Error Occurred","Unable to save your Skill","warning");
          }
      },
    });
  });
//$(document).on('submit','#portfolioproject',function(e){
  //  e.preventDefault();
    //$.ajax({
      //type:'POST',
      //url:'/user/createportfolio/portfoliop/',
      //data:{
        //pname:$('#pname').val(),
        //purl:$('#purl').val(),
        //pdesp:$('#pdesp').val(),
        //pimage:$('#fileElem').val(),
        //csrfmiddlewaretoken:$('input[name=csrfmiddlewaretoken]').val()
      //},
      //success:function(response){
       // console.log(response);
      //  $('#portfolioproject').trigger('reset');
       // window.location='http://127.0.0.1:8000/user/createportfolio/'
      //},
      //statusCode:{
        //  500:function(){
          //  $('#pdesp').trigger('reset');
            //swal("Error Occurred","Unable to save your Skill","warning");
          //}
   //   },
     // statusCode:{
       //   300:function(){
         //   $('#pdesp').trigger('reset');
           // swal("Error Occurred","Unable to save your Skill","warning");
        //  }
      //},
      //statusCode:{
        //  404:function(){
          //  $('#pdesp').trigger('reset');
            //swal("Error Occurred","Unable to save your Skill","warning");
          //}
    //  },
    //});
  //});

  $(window).on('scroll', function(event) {
    if($(this).scrollTop() > 40){
        $('.back-to-top2').fadeIn(200)
    } else{
        $('.back-to-top2').fadeOut(200)
    }
});

 
