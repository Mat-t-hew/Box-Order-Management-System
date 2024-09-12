# Box Order Management System

## Overview

The Box Order Management System is designed to streamline the process of managing box orders, generating quotations, handling invoices, and maintaining user access for staff. The system is built using Python with Tkinter for the GUI, offering two main portals:

- **Client Portal:** For customers to get quotations, place orders, and receive invoices/receipts.
- **Staff Portal:** For staff to log in with different roles (Staff, Manager, Business Owner) and manage access, including creating, destroying, or resetting user profiles.

## Features

- **Client Portal:**
  - Get quotations based on box specifications.
  - Place orders and receive invoices/receipts.

- **Staff Portal:**
  - Role-based access for Staff, Manager, and Business Owner.
  - Authentication and profile management for staff users.

## Technologies

- **Language:** Python
- **GUI Framework:** Tkinter
- **IDE:** Visual Studio Code

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/Mat-t-hew/Box-Order-Management-System.git
    ```

2. Navigate to the project directory:
    ```bash
    cd Box-Order-Management-System
    ```

3. Set up a virtual environment (optional but recommended):
    ```bash
    python -m venv myenv
    ```

4. Activate the virtual environment:
    - On Windows:
        ```bash
        myenv\Scripts\activate
        ```
    - On macOS/Linux:
        ```bash
        source myenv/bin/activate
        ```

5. Install any required dependencies (if applicable):
    ```bash
    pip install -r requirements.txt
    ```

## Usage

To start the application, run:
```bash
python main.py
```
## Progress

### Progress Rating
- **Rating:** 7/10  
- **Explanation:** Significant progress has been made, including completing the base functionality of the client and staff portals. However, there are still pending tasks, such as connecting the GUI to backend logic and implementing error handling.

### Completed Tasks
- Basic UI for Client and Staff portals.
- Role-based access system.
- Navigation within a single window using Tkinter.

### Incomplete Tasks
- Detailed user authentication logic.
- Integration with backend data storage.
- Additional UI enhancements and bug fixes.

## Challenges

### Technical Challenge
The most difficult technical challenge encountered this week was integrating the Figma designs into a Tkinter GUI. As a beginner in Figma, the learning curve was steep, especially in exporting design elements to use them effectively in Tkinter. I needed to figure out how to map the visual components accurately to the Tkinter widgets while maintaining the design's integrity. Furthermore, converting complex Figma layouts to a Tkinter-compatible format required understanding both the limitations of Tkinter and the flexibility of Figma's design tools. As a backend developer, transitioning to a more front-end-focused task presented additional challenges in adjusting my thinking and approach to GUI design and event handling.

### Non-Technical Challenge
The most difficult non-technical challenge this week was managing time effectively while learning new tools and technologies, such as Figma for the UI design. As someone focused primarily on backend development, stepping into the world of UI/UX design required me to balance learning new skills with making actual progress on the project. This shift required me to quickly adapt to a new workflow and figure out how to integrate these designs into the existing codebase. Additionally, coordinating with team members who have different levels of experience and expertise in front-end development added to the complexity, as it required more communication and collaboration to ensure everyone was aligned on the project goals and progress.

## Screenshots

_Add screenshots of the Client Portal and Staff Portal here._

## Future Updates
- Expand functionality for both client and staff portals.
- Improve user interface based on feedback.
- Implement additional features such as order tracking and detailed reporting.

## Contributing
If you'd like to contribute to the project, please fork the repository and submit a pull request with your changes.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## How to Use Tkinter?
_Tkinter is a built-in Python module used for building GUIs. It provides various widgets like buttons, labels, text boxes, and more, which can be used to create windows and applications. For a comprehensive guide, refer to the [official Tkinter documentation](https://docs.python.org/3/library/tkinter.html)._

## Best Figma Practices
- **Start with a clear structure:** Organize your design files and pages.
- **Use auto-layout and components:** This will help in maintaining consistency across your design.
- **Use Figma's prototyping features:** Create interactive mockups to visualize the user flow.
- **Leverage Figma's community resources:** Utilize templates and plugins available in the Figma community to speed up your design process.
