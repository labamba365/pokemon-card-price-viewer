// script.js
// Fetches card data and populates the table based on selected price metric.

// Global variable to store card data once loaded
let cardData = [];

/**
 * Populate the table body with sorted card data.
 *
 * @param {string} metric - The metric to sort by (low, mid, high, market)
 */
function populateTable(metric) {
  if (!Array.isArray(cardData) || cardData.length === 0) return;
  // Create a copy of the array and sort by chosen metric descending
  const sorted = [...cardData].sort((a, b) => b[metric] - a[metric]);
  const tbody = document.querySelector('#card-table tbody');
  // Clear any existing rows
  tbody.innerHTML = '';
  // Limit to top 10 cards
  sorted.slice(0, 10).forEach((card, index) => {
    const tr = document.createElement('tr');
    tr.innerHTML = `
      <td>${index + 1}</td>
      <td>${card.name}</td>
      <td>${card.low.toFixed(2)}</td>
      <td>${card.mid.toFixed(2)}</td>
      <td>${card.high.toFixed(2)}</td>
      <td>${card.market.toFixed(2)}</td>
    `;
    tbody.appendChild(tr);
  });
}

/**
 * Initialize the page: load data and set up event listeners.
 */
async function init() {
  try {
    const response = await fetch('../cards_data.json');
    if (!response.ok) {
      throw new Error(`HTTP error! status: ${response.status}`);
    }
    const data = await response.json();
    cardData = data;
    const select = document.getElementById('metric-select');
    // Initially populate table with selected option
    populateTable(select.value);
    // Update table on selection change
    select.addEventListener('change', () => {
      populateTable(select.value);
    });
  } catch (err) {
    console.error('Failed to load or parse card data:', err);
    const tbody = document.querySelector('#card-table tbody');
    tbody.innerHTML = '<tr><td colspan="6">Error loading card data.</td></tr>';
  }
}

// Run init on DOMContentLoaded
document.addEventListener('DOMContentLoaded', init);
