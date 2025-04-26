function decode(str){
    var CryptoJS = require("crypto-js");
    var KEY = 'aiding6666666666';
    var key = CryptoJS.enc.Utf8.parse(KEY);
    var decrypted = CryptoJS.AES.decrypt(str, key, {
                   // iv: iv,
                   mode: CryptoJS.mode.ECB,
                   padding: CryptoJS.pad.Pkcs7,
    });
    return decrypted.toString(CryptoJS.enc.Utf8)
}

