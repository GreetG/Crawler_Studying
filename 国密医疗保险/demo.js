
const { JSDOM } = require('jsdom');

const dom = new JSDOM(`<!DOCTYPE html><p>Hello world</p>`);

var CryptoJS = require("crypto-js")
global.window = dom.window;
global.document = dom.window.document;
global.navigator = dom.window.navigator;
global.object = dom.window.object

function i123() {
            var e, t, n, i = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ", r = "0123456789";
            return e = o(6, "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"),
            t = o(1, i),
            n = o(1, r),
            t + n + e;
            function o(e, t) {
                e = e || 32;
                for (var n = "", i = 0; i < e; i++)
                    n += t.charAt(Math.ceil(1e3 * Math.random()) % t.length);
                return n
            }
        }
function get_header(){
var s = Math.ceil((new Date).getTime() / 1e3),
    h = i123(),
    f = s + h + s;
    var w = CryptoJS.SHA256(f).toString();





function Zi(){
    function t(t) {
        return 0 > t ? NaN : 30 >= t ? 0 | Math.random() * (1 << t) : 53 >= t ? (0 | Math.random() * (1 << 30)) + (0 | Math.random() * (1 << t - 30)) * (1 << 30) : NaN
    }
    function e(t, e) {
        for (var n = t.toString(16), r = e - n.length, a = "0"; r > 0; r >>>= 1,
        a += a)
            1 & r && (n = a + n);
        return n
    }
    var ret = function(n) {
        return n || (n = ""),
        e(t(32), 8) + n + e(t(16), 4) + n + e(16384 | t(12), 4) + n + e(32768 | t(14), 4) + n + e(t(48), 12)
    }();
    return ret.substring(0, 16);
}

function Ir() {
  try {
         return Zi().substring(0, 16)
     } catch (t) {}
 }
testkey = '4Nl_NnGbjwY';
var x = ";x=" + Ir(), i = "c=B|" + testkey;
XTingyun=i + x


return [s,h,w,XTingyun]
}

function get_param(){
    var sm2 = require("sm-crypto").sm2


    function v(e) {
                var t = [];
                for (var n in e)
                    if (e.hasOwnProperty(n) && (e[n] || "".concat(e[n])))
                        if ("data" === n) {
                            var i = Object.assign({}, e[n]);
                            for (var r in i) {
                                if ("number" != typeof i[r] && "boolean" != typeof i[r] || (i[r] = "" + i[r]),
                                Array.isArray(i[r]) && !i[r].length && delete i[r],
                                Array.isArray(i[r]) && i[r].length > 0)
                                    for (var o = 0; o < i[r].length; o++)
                                        i[r][o] = p(i[r][o]);
                                null != i[r] && i[r] || delete i[r]
                            }
                            var a = p(i);
                            t.push("".concat(n, "=").concat(JSON.stringify(a)))
                        } else
                            t.push("".concat(n, "=").concat(e[n]));
                return t.push("key=".concat("NMVFVILMKT13GEMD3BKPKCTBOQBPZR2P")),
                t.join("&")
            }

    function m(e) {
                var t = {}
                  , n = ["signData", "encData", "extra"];
                for (var i in e)
                    e.hasOwnProperty(i) && !n.includes(i) && null != e[i] && (t[i] = e[i]);
                return t
            }


    function p(e) {
                var t = new Array
                  , n = 0;
                for (var i in e)
                    t[n] = i,
                    n++;
                var r = [].concat(t).sort()
                  , o = {};
                for (var a in r)
                    o[r[a]] = e[r[a]];
                return o
            }






        t = {
    "data": {
        "addr": "",
        "regnCode": "430500",
        "medinsName": "",
        "medinsLvCode": "",
        "medinsTypeCode": "",
        "outMedOpenFlag": "",
        "pageNum": 1,
        "pageSize": 10,
        "queryDataSource": "es"
    },
    "appCode": "T98HPCGN5ZVVQBS8LZQNOAEXVI9GYHKQ",
    "version": "1.0.0",
    "encType": "SM4",
    "signType": "SM2",
    "timestamp": 1741626318
}
        l =
            {
                appCode: "T98HPCGN5ZVVQBS8LZQNOAEXVI9GYHKQ",
                version: "1.0.0",
                appSecret: "NMVFVILMKT13GEMD3BKPKCTBOQBPZR2P",
                publicKey: "BEKaw3Qtc31LG/hTPHFPlriKuAn/nzTWl8LiRxLw4iQiSUIyuglptFxNkdCiNXcXvkqTH79Rh/A2sEFU6hjeK3k=",
                privateKey: "AJxKNdmspMaPGj+onJNoQ0cgWk2E3CYFWKBJhpcJrAtC",
                publicKeyType: "base64",
                privateKeyType: "base64"
            }

        var n = m(t)
        , i = p(n);
    // console.log(t)
        i.data = p(i.data);

        var r = v(i)

        , a = sm2.doSignature(r, "009c4a35d9aca4c68f1a3fa89c93684347205a4d84dc260558a049869709ac0b42", {
        hash: !0
        });
        console.log(a)
        // console.log(a)
        sign_DATA =  Buffer.from("4a31f5b8bc6e653531502f28525e9f72d973b632b8c91dcfc5841ed352ab057b93ba85cf5beb92c53fe06106994e2706277f4ab284055b4c570055b130b23303", "hex").toString("base64")
        console.log(sign_DATA)







        function y(e, t) {
        return A(b(A(e.substr(0, 16)), A(t)).toUpperCase().substr(0, 16))
        }

        function l111(e, t) {
        return e << t | e >>> 32 - t
        }
        function u123(e) {
            return (255 & a[e >>> 24 & 255]) << 24 | (255 & a[e >>> 16 & 255]) << 16 | (255 & a[e >>> 8 & 255]) << 8 | 255 & a[255 & e]
        }
        function h123(e) {
            return e ^ l111(e, 13) ^ l111(e, 23)
        }

        function c1133(e) {
            return e ^ l111(e, 2) ^ l111(e, 10) ^ l111(e, 18) ^ l111(e, 24)
        }
        function d1313(e, t, n) {
            for (var i, r, o = new Array(4), a = new Array(4), s = 0; s < 4; s++)
                a[0] = 255 & e[0 + 4 * s],
                a[1] = 255 & e[1 + 4 * s],
                a[2] = 255 & e[2 + 4 * s],
                a[3] = 255 & e[3 + 4 * s],
                o[s] = a[0] << 24 | a[1] << 16 | a[2] << 8 | a[3];
            for (i = 0; i < 32; i += 4)
                r = u123(r = o[1] ^ o[2] ^ o[3] ^ n[i + 0]),
                o[0] ^= c1133(r),
                r = u123(r = o[2] ^ o[3] ^ o[0] ^ n[i + 1]),
                o[1] ^= c1133(r),
                r = u123(r = o[3] ^ o[0] ^ o[1] ^ n[i + 2]),
                o[2] ^= c1133(r),
                r = u123(r = o[0] ^ o[1] ^ o[2] ^ n[i + 3]),
                o[3] ^= c1133(r);
            for (var l = 0; l < 16; l += 4)
                t[l] = o[3 - l / 4] >>> 24 & 255,
                t[l + 1] = o[3 - l / 4] >>> 16 & 255,
                t[l + 2] = o[3 - l / 4] >>> 8 & 255,
                t[l + 3] = 255 & o[3 - l / 4]
        }
        var i = 0
          , r = 32
          , o = 16
          , a = [214, 144, 233, 254, 204, 225, 61, 183, 22, 182, 20, 194, 40, 251, 44, 5, 43, 103, 154, 118, 42, 190, 4, 195, 170, 68, 19, 38, 73, 134, 6, 153, 156, 66, 80, 244, 145, 239, 152, 122, 51, 84, 11, 67, 237, 207, 172, 98, 228, 179, 28, 169, 201, 8, 232, 149, 128, 223, 148, 250, 117, 143, 63, 166, 71, 7, 167, 252, 243, 115, 23, 186, 131, 89, 60, 25, 230, 133, 79, 168, 104, 107, 129, 178, 113, 100, 218, 139, 248, 235, 15, 75, 112, 86, 157, 53, 30, 36, 14, 94, 99, 88, 209, 162, 37, 34, 124, 59, 1, 33, 120, 135, 212, 0, 70, 87, 159, 211, 39, 82, 76, 54, 2, 231, 160, 196, 200, 158, 234, 191, 138, 210, 64, 199, 56, 181, 163, 247, 242, 206, 249, 97, 21, 161, 224, 174, 93, 164, 155, 52, 26, 85, 173, 147, 50, 48, 245, 140, 177, 227, 29, 246, 226, 46, 130, 102, 202, 96, 192, 41, 35, 171, 13, 83, 78, 111, 213, 219, 55, 69, 222, 253, 142, 47, 3, 255, 106, 114, 109, 108, 91, 81, 141, 27, 175, 146, 187, 221, 188, 127, 17, 217, 92, 65, 31, 16, 90, 216, 10, 193, 49, 136, 165, 205, 123, 189, 45, 116, 208, 18, 184, 229, 180, 176, 137, 105, 151, 74, 12, 150, 119, 126, 101, 185, 241, 9, 197, 110, 198, 132, 24, 240, 125, 236, 58, 220, 77, 32, 121, 238, 95, 62, 215, 203, 57, 72]
          , s = [462357, 472066609, 943670861, 1415275113, 1886879365, 2358483617, 2830087869, 3301692121, 3773296373, 4228057617, 404694573, 876298825, 1347903077, 1819507329, 2291111581, 2762715833, 3234320085, 3705924337, 4177462797, 337322537, 808926789, 1280531041, 1752135293, 2223739545, 2695343797, 3166948049, 3638552301, 4110090761, 269950501, 741554753, 1213159005, 1684763257];
        function f1234(e, t, n) {
            var a = []
              , l = 0
              , c = new Array(r);
            !function(e, t, n) {
                for (var r, o, a = new Array(4), l = new Array(4), c = 0; c < 4; c++)
                    l[0] = 255 & e[0 + 4 * c],
                    l[1] = 255 & e[1 + 4 * c],
                    l[2] = 255 & e[2 + 4 * c],
                    l[3] = 255 & e[3 + 4 * c],
                    a[c] = l[0] << 24 | l[1] << 16 | l[2] << 8 | l[3];
                for (a[0] ^= 2746333894,
                a[1] ^= 1453994832,
                a[2] ^= 1736282519,
                a[3] ^= 2993693404,
                r = 0; r < 32; r += 4)
                    o = u123(o = a[1] ^ a[2] ^ a[3] ^ s[r + 0]),
                    t[r + 0] = a[0] ^= h123(o),
                    o = u123(o = a[2] ^ a[3] ^ a[0] ^ s[r + 1]),
                    t[r + 1] = a[1] ^= h123(o),
                    o = u123(o = a[3] ^ a[0] ^ a[1] ^ s[r + 2]),
                    t[r + 2] = a[2] ^= h123(o),
                    o = u123(o = a[0] ^ a[1] ^ a[2] ^ s[r + 3]),
                    t[r + 3] = a[3] ^= h123(o);
                if (n === i)
                    for (r = 0; r < 16; r++)
                        o = t[r],
                        t[r] = t[31 - r],
                        t[31 - r] = o
            }(t, c, n),
            new Array(16);
            for (var f = new Array(16), p = e.length; p >= o; ) {
                d1313(e.slice(l, l + 16), f, c);
                for (var m = 0; m < o; m++)
                    a[l + m] = f[m];
                p -= o,
                l += o
            }
            return a
        }
        function p123(e, t) {
        return f1234(e, t, 1)
        }
        function b(t, n) {
        var i = 16 - parseInt(n.length % 16);
        n = n.concat(new Array(i).fill(i));
        var r = p123(n, t);
        // console.log(r)
        return Buffer.from(r).toString("hex")
        }
        function A(e) {
                var t, n, i = new Array;
                t = e.length;
                for (var r = 0; r < t; r++)
                    (n = e.charCodeAt(r)) >= 65536 && n <= 1114111 ? (i.push(n >> 18 & 7 | 240),
                    i.push(n >> 12 & 63 | 128),
                    i.push(n >> 6 & 63 | 128),
                    i.push(63 & n | 128)) : n >= 2048 && n <= 65535 ? (i.push(n >> 12 & 15 | 224),
                    i.push(n >> 6 & 63 | 128),
                    i.push(63 & n | 128)) : n >= 128 && n <= 2047 ? (i.push(n >> 6 & 31 | 192),
                    i.push(63 & n | 128)) : i.push(255 & n);
                return i
            }

     var  n123  =JSON.stringify(t.data)
    // console.log(n123)
    var a = A(n123);
        console.log(a)
    var u = l.appCode
    // console.log(u)

    var s = y(u, "NMVFVILMKT13GEMD3BKPKCTBOQBPZR2P")
    s = [
    67,
    51,
    65,
    69,
    53,
    56,
    55,
    51,
    68,
    48,
    56,
    52,
    49,
    56,
    68,
    65
]
    // console.log(s)
    var l = b(s, a);
        // console.log(l)
    enc_DATA = "3dfbca4667b978f639bb23b95dce4cc7bf20a5e88ea26078ebc67b861077836accd20943b4dae96380b41164d761de9742c84a985fe3babc31cb352556bb87c9c1495db24a29ab6bc3a85ab7fca00f33c56677481a67c67f739ee2c7d589054dc373615b5ddb33c24c5b31e61cb7643e8ccaa19eae1fd36157cf9869e3a3753ed0b4e7bb97c60bf8e5275cafcafd1e13e384c10195003fd638576645b5ef45ea"
        enc_DATA = enc_DATA.toUpperCase()
    console.log(enc_DATA)
    return [sign_DATA,enc_DATA]


}

