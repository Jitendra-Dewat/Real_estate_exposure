function checkName(){
    var name=document.getElementById("name").value;
   // console.log(x);
    var namecheck=/^[A-Za-z. ]{3,30}$/;
    if(namecheck.test(name)){
        document.getElementById("nerror").innerHTML="";
    }else{
        document.getElementById("nerror").innerHTML="** Invlaid Name field";
        document.getElementById("name").value="";
        document.getElementById("name").focus();
    }
}


function checkPhone(){
    var phone=document.getElementById("phone").value;
    //console.log(x);
    var phonecheck = /^[789]{1}[0-9]{9}$/;
    //console.log(phonecheck.test(x));
    if(phonecheck.test(phone)){
        document.getElementById("perror").innerHTML="";
    }else{
        document.getElementById("perror").innerHTML="** invalid phone number";
        document.getElementById("phone").value="";
        document.getElementById("phone").focus();
    }
}


function checkAdhar(){
    var adhar=document.getElementById("adhar").value;
    console.log(adhar);
    var adharcheck = /^[0-9]{13}$/;
    console.log(adharcheck.test(adhar));
    if(adharcheck.test(adhar)){
        document.getElementById("aderror").innerHTML="";
    }else{
        document.getElementById("aderror").innerHTML="** invalid adhar number";
        document.getElementById("adhar").value="";
        document.getElementById("adhar").focus();
    }
}


function checkAddress(){
    var address=document.getElementById("address").value;
    console.log(address);
    var addresscheck = /^[a-zA-Z0-9\s,'-]{3,}$/;
    console.log(addresscheck.test(address));
    if(addresscheck.test(address)){
        document.getElementById("aerror").innerHTML="";
    }else{
        document.getElementById("aerror").innerHTML="** invalid address";
        document.getElementById("address").value="";
        document.getElementById("address").focus();
    }
}


function checkEmail(){
    var email=document.getElementById("email").value;
    console.log(email);
    var emailcheck = /^[A-Za-z._0-9]{3,}@[A-Za-z]{3,}[.]{1}[A-Za-z.]{2,6}$/;
    //console.log(emailcheck);
    console.log(emailcheck.test(email));
    if(emailcheck.test(email)){
        document.getElementById("eerror").innerHTML="";
    }else{
        document.getElementById("eerror").innerHTML="** invalid email";
        document.getElementById("email").value="";
        document.getElementById("email").focus();
    }
}


function checkPassword(){
    var pass=document.getElementById("pass").value;
    console.log(pass);
    var passcheck = /^(?=.*[A-Z])(?=.*[a-z])(?=.*[0-9])(?=.*[!@#$%^&*])[a-zA-Z0-9!@#$%^&*]{8,16}$/;
    //console.log(emailcheck);
    console.log(passcheck.test(pass));
    if(passcheck.test(pass)){
        document.getElementById("paerror").innerHTML="";
    }else{
        document.getElementById("paerror").innerHTML="** invalid password! password must be 8+ and one A-Z, a-z, 0-9, and special character!";
        document.getElementById("pass").value="";
        document.getElementById("pass").focus();
    }
}



/*function checkAddress(){
    var address=document.getElementById("address").value;
    console.log(address);
    var addresscheck = /^[a-zA-Z0-9 , .'-/]{3,}$/;
    console.log(addresscheck.test(address));
    if(addresscheck.test(address)){
        document.getElementById("aerror").innerHTML="";
    }else{
        document.getElementById("aerror").innerHTML="** invalid Address";
        document.getElementById("address").value="";
        document.getElementById("address").focus();
    }
}
*/

function checkBlood(){
    var blood=document.getElementById("blood").value;
    //console.log(x);
    var bloodcheck = /^[oOaAbB]{1,2}[+-]{1}$/;
    //console.log(addresscheck.test(address));
    if(bloodcheck.test(blood)){
        document.getElementById("berror").innerHTML="";
    }else{
        document.getElementById("berror").innerHTML="** invalid Address";
        document.getElementById("blood").value="";
        document.getElementById("blood").focus();
    }
}


function checkRollNo(){
    var id=document.getElementById("id").value;
    console.log(id);
    var idcheck = /^[bBmMpP]{1}[0-9]{6}[a-zA-Z]{2}$/;
    console.log(idcheck.test(id));
    if(idcheck.test(id)){
        document.getElementById("ierror").innerHTML="";
    }else{
        document.getElementById("ierror").innerHTML="** invalid College Id";
        document.getElementById("id").value="";
        document.getElementById("id").focus();
    }
}





/*var emailcheck = /^[A-Za-z._]{3,}@[A-Za-z]{3,}[.]{1}[A-Za-z.]{2,6}$/;
            var namecheck = /^[A-Za-z. ]{3,30}$/;
            var passcheck = /^(?=.*[0-9])(?=.*[!@#$%^&*])[a-zA-Z0-9!@#$%^&*]{8,16}$/
            var phonecheck = /^[789][0-9]{9}$/;
            var idcheck = /^[bBmMpP]{1}[0-9]{6}[a-zA-Z]{2}$/;
            var bloddcheck = /^[oOaAbB]{1,2}[+-]{1}$/;
            var addresscheck = /^[a-zA-Z0-9\s,'-]$/;*/





