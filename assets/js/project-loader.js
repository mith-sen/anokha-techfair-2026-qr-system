
document.addEventListener('DOMContentLoaded', async () => {
    try {
        // 1. Get Project ID
        // Try getting from .project-id element text first (if present), or fallback to filename
        let projectId = '';
        const idEl = document.querySelector('.project-id');

        // Strategy: Stick with filename as the robust key, but if we are testing locally or filename is different,
        // we might rely on the text content if it looks like a valid ID.
        // However, the JSON was generated using filenames. So filename is the safest key.
        const path = window.location.pathname;
        const filename = path.split('/').pop().replace('.html', '');
        projectId = filename;

        console.log(`Loading project data for ID: ${projectId}`);

        // 2. Fetch Data
        // projects.json is in the root directory
        const response = await fetch('./projects.json');
        if (!response.ok) throw new Error('Failed to load project data');
        const projects = await response.json();

        const data = projects[projectId];
        if (!data) {
            console.error(`Project data for ${projectId} not found in JSON.`);
            return;
        }

        // 3. Populate Data

        // Title
        // Preserve the Github icon logic if it exists
        const h1 = document.querySelector('h1');
        if (h1) {
            const githubLink = h1.querySelector('.github-title-icon');
            if (githubLink) {
                // Update href if data exists
                if (data.githubLink) {
                    githubLink.href = data.githubLink;
                    githubLink.style.display = 'inline-flex';
                } else {
                    // Optionally hide it if no link? User said store it, implies usages.
                    // Let's keep it but maybe it goes nowhere (#) if empty.
                    githubLink.href = '#';
                }
            }
            // Re-insert content
            const iconHtml = githubLink ? githubLink.outerHTML : '';
            h1.innerHTML = `${data.title} ${iconHtml}`;

            // Re-bind the element reference after innerHTML replacement (though outerHTML approach preserved attributes)
            // If we want to ensure the specific element in the DOM is updated if we didn't use innerHTML for it:
            const newLink = h1.querySelector('.github-title-icon');
            if (newLink && data.githubLink) newLink.href = data.githubLink;
        }

        // Update Document Title
        document.title = `${data.id} - ${data.title}`;

        // Project ID Display
        if (idEl) idEl.textContent = data.id || projectId;

        // Department
        const deptEl = document.querySelector('.department');
        if (deptEl) deptEl.textContent = data.department;

        // Team Info
        updateInfoValue('Team Name', data.teamName);
        updateInfoValue('Stall Number', data.stallNumber);
        updateInfoValue('Faculty Mentor', data.facultyMentor);

        // Description
        const descEl = document.querySelector('.description');
        if (descEl) descEl.textContent = data.description;

        // Levels: TRL, MRL, IRL
        updateLevel('TRL', data.trl);
        updateLevel('MRL', data.mrl);
        updateLevel('IRL', data.irl);

        // SDGs
        const sdgContainer = document.querySelector('.sdg-icons');
        if (sdgContainer && data.sdgs) {
            sdgContainer.innerHTML = '';
            data.sdgs.forEach(sdg => {
                const img = document.createElement('img');
                img.src = `./assets/SDGS/SDG${sdg}.jpg`;
                img.alt = `SDG ${sdg}`;
                img.className = 'sdg-icon';
                sdgContainer.appendChild(img);
            });
        }

        // Team Members
        const membersContainer = document.querySelector('.team-members');
        if (membersContainer && data.teamMembers) {
            membersContainer.innerHTML = '';
            data.teamMembers.forEach(member => {
                const div = document.createElement('div');
                div.className = 'team-member';
                const linkedinUrl = member.linkedin || '#';

                div.innerHTML = `
                    <div>
                        ${member.name} <span class="roll-number">${member.rollNumber}</span>
                    </div>
                    <a href="${linkedinUrl}" class="member-link" target="_blank" rel="noopener noreferrer">
                         <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="#0077b5">
                           <path d="M19 0h-14c-2.761 0-5 2.239-5 5v14c0 2.761 2.239 5 5 5h14c2.762 0 5-2.239 5-5v-14c0-2.761-2.238-5-5-5zm-11 19h-3v-11h3v11zm-1.5-12.268c-.966 0-1.75-.79-1.75-1.764s.784-1.764 1.75-1.764 1.75.79 1.75 1.764-.783 1.764-1.75 1.764zm13.5 12.268h-3v-5.604c0-3.368-4-3.113-4 0v5.604h-3v-11h3v1.765c1.396-2.586 7-2.777 7 2.476v6.759z" />
                         </svg>
                    </a>
                `;
                membersContainer.appendChild(div);
            });
        }
    } catch (e) {
        console.error("Error loading project data:", e);
    }
});

function updateInfoValue(label, value) {
    // Find div with class info-label containing text 'label'
    const labels = Array.from(document.querySelectorAll('.info-label'));
    const targetLabel = labels.find(el => el.textContent.trim() === label);
    if (targetLabel) {
        // Find sibling with class info-value
        // The structure is info-item -> (info-label, info-value)
        // So info-value is sibling
        const parent = targetLabel.parentElement;
        const valueEl = parent.querySelector('.info-value');
        if (valueEl) {
            valueEl.textContent = value || 'N/A';
        }
    }
}

function updateLevel(label, value) {
    const labels = Array.from(document.querySelectorAll('.level-label'));
    const targetLabel = labels.find(el => el.textContent.trim() === label);
    if (targetLabel && targetLabel.parentElement) {
        const valEl = targetLabel.parentElement.querySelector('.level-value');
        if (valEl) valEl.textContent = value || '-';
    }
}