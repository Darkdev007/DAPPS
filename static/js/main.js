const tabItems = document.querySelectorAll('.tab-item');
const tabContentItems = document.querySelectorAll('.tab-content-item');

function selectItem(e) {
    removeShow();
    this.classList.add('tab-item');
    const tabContentItem = document.querySelector(`#${this.id}-content`);
    tabContentItem.classList.add('show');
}

function removeShow() {
    tabContentItems.forEach(item => item.classList.remove('show',))
}
tabItems.forEach(item => item.addEventListener('click', selectItem))


function load() {
    document.getElementById("loader").classList.add("active");
    setTimeout(function(){
      document.getElementById("loader").classList.remove("active");
    },3000);
  };

  window.onload = function(){
    var theDelay = 5;
    var timer = setTimeout("showText()",theDelay*1000)
  }
  function showText(){
    document.getElementById("delayedText").style.visibility = "visible";
  }

// setTimeout(function(){
//     document.getElementById('showMeAfter3seconds').classList.remove('hide-me');
// },5000);
// $(document).ready(function(){
//     setTimeout(function(){
//         $(".hide-me").show();
//     }, 3000);
// });

