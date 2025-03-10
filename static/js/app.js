// static/js/app.js

// Initialize tooltips
document.addEventListener('DOMContentLoaded', function() {
    var tooltipTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="tooltip"]'));
    var tooltipList = tooltipTriggerList.map(function(tooltipTriggerEl) {
        return new bootstrap.Tooltip(tooltipTriggerEl);
    });
});

// File upload preview
function previewImage(input) {
    if (input.files && input.files[0]) {
        var reader = new FileReader();
        reader.onload = function(e) {
            document.getElementById('imagePreview').src = e.target.result;
        }
        reader.readAsDataURL(input.files[0]);
    }
}

// Health record form dynamic handling
document.addEventListener('DOMContentLoaded', function() {
    const recordTypeSelect = document.getElementById('id_record_type');
    const symptomFields = document.getElementById('symptom-fields');
    
    if (recordTypeSelect && symptomFields) {
        recordTypeSelect.addEventListener('change', function() {
            if (this.value === 'checkup') {
                symptomFields.style.display = 'none';
            } else {
                symptomFields.style.display = 'block';
            }
        });
    }
});

// Achievement progress animation
function animateProgress() {
    const progressBars = document.querySelectorAll('.progress-bar');
    progressBars.forEach(bar => {
        const target = bar.getAttribute('aria-valuenow');
        let width = 0;
        const interval = setInterval(() => {
            if (width >= target) {
                clearInterval(interval);
            } else {
                width++;
                bar.style.width = width + '%';
            }
        }, 10);
    });
}

// Form validation
function validateForm(formId) {
    const form = document.getElementById(formId);
    if (!form) return true;

    let isValid = true;
    const requiredFields = form.querySelectorAll('[required]');

    requiredFields.forEach(field => {
        if (!field.value.trim()) {
            isValid = false;
            field.classList.add('is-invalid');
        } else {
            field.classList.remove('is-invalid');
        }
    });

    return isValid;
}

// AJAX for real-time health status updates
function updateHealthStatus(petId, status) {
    fetch(`/api/pets/${petId}/health-status/`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': getCookie('csrftoken')
        },
        body: JSON.stringify({ status: status })
    })
    .then(response => response.json())
    .then(data => {
        if (data.success) {
            showNotification('Health status updated successfully');
        }
    })
    .catch(error => console.error('Error:', error));
}

// Utility function to get CSRF token
function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

// Notification system
function showNotification(message, type = 'success') {
    const notification = document.createElement('div');
    notification.className = `alert alert-${type} alert-dismissible fade show`;
    notification.innerHTML = `
        ${message}
        <button type="button" class="btn-close" data-bs-dismiss="alert"></button>
    `;
    document.getElementById('notification-container').appendChild(notification);
    
    setTimeout(() => {
        notification.remove();
    }, 5000);
}