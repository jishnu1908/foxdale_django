
function verify() {
    let y = document.getElementById('inputusername').value;

    if (y.length <= 5) {
        window.alert('Username must be longer than 5 characters');
        return false;
    }
    
    return true;
}