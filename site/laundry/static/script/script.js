function openContact() {
    document.getElementById('contact_modal').classList.add('show');
  }
  function openLoc() {
    document.getElementById('loc_modal').classList.add('show');
  }

  function openFAQ() {
    document.getElementById('faq_modal').classList.add('show');
  }
  function openLS() {
    document.getElementById('LS_modal').classList.add('show');
  }
  function openRe() {
    document.getElementById('Re_modal').classList.add('show');

  }
  function openStatus() {
    document.getElementById('statusModal').classList.add('show');

  }
   function openR() {
    document.getElementById('R_modal').classList.add('show');
  }
  function openE() {
    document.getElementById('E_modal').classList.add('show');
  }
  function openD() {
    document.getElementById('D_modal').classList.add('show');
  }
  function openC() {
    document.getElementById('confirmationModal').classList.add('show');
    
  }
  

  document.addEventListener('DOMContentLoaded', function() {
    // Function to toggle field visibility
    function toggleFields(checkbox, fieldsClass) {
        const checkboxElement = document.querySelector(`input[name="${checkbox}"]`);
        const fields = document.querySelectorAll(`.${fieldsClass}`);
        
        function updateFields() {
            fields.forEach(field => {
                if (checkboxElement.checked) {
                    field.style.display = 'block';
                    setTimeout(() => field.style.opacity = '1', 10);
                } else {
                    field.style.opacity = '0';
                    setTimeout(() => field.style.display = 'none', 300);
                }
            });
        }
        
        // Initial update
        updateFields();
        
        // Add event listener
        checkboxElement.addEventListener('change', updateFields);
    }
    
    // Apply to both pickup and delivery fields
    toggleFields('pickup_required', 'pickup-details');
    toggleFields('delivery_required', 'delivery-details');
});
  
  window.onclick = function(event) {
    const contactModal = document.getElementById('contact_modal');
    const faqModal = document.getElementById('faq_modal');
    const lsModal = document.getElementById('LS_modal');
    const ReModal = document.getElementById('Re_modal');
    const statusModal = document.getElementById('statusModal');
    const rModal = document.getElementById('R_modal');
    const eModal = document.getElementById('E_modal');
    const dModal = document.getElementById('D_modal');
    const lModal = document.getElementById('loc_modal');
    const cModal = document.getElementById('confirmationModal');

  
    if (event.target === contactModal) {
      contactModal.classList.remove('show');
    }
    if (event.target === faqModal) {
      faqModal.classList.remove('show');
    }
    if (event.target === lsModal) {
        lsModal.classList.remove('show');
      }
    if (event.target === ReModal) {
        ReModal.classList.remove('show');
      }
    if (event.target === statusModal) {
        statusModal.classList.remove('show');
      }
    if (event.target === rModal) {
      rModal.classList.remove('show');
    }
    if (event.target === lModal) {
      lModal.classList.remove('show');
    }
    if (event.target === eModal) {
      eModal.classList.remove('show');
    }
    if (event.target === dModal) {
      dModal.classList.remove('show');
    }
  if (event.target === cModal) {
    cModal.classList.remove('show');
  }
    
  };
  
   document.getElementById('statusForm').addEventListener('submit', function(e) {
    e.preventDefault(); // Prevent the form from submitting normally

    const rngCode = document.getElementById('rngCodeInput').value;
    const statusMessage = document.getElementById('statusMessage');

    // Clear previous result
    statusMessage.innerHTML = '';

    // Make the GET request
    fetch(`/get-completion-status/?rng_code=${encodeURIComponent(rngCode)}`)
      .then(response => {
        if (!response.ok) {
          if (response.status === 404) {
            throw new Error('Reservation code not found.');
          }
          throw new Error('An error occurred. Please try again.');
        }
        return response.json();
      })
      .then(data => {
        statusMessage.innerHTML = `<p>Status: <strong>${data.completion_status}</strong></p>`;
      })
      .catch(error => {
        statusMessage.innerHTML = `<p style="color: red;">${error.message}</p>`;
      });
  });