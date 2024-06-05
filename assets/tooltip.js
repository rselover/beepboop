window.dccFunctions = window.dccFunctions || {};
window.dccFunctions.formatCurrency = function(value) {
    if (value < 1000000) {
        return '$' + (value / 1000).toFixed(0) + 'K';
    } else if (value === 1000000) {
        return '$1M';
    } else {
        return '$' + (value / 1000000).toFixed(2) + 'M';
    }
}