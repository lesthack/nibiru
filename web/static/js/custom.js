function show_hide_pass(obj){
    var id = obj.parentElement.getAttribute('data-id');
    var eye_pass = document.getElementById('eye-' + id);
    var pass = document.getElementById(id);

    if(pass.className=='password-value hide'){
        pass.className='password-value show';
        pass.value = obj.parentElement.getAttribute('data-value');
        eye_pass.className = 'fa fa-eye-slash';        
    }
    else{
        pass.className='password-value hide';
        pass.value = '******';
        eye_pass.className = 'fa fa-eye';
    }
}

function copy2clipboard(obj){
    if(obj.className=='password-value show'){
        obj.select();
        try {
          var successful = document.execCommand('copy');
          var msg = successful ? 'successful' : 'unsuccessful';
          console.log('Copying text command was ' + msg);
        } catch (err) {
          console.log('Oops, unable to copy');
        }
    }
}

document.addEventListener('DOMContentLoaded', function () {
  if (!Notification) {
    console.log('Desktop notifications not available in your browser. Try Chromium.'); 
    return;
  }

  if (Notification.permission !== "granted")
    Notification.requestPermission();
});
