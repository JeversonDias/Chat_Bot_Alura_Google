function loadIframe(fileId) {
    var url = 'https://drive.google.com/file/d/' + fileId + '/preview';
    document.getElementById('driveIframe').src = url;
}