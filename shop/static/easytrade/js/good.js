let count = 1
let Price = parseFloat(prise.textContent.replace(',', '.'))

minus.onclick = function() {
    if (count > 1) count -= 1
    countresult.innerHTML = count
    sum.innerHTML = Price * count
    result.value = count

};

plus.onclick = function() {
    count += 1
    countresult.innerHTML = count
    sum.innerHTML = Price * count
    result.value = count
};

