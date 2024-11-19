document.addEventListener("DOMContentLoaded", () => {
  const properties = document.querySelectorAll(".property");
  const investmentSection = document.querySelector(".investment-section");
  const chartSection = document.querySelector(".chart-section");
  const selectedProperty = document.getElementById("selected-property");
  const propertyValueElem = document.getElementById("property-value");
  const investmentInput = document.getElementById("investment");
  const percentageElem = document.getElementById("percentage");
  const finalizeButton = document.getElementById("finalize-investment");
  const chartCanvas = document.getElementById("value-chart");
  let chartInstance = null;

  // Function to generate zigzag growth data
  const generateGrowthData = (startValue, months) => {
    const values = [];
    let currentValue = startValue;
    for (let i = 0; i < months; i++) {
      currentValue += (Math.random() - 0.5) * 5000 + 3000; // Zigzag pattern
      values.push(Math.max(currentValue, 0)); // Ensure non-negative values
    }
    return values;
  };

  // Smoothly scroll to a section
  const scrollToSection = (section) => {
    section.scrollIntoView({ behavior: "smooth", block: "start" });
  };

  // Initialize event listeners for properties
  properties.forEach((property) => {
    const button = property.querySelector(".invest-button");
    button.addEventListener("click", () => {
      console.log("Invest button clicked!"); // Debugging
      const propertyValue = parseFloat(property.dataset.value);
      selectedProperty.textContent = property.querySelector("p").textContent;
      propertyValueElem.textContent = propertyValue.toLocaleString();
      investmentSection.style.display = "flex";
      chartSection.style.visibility = "hidden";
      investmentInput.value = "";
      percentageElem.textContent = "0";

      // Scroll to the investment section
      scrollToSection(investmentSection);

      // Update percentage on input change
      investmentInput.addEventListener("input", () => {
        const investment = parseFloat(investmentInput.value) || 0;
        const percentage = ((investment / propertyValue) * 100).toFixed(2);
        percentageElem.textContent = percentage;
      });

      // Show chart on finalizing investment
      finalizeButton.addEventListener("click", () => {
        console.log("Finalize button clicked!"); // Debugging
        investmentSection.style.display = "none";
        chartSection.style.visibility = "visible";

        const months = 12;
        const propertyGrowth = generateGrowthData(propertyValue, months);
        const investmentPercentage = parseFloat(percentageElem.textContent) / 100;
        const investmentGrowth = propertyGrowth.map(
          (value) => value * investmentPercentage
        );

        // Scroll to the chart section
        scrollToSection(chartSection);

        // Ensure chart is properly initialized
        setTimeout(() => {
          if (chartInstance) chartInstance.destroy(); // Destroy old chart
          chartInstance = new Chart(chartCanvas, {
            type: "line",
            data: {
              labels: Array.from(
                { length: months },
                (_, i) => `Month ${i + 1}`
              ),
              datasets: [
                {
                  label: "Property Value",
                  data: propertyGrowth,
                  borderColor: "#ff8c42",
                  borderWidth: 2,
                  tension: 0.4,
                },
                {
                  label: "Your Investment Value",
                  data: investmentGrowth,
                  borderColor: "#42ff8c",
                  borderWidth: 2,
                  tension: 0.4,
                },
              ],
            },
            options: {
              responsive: true,
              plugins: {
                legend: { position: "top" },
              },
              scales: {
                x: { beginAtZero: true },
                y: { beginAtZero: true },
              },
            },
          });
          console.log("Chart successfully rendered!");
        }, 50);
      });
    });
  });
});
