Array.prototype.forEach.call(document.getElementsByClassName('square'), function(item, index, array) {
    item.onclick = function() {
        this.classList.toggle('clicked');
    };
    item.classList.add('clickable');
});
