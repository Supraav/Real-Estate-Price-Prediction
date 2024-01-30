const radioBtns = document.querySelectorAll('input[name="underground"]');
   const livingsize = document.getElementsByName("livingsize")[0];
   const landsize= document.getElementsByName("landsize")[0];
    // const option = document.getElementsByName("underground");
    const basementsize = document.getElementsByName("basementsize")[0];

    radioBtns.forEach(function(underground) {
      underground.addEventListener('click', function() {
        if (underground.id === "radio_4") {
          basementsize.value=0;
        basementsize.readOnly=true;
      }
      else{
         basementsize.readOnly=false;
      }
      });
    });

    function checkvalue(){
      var field1 = document.getElementById("livingsize").value;
      var field2= document.getElementById("landsize").value;
      
      if (field1>field2){
        alert("Living size should be less than landsize");
        document.getElementById("livingsize").value='';

      }
      
    }
    function funcscrolled(){
      document.getElementById("scrolltime").scrollIntoView();
    }