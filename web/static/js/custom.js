function show_hide_pass(obj){
    var id = obj.parentElement.getAttribute('data-id');
    var eye_pass = document.getElementById('eye-' + id);
    var pass = document.getElementById(id);

    
    if(pass.className=='hide'){
        pass.className='show';
        pass.textContent = obj.parentElement.getAttribute('data-value');
        eye_pass.className = 'fa fa-eye-slash';        
    }
    else{
        pass.className='hide';
        pass.textContent = '************';
        eye_pass.className = 'fa fa-eye';
    }
}
