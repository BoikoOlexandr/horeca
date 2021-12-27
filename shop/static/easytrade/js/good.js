let count = 0
let Price = Number(prise.textContent)

minus.onclick = function() {
    if (count > 0) count -= 1
    countresult.innerHTML = count
    sum.innerHTML = count*Price
    result.value = count

};

plus.onclick = function() {
    count += 1
    countresult.innerHTML = count
    sum.innerHTML = count*Price
    result.value = count
};