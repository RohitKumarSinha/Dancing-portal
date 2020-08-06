$(function () {
  "use strict";

  var body = $("#wrapper");

  function goToNextInput(e) {
    var key = e.which,
      t = $(e.target),
      sib = t.next("#wrapper #dialog input");

    if (key != 9 && (key < 48 || key > 57)) {
      e.preventDefault();
      return false;
    }

    if (key === 9) {
      return true;
    }

    if (!sib || !sib.length) {
      sib = body.find("input").eq(0);
    }
    sib.select().focus();
  }

  function onKeyDown(e) {
    var key = e.which;

    if (key === 9 || (key >= 48 && key <= 57)) {
      return true;
    }

    e.preventDefault();
    return false;
  }

  function onFocus(e) {
    $(e.target).select();
  }

  body.on("keyup", "input", goToNextInput);
  body.on("keydown", "input", onKeyDown);
  body.on("click", "input", onFocus);
});

loadEventListeners();

// Load all event listeners
function loadEventListeners() {
  // Filter tasks event
  document.getElementById("wrapper").style.display = "none";
  document.getElementById("wrapper1").style.display = "block";
}

// Store Task
function storeTaskInLocalStorage(task) {
  let tasks;
  if (localStorage.getItem("tasks") === null) {
    tasks = [];
  } else {
    tasks = JSON.parse(localStorage.getItem("tasks"));
  }

  tasks.push(task);

  localStorage.setItem("tasks", JSON.stringify(tasks));
  return;
}

function reverse() {
  localStorage.clear();
  inputtxt = document.getElementById("input1").value;

  var phoneno = /^\d{10}$/;
  if (inputtxt.match(phoneno)) {
    const getresponse = new getResponse();
    inputtxt = "91" + inputtxt;
    getresponse.getUser(inputtxt).then((data) => {
      if (data.status == true) {
        // Store in LS
        storeTaskInLocalStorage(inputtxt);
      }
    });
  } else {
    // alert("Not a valid Phone Number");
    $("#test").html("you enter wrong number please try again");
    return false;
  }
  // Filter tasks event
  document.getElementById("wrapper1").style.display = "none";
  document.getElementById("wrapper").style.display = "block";
}

function myFunction() {
  var input, filter, cards, cardContainer, h5, title, i;
  input = document.getElementById("myFilter");
  filter = input.value.toUpperCase();
  cardContainer = document.getElementById("showVideos");
  cards = cardContainer.getElementsByClassName("card");
  for (i = 0; i < cards.length; i++) {
    title = cards[i].querySelector(".card-body span.card-title");
    if (title.innerText.toUpperCase().indexOf(filter) > -1) {
      cards[i].style.display = "";
    } else {
      cards[i].style.display = "none";
    }
  }
}

class getResponse {
  async getUser(inputtxt) {
    console.log(inputtxt);
    const profileResponse = await fetch(
      "http://services.thedirtylaundry.in/v1/otpservice?phone=" + inputtxt
    );

    const profile = await profileResponse.json();

    return profile;
  }
}

// Get Tasks from LS
function getTasks() {
  let tasks;
  if (localStorage.getItem("tasks") === null) {
    tasks = [];
  } else {
    tasks = JSON.parse(localStorage.getItem("tasks"));
  }

  console.log(tasks[0]);
  mobileNum = tasks[0];
  otp1 = document.getElementById("otpOne").value;
  otp2 = document.getElementById("otpTwo").value;
  otp3 = document.getElementById("otpThree").value;
  otp4 = document.getElementById("otpFour").value;

  otp = otp1 + otp2 + otp3 + otp4;

  const getresponse = new getOtp();
  getresponse.getUser(mobileNum, otp).then((data) => {
    if (data.status == false) {
      alert("Not a valid otp");
      $("#test1").html("you enter wrong OTP please try again");
    } else {
      loadEventListeners();
      $(function () {
        $("#modal").modal("toggle");
      });
    }
  });

  console.log(otp);
}

function sendOtp() {
  let tasks;
  if (localStorage.getItem("tasks") === null) {
    tasks = [];
  } else {
    tasks = JSON.parse(localStorage.getItem("tasks"));
  }
  mobileNum = tasks[0];
  const getresponse = new getResponse();
  getresponse.getUser(mobileNum).then((data) => {
    if (data.status == true) {
      alert("Otp is sent");
    }
  });
}

class getOtp {
  async getUser(mobileNum, Otp) {
    const profileResponse = await fetch(
      "http://services.thedirtylaundry.in/v1/otpservice?phone=" +
        mobileNum +
        "&otp=" +
        Otp
    );

    const status = await profileResponse.json();

    return status;
  }
}
