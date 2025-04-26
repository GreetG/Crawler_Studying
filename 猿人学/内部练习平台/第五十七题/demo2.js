CryptoJS = require("crypto-js")
function get_result(result) {

    res2 = result.slice(8)
    res1 = result.slice(0,8)
    C = res1
    q = CryptoJS.enc.Utf8.parse(C)
    v = CryptoJS.DES.decrypt(
       res2 , q, {
            'mode': CryptoJS.mode.ECB,
            'padding': CryptoJS.pad.Pkcs7
        })
    return v.toString(CryptoJS.enc.Utf8)
}



