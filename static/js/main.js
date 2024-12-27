document.addEventListener('DOMContentLoaded', function() {
    const weekItems = document.querySelectorAll('.week-item');
    
    weekItems.forEach(item => {
        item.addEventListener('click', function() {
            const weekId = this.dataset.week;
            loadContent(weekId);
            
            // Update active state of sidebar items
            weekItems.forEach(wi => wi.classList.remove('active'));
            this.classList.add('active');
        });
    });
});

function loadContent(weekId) {
    const topics = document.querySelectorAll('.topic-content');
    topics.forEach(topic => {
        if (topic.id === weekId) {
            topic.classList.remove('hidden');
            topic.classList.add('active');
        } else {
            topic.classList.add('hidden');
            topic.classList.remove('active');
        }
    });
}