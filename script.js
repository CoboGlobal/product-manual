/*
window.addEventListener('load', function() {

checkAndChangeText()

    // Create a new MutationObserver
    var observer = new MutationObserver(function(mutationsList, observer) {
        for(var mutation of mutationsList) {
            if (mutation.type === 'childList') {
                checkAndChangeText()
            }
        }
    });

    // Start observing changes in the URL path
    observer.observe(document.body, { childList: true, subtree: true });
});


function checkAndChangeText() {
    const allElements = document.querySelectorAll('*');

    allElements.forEach(element => {
                    // Check if the element contains any text nodes
                    element.childNodes.forEach(child => {
                        if (child.nodeType === Node.TEXT_NODE && child.nodeValue.trim() !== '') {
                            if (window.location.href.includes('/en/')) {
                                element.style.color = 'blue';
                                //element.textContent = 'hi';
                            }
                        }
                    });
                });
}*/
