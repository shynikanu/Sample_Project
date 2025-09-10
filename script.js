document.addEventListener('DOMContentLoaded', function () {
    const form = document.getElementById('task-form');
    const input = document.getElementById('task-input');
    const list = document.getElementById('task-list');

    // Add task
    form.addEventListener('submit', function (e) {
        e.preventDefault();
        const taskText = input.value.trim();
        if (taskText) {
            addTask(taskText);
            input.value = '';
            input.focus();
        }
    });

    // Add task to list
    function addTask(text) {
        const li = document.createElement('li');
        li.className = 'task-item';
        li.innerHTML = `
            <label>
                <input type="checkbox" aria-label="Mark task as completed">
                <span>${escapeHtml(text)}</span>
            </label>
            <div class="task-actions">
                <button class="delete-btn" aria-label="Delete task">Delete</button>
            </div>
        `;
        list.appendChild(li);
    }

    // Mark completed & delete
    list.addEventListener('click', function (e) {
        if (e.target.matches('input[type="checkbox"]')) {
            const item = e.target.closest('.task-item');
            item.classList.toggle('completed', e.target.checked);
        }
        if (e.target.matches('.delete-btn')) {
            const item = e.target.closest('.task-item');
            item.remove();
        }
    });

    // Escape HTML for security
    function escapeHtml(text) {
        const div = document.createElement('div');
        div.textContent = text;
        return div.innerHTML;
    }
});
