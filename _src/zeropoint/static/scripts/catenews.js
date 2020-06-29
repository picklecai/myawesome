var tabs = document.getElementsByClassName('tabs')[0].getElementsByTagName('button');
var contents = document.getElementsByName('tabContent');

(function changeTab(tab) {
    for(var i = 0, len = tabs.length; i < len; i++) {
        tabs[i].onclick = showTab;
    }
})();

function showTab() {
    for(var i = 0, len = tabs.length; i < len; i++) {
        if(tabs[i] === this) {
            contents[i].className = 'show';
        }
        else {
            contents[i].className = 'hidden';
        }
    }
}