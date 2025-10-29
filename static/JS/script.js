function showTab(tabName) {
    // Hide all tabs
    document.querySelectorAll('.tab').forEach(tab => {
        tab.classList.remove('active-tab');
    });

    // Remove active state from nav links
    document.querySelectorAll('.nav-links a').forEach(link => {
        link.classList.remove('active');
    });

    // Show selected tab and activate nav link
    document.getElementById(tabName).classList.add('active-tab');
    document.getElementById(tabName + '-tab').classList.add('active');
}
