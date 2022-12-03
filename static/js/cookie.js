//添加cookie
function addCookie(name, value, expiresHours) {
    var cookieString = name + "=" + encodeURI(value);
    //判断是否设置过期时间 
    if (expiresHours > 0) {
        var date = new Date();
        date.setTime(date.getTime + expiresHours * 3600 * 1000);
        cookieString = cookieString + "; expires=" + date.toGMTString();
    }
    document.cookie = cookieString;
}
//去除cookie
function removeCookies(cookieList){
    let data = new Date(new Date().getTime() - 24 * 60 * 60 * 1000).toUTCString()
   
        document.cookie = cookieList + '= ;' + 'expires=' + data
        if (document.cookie === "") {
            window.location.replace("login.html")
        }
    
}
//判断cookie，跳转页面
if (document.cookie === "") {
    window.location.replace("login.html")
}

