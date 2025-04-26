const CryptoJS = require("crypto-js");

const crypto = require("crypto");
function md5ToBigEndianWords(data) {
    // 1. 计算 MD5 哈希（返回 Buffer）
    const md5 = crypto.createHash("md5").update(data).digest();

    // 2. 使用 DataView 按大端序读取 4 个 int32
    const view = new DataView(md5.buffer);
    const words = [
        view.getInt32(0, false),  // 大端序 (false)
        view.getInt32(4, false),
        view.getInt32(8, false),
        view.getInt32(12, false),
    ];

    return { words, sigBytes: 16 };
}


function p_stringify(result){
    r = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/="
    n = result.sigBytes
    e = result.words
    for (var o = [], i = 0; i < n; i += 3)
                        for (var a = (e[i >>> 2] >>> 24 - i % 4 * 8 & 255) << 16 | (e[i + 1 >>> 2] >>> 24 - (i + 1) % 4 * 8 & 255) << 8 | e[i + 2 >>> 2] >>> 24 - (i + 2) % 4 * 8 & 255, u = 0; u < 4 && i + .75 * u < n; u++)
                            o.push(r.charAt(a >>> 6 * (3 - u) & 63));
    var c = r.charAt(64);
    if (c)
        for (; o.length % 4; )
            o.push(c);
    return o.join("")
}
function get_f(data_){
    const key = "8eMrcmkiElSWiwCSrQrSSfAlG11rLHz1"; // n
    var s =data_
    // 计算 HMAC-SHA256
    const hmac = CryptoJS.HmacSHA256(s, key);
    // 转换为 words + sigBytes 格式
    const words = hmac.words; // 8个 int32
    const sigBytes = hmac.sigBytes; // 32
    return { words, sigBytes }
}
function get_header(){
    const data = '___jscode___'
    const result = md5ToBigEndianWords(data);
    var am_sign_time = Math.floor(Date.now() / 1e3)
    var am_sign_version = "v1"
    digest=p_stringify(result)
    c = []
    c.push("POST /api/v2/direct-trackings/batch track.aftership.com")
    c.push("am-sign-time: ".concat(am_sign_time))
    c.push("am-sign-version: v1")
    c.push("digest: ".concat(digest))
    var s = `POST /api/v2/direct-trackings/batch track.aftership.com\nam-sign-time: ${am_sign_time}\nam-sign-version: v1\ndigest: ${digest}`;
    var signature = p_stringify(get_f(s))

    return [signature,am_sign_time,digest]
}

