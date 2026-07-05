document.addEventListener("DOMContentLoaded", () => {
    const menuButton = document.querySelector(".menu-toggle");
    const navigation = document.querySelector(".nav-links");

    if (menuButton && navigation) {
        menuButton.addEventListener("click", () => {
            const isOpen = navigation.classList.toggle("is-open");
            menuButton.classList.toggle("is-open", isOpen);
            menuButton.setAttribute("aria-expanded", String(isOpen));
            document.body.classList.toggle("menu-open", isOpen);
        });

        navigation.querySelectorAll("a").forEach((link) => {
            link.addEventListener("click", () => {
                navigation.classList.remove("is-open");
                menuButton.classList.remove("is-open");
                menuButton.setAttribute("aria-expanded", "false");
                document.body.classList.remove("menu-open");
            });
        });
    }

    const resizeCharts = () => {
        if (!window.Plotly) {
            return;
        }

        document.querySelectorAll(".plotly-graph-div").forEach((chart) => {
            window.Plotly.Plots.resize(chart);
        });
    };

    window.addEventListener("resize", resizeCharts);
    setTimeout(resizeCharts, 300);
});
