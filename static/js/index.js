   const livingsize = document.getElementsByName("livingsize")[0];
    const option = document.getElementById("underground");
    const basementsize = document.getElementsByName("basementsize")[0];

    option.addEventListener("change", function () {   
      //no 
      if (option.value === "0") {

        basementsize.value=0;
        basementsize.readOnly=true;
      }
      else{
         basementsize.readOnly=false;
      }
      //yes
    });