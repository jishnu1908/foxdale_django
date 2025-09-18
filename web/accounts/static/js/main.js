
function verify() {
    let y = document.getElementById('inputname').value;

    if (y.length <= 8) {
        window.alert('Username must be longer than 8 characters');
        return false;
    }
    
    return true;
}