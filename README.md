1. Project name and Tagline

TICKiT

TICKiT, ClickiT, EnjoyiT, Your Instant Pass to Awesome!!!

**3. Team Members**

**Jessica Sewe Guriyire **
**Role:** Back End Engineer 
**Reasoning:** Jessica’s expertise lies in backend development. She will be responsible for server-side logic, database management, and ensuring the functionality and performance of the TICKit platform. Her role is crucial in building a robust and scalable backend infrastructure.

**Vaness Jame Henley Coussey**
**Role:** Front End Engineer 
**Reasoning:** Vaness, specializing in frontend development, will focus on creating intuitive and visually appealing user interfaces for the TICKit web service. His role involves translating design concepts into responsive and engaging user experiences, ensuring a seamless interaction for users.

By dividing the team into backend and frontend engineers, each team member can focus on their specific area of expertise. This specialization ensures a depth of knowledge and efficiency in their respective domains.

**3. Technologies**

**Backend technologies:**
**Chosen:** Python
**Alternate: **JavaScript
**Trade-offs:** Python was selected for its readability, extensive libraries (such as Django for web development), and versatility. JavaScript was considered for its front-end capabilities, but Python's backend robustness and ease of integration led to the final decision. The project required a strong backend focus, making Python a more suitable choice


**Database Management System:**
**Chosen: **PostgreSQL
**Alternate:** MongoDB
**Trade-offs**: PostgreSQL was preferred for its relational database structure, ACID compliance, and robust features. MongoDB, a NoSQL database, was considered for its flexibility with unstructured data. The decision leaned towards PostgreSQL due to the project's need for complex relationships between data entities and the requirem




**Web Framework:**
**Chosen: **Flask
**Alternate:** Django
**Trade-offs:** Flask, selected for its lightweight and modular design, provides flexibility and is well-suited for small to medium-sized projects. Django, with its "batteries-included" philosophy, offers a more integrated solution suitable for larger and more complex applications. The decision to use Flask was made to prioritize simplicity, customiz



**Frontend Framework:**
**Chosen:** React
**Alternate:** Vue.js
**Trade-offs:** React was selected for its strong community support, a vast ecosystem of libraries, and a virtual DOM that enhances performance. Vue.js, known for its simplicity and ease of integration, was considered, but React's popularity and extensive third-party component libraries influenced the choice, facilitating faster development and future scalability.


**4. Challenge**
**Problem Statement:**
The TICKiT event web service seeks to tackle the challenge of streamlining and simplifying the process of ticket procurement for a diverse range of events, including conferences, sports, and entertainment. The current landscape often involves fragmented ticketing platforms, making it challenging for users to discover, purchase, and manage tickets seamlessly.
Limitations - What the Project Will Not Solve:
While TICKiT addresses the ticketing process, it does not solve broader issues related to event planning, logistics, or external factors affecting event attendance. It focuses specifically on providing a user-friendly platform for ticket transactions but does not guarantee event success, handle event organization, or address external circumstances affecting event attendance.
Target Audience and Users
TICKiT is designed to assist event enthusiasts, sports fans, conference attendees, and anyone looking for a convenient and centralized platform to purchase tickets for various events. It caters to a broad user base, including individuals seeking event tickets for personal enjoyment or professional networking.
Relevance to Locale:
TICKiT is not inherently dependent on a specific locale. While it can benefit users globally, the events listed on the platform may be localized based on geographical preferences. The service's adaptability allows it to be relevant and accessible to users worldwide, providing a universal solution for event ticketing needs


**5. Risks**

**Non-Technical Risks:**

**Potential Impact:** Market Competition


**Description:** Increased competition or market shifts could impact the service's user base and revenue.
Strategies for Prevention: Regular market analysis, staying updated on industry trends, and fostering customer loyalty through exclusive offers or partnerships will be pursued. The service will also strive for continuous improvement based on user feedback

**Potential Impact:** Legal and Compliance Issues
Description: Non-compliance with data protection regulations, licensing issues, or legal disputes could have severe consequences.
Strategies for Prevention: Regular legal assessments, compliance checks, and ensuring adherence to relevant laws and regulations will be prioritized. Legal consultation will be sought to address any potential concerns proactively


**Technical Risks:**
 
** Potential Impact**: System Downtime or Performance Issues Description: Technical glitches, server outages, or unexpected issues in third-party integrations could lead to service downtime or suboptimal performance. 
Safeguards/Alternatives: Regular system monitoring, automated testing, and redundant server configurations will be implemented to minimize downtime. A robust backup system and contingency plans for quick issue resolution will be in place.

**Potential Impact:** Security Vulnerabilities

**Description:** Potential breaches or vulnerabilities in the system could compromise user data and erode trust.
Safeguards/Alternatives: Regular security audits, encryption protocols, and strict access controls will be implemented. Continuous monitoring for potential threats, prompt software updates, and a response plan for security incidents will be integral.

**6. Infrastructure**

**Branching and Merging:**

**Process:** The team follows the Gitflow branching model. The main branches include master for production-ready code, develop for ongoing development, and feature branches for specific features or bug fixes. Feature branches are created, developed, and tested locally before merging into the develop branch. Release branches are used for final testing and preparing for production, and hotfix branches address urgent issues in the master branch.

**Deployment Strategy:**

**Strategy:** Continuous Integration/Continuous Deployment (CI/CD) is employed. Changes pushed to the develop branch trigger automated tests. Successful tests prompt deployment to a staging environment for further testing. Once approved, changes are merged into the master branch, triggering automatic deployment to the production environment. Rollback strategies are in place to address unforeseen issues.
Data Population:

**Approach:** The app's initial data is populated through seed scripts or fixtures during the deployment process. For ongoing updates, data may be sourced from APIs, user input, or integrated external systems. Regular database backups and versioning are implemented to ensure data integrity and provide recovery options.

**Testing Tools and Automation:**

**Tools:** Testing is conducted using a combination of unit testing, integration testing, and end-to-end testing.

**Automation:** Automated testing tools such as pytest for unit tests and Selenium for end-to-end tests are integrated into the CI/CD pipeline. Additionally, linting tools like ESLint for JavaScript and Pylint for Python are used to enforce code quality standards. Continuous monitoring tools are in place to identify potential issues in real-time.

**7. Existing Solutions**

**StubHub:**

**Similarities**: StubHub is a secondary ticket marketplace, sharing common ground with TICKiT in the event ticketing domain.
Differences: TICKiT focuses on primary ticket sales, ensuring authenticity and a direct connection between event organizers and attendees. StubHub primarily facilitates the resale of tickets, catering to a different segment of the market.


**Decision to Reimplement:**
While existing solutions StubHub offer comprehensive event management and ticketing services, TICKit has chosen to reimplement based on specific goals:

**Simplified Ticket Procurement:** TICKit aims to streamline the ticket purchase process, ensuring a user-friendly experience with an emphasis on simplicity and efficiency.

**Personalization: **TICKit focuses on personalized event recommendations, enhancing user engagement by tailoring suggestions based on user preferences and past interactions.

**Authenticity:** By prioritizing primary ticket sales, TICKit ensures the authenticity of tickets and fosters direct connections between event organizers and attendees.

The decision to reimplement is based on these specific aspects, addressing potential gaps in the market and providing users with a fresh, user-centric approach to event ticketing. Learning from existing solutions, TICKit seeks to offer a more intuitive, personalized, and authentic experience for users in the dynamic landscape of event ticketing.
