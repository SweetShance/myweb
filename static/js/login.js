function showhidediv(id){
    var sbtitle=document.getElementById(id);
    var js_login = document.getElementById('login')
    var js_registered = document.getElementById('registered')
    if(sbtitle){
        if(sbtitle.style.display=='block'){
        sbtitle.style.display='none';
        }else{
        sbtitle.style.display='block';
          if(id=='registered'){
            js_login.style.display='none';
          }
          if(id=='login'){
              js_registered.style.display='none';
          } 
        }
    }
  }
  　//paraName 等找参数的名称
　　function GetUrlParam(paraName) {
　　　　var url = document.location.toString();
　　　　var arrObj = url.split("?");
　　　　if (arrObj.length > 1) {
　　　　　　var arrPara = arrObj[1].split("&");
　　　　　　var arr;
　　　　　　for (var i = 0; i < arrPara.length; i++) {
　　　　　　　　arr = arrPara[i].split("=");
　　　　　　　　if (arr != null && arr[0] == paraName) {
　　　　　　　　　　return arr[1];
　　　　　　　　}
　　　　　　}
　　　　　　return "";
　　　　}
　　　　else {
　　　　　　return "";
　　　　}
　　}
    var customerId=document.cookie; 
    
    var a = 0
   for(var i = 0; i < customerId.split(';').length; i++){
      if(customerId.split(';')[i] == 'login=True'){
        a++
      }
      
      if(customerId.split(';')[i].replace(/(^\s*)|(\s*$)/g, "") == 'login=logout'){
        a++
      }
   }
    var test = customerId.split(';')[1];
　　if(GetUrlParam("form")=="login" && a==0){
    $('#exampleModalCenter').modal('show')
    }
    if(GetUrlParam("form")=="register" && a==0){
        $('#exampleModalCenter').modal('show')
        var js_login = document.getElementById('login')
        var js_registered = document.getElementById('registered')
        js_login.style.display='none'
        js_registered.style.display='block'
    }
  