console.log(
    "AI Career Recommendation System loaded successfully."
);

document.addEventListener("DOMContentLoaded", function () {

    const sliders = document.querySelectorAll(
        'input[type="range"]'
    );

    sliders.forEach(function (slider) {

        slider.addEventListener("input", function () {

            const output = slider.nextElementSibling;

            if (output) {

                output.value = slider.value;

            }

        });

    });

});