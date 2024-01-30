function showOutput() {
    var bedrooms = document.getElementById("bedrooms").value;
    var bathroom = document.getElementById("bathroom").value;
    var landsize = document.getElementById("landsize").value;
    var livingsize = document.getElementById("livingsize").value;
    var underground = document.getElementById("underground").value;
    var basementsize = document.getElementById("basementsize").value;
    var floors = document.getElementById("floors").value;
    var view = document.getElementById("view").value;
    var renovated = document.getElementById("renovated").value;
    var city = document.getElementById("city").value;

    document.getElementById("outputBedrooms").textContent = bedrooms;
    document.getElementById("outputBathroom").textContent = bathroom;
    document.getElementById("outputLandsize").textContent = landsize;
    ocument.getElementById("outputLivingsize").textContent = livingsize;
    document.getElementById("outputUnderground").textContent = underground;
    document.getElementById("outputBasementsize").textContent = basementsize;
    ocument.getElementById("outputFloors").textContent = floors;
    document.getElementById("outputView").textContent = view;
    document.getElementById("outputRenovated").textContent = renovated;
    document.getElementById("outputCity").textContent = city;

    document.getElementById("output").style.display = "block";
  }