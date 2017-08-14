

function drawMagnifi() {
    magniPattern = document.getElementById('searchIco');
    getsetwhcheckifinviewport(magniPattern, "True");
    if (magniPattern.getContext) {
        var xCord = Math.round(canWidth / 2.35 + 0.5);
        var yCord = Math.round(canHeight / 2.35 + 0.5);
        var magniCanva = magniPattern.getContext('2d');
        magniCanva.beginPath();
        magniCanva.arc(xCord, yCord, yCord - 2.5, 0, Math.PI / 4, false);
        magniCanva.lineTo(canWidth, canHeight);
        magniCanva.arc(xCord, yCord, yCord - 2.5, Math.PI / 4, 4 * Math.PI, false);//2 circles..
        magniCanva.strokeStyle = "white";
        magniCanva.stroke();
    }
}
//function drawHamburger(colorStr) {
function drawHamburger(clrargHam, linesnr) {
    canvasHamburger = document.getElementById('hamburger');
    getsetwhcheckifinviewport(canvasHamburger, null);
    var lines;
    if (linesnr) {
        lines = linesnr;
    }
    else {
        lines = 3;
    }
    var lineWidth = 1;//PX VALUE
    var coloredAred = lines * lineWidth;
    var padarea = canHeight - coloredAred - lineWidth;
    var fullheightlines = lines - 1;
    var pad = padarea / fullheightlines;
    pad = Math.round(pad);
    if (padarea < 0) {
        return;
    }
    var xCord = 0;
    var yCord = 0.5;

    var letters = '0123456789ABCDEF';
    var color = '#';

    for (var i = 0; i < 6; i++) {
        color += letters[Math.floor(Math.random() * 16)];
    }
    if (canvasHamburger.getContext) {
        var ctxHam = canvasHamburger.getContext('2d');
        // ctxHam.beginPath();
        ctxHam.lineWidth = lineWidth;
        for (var i = 0; i < lines; i++) {
            for (var c = 0; c < lineWidth; c++) {
                ctxHam.moveTo(xCord, yCord);
                ctxHam.lineTo(canWidth, yCord);
                yCord += lineWidth;
            }
            yCord += pad;
        }
        if (clrargHam) {
            ctxHam.strokeStyle = clrargHam;
        }
        else {
            ctxHam.strokeStyle = "" + color + "";
        }
        ctxHam.stroke();
        color = "";
        clrargHam = ""
    }
}
function drawSipkah() {
    canvasArrow = document.getElementById('arrwC');
    getsetwhcheckifinviewport(canvasArrow, "True");
    var arrowThick = canHeight / 100 * 10;
    if (canvasArrow.getContext) {
        var ctx = canvasArrow.getContext('2d');
        ctx.beginPath();
        ctx.moveTo(canWidth / 4, canHeight / 10);
        ctx.lineTo(canWidth / 4, canHeight / 2 - arrowThick / 2);
        ctx.lineTo(canWidth / 5 * 4, canHeight / 2 - arrowThick / 2);
        ctx.lineTo(canWidth / 5 * 4, canHeight / 2 - arrowThick / 2 + arrowThick);
        ctx.lineTo(canWidth / 4, canHeight / 2 - arrowThick / 2 + arrowThick);
        ctx.lineTo(canWidth / 4, canHeight / 10 * 9);
        ctx.lineTo(canHeight / 10, canHeight / 2);
        ctx.lineTo(canHeight / 2, canHeight / 10);
        ctx.fillStyle = "white";
        ctx.fill();
        var fyt = canvasArrow.getContext('2d');
        fyt.fillStyle = "#FFFFFF";
        fyt.fillRect(canWidth - canWidth / 10, 0, canHeight / 10, canHeight);
    }
}

function drawX() {
    canvasX = document.getElementById('arrwC');
    getsetwhcheckifinviewport(canvasX, null);
    if (canvasX.getContext) {
        //alert(canWidth+','+canHeight);
        var ctd = canvasX.getContext('2d');
        ctd.imageSmoothingEnabled = true;
        ctd.lineWidth = 9;
        ctd.beginPath();
        ctd.moveTo(0, 0);
        ctd.lineTo(canWidth, canHeight);
        ctd.moveTo(0, canHeight);
        ctd.lineTo(canWidth, 0);
        ctd.strokeStyle = "white";
        ctd.stroke();
    }
}

function getsetwhcheckifinviewport(htmlElem, set) {
    positionInfo = htmlElem.getBoundingClientRect();
    if (set == "True" || !set) {
        canWidth = positionInfo.width;
        canHeight = positionInfo.height;
        htmlElem.setAttribute("height", canHeight);
        htmlElem.setAttribute("width", canWidth);
        return canWidth, canHeight;
    }
    else {
        return ( positionInfo.top >= 0 &&
        positionInfo.left >= 0 &&
        positionInfo.bottom <= (window.innerHeight || document.documentElement.clientHeight) && /*or $(window).height() */
        positionInfo.right <= (window.innerWidth || document.documentElement.clientWidth));
    }
}


function getStyles(htmlElem) {
    var style = window.getComputedStyle ? getComputedStyle(htmlElem, null) : htmlElem.currentStyle;
    elemWidth = parseInt(style.width, 10);
    elemHeight = parseInt(style.height, 10);
    elemIsVisible = true;
    if (isNaN(elemHeight)) {
        elemIsVisible = false;
    }
    elemFontSize = parseInt(style['font-size'], 10);
    elemLineHeight = parseInt(style['line-height'], 10);
    if (isNaN(elemLineHeight)) {
        elemLineHeight = 18;
    }
    elemFontFamily = style['font-family'];
    return elemWidth, elemHeight, elemFontSize, elemFontFamily, elemIsVisible, elemLineHeight;
}
function getTextWidth(text, font) {
    var canvas = getTextWidth.canvas || (getTextWidth.canvas = document.createElement("canvas"));
    var context = canvas.getContext("2d");
    context.font = font;
    var metrics = context.measureText(text);
    objectWidth = metrics.width;
    return objectWidth;
}

function trimAnchors(maxLines) {
    var trimmedSymbol = "...";
    var anchors = document.getElementsByTagName('a');
    var l = anchors.length;
    for (var i = 0; i < l; i++) {
        var anchor = anchors[i];
        getStyles(anchor);
        //TODO VECI Z OWLU...
        if (elemIsVisible == true) {
            var txtt = anchor.innerText;
            if (txtt && (' ' + anchor.className + ' ').indexOf('main-menu-anchor') > -1 == false) {
                //todo jinym zpusobem
                if (elemHeight > elemLineHeight * maxLines) {
                    var containerWith = elemWidth;
                    // getTextWidth("M", elemFontSize + "px " + elemFontFamily);
                    anchor.innerText = "M";
                    getStyles(anchor);
                    var emWidth = Math.round(elemWidth);
                    var emsPerLines = containerWith / emWidth * maxLines;
                    var trimmedTextAlpha = txtt.slice(0, emsPerLines);
                    for (var x = emsPerLines; x < txtt.length; x++) {
                        var c = txtt.charAt(x);
                        trimmedTextAlpha += c;
                        anchor.innerText = trimmedTextAlpha;
                        getStyles(anchor);
                        if (elemHeight > elemLineHeight * maxLines) {
                            anchor.innerText = trimmedTextAlpha.slice(0, trimmedTextAlpha.length - 5) + trimmedSymbol;
                            x = txtt.length;
                        }
                    }
                }
            }
        }
    }
}
