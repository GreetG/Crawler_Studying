const CryptoJS = require("crypto-js")
function get_crypto_url(page) {
        j = page.toString()
        d = CryptoJS.enc.Utf8.parse("aiding88")
        var D = CryptoJS.DES.encrypt(j, d, {
            'mode': CryptoJS.mode.ECB,
            'padding': CryptoJS.pad.Pkcs7
        })
    return D.toString()
}

