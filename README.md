# Smart File Organizer

A Python GUI application that previews and categorizes files in a specified directory based on their file extensions.

## Features

- **GUI Interface**: Built with tkinter for easy folder selection and preview
- **File Categorization**: Categorizes files into:
  - **PDF** - `.pdf` files
  - **Images** - `.jpg`, `.jpeg`, `.png`, `.gif`, `.webp`
  - **Videos** - `.mp4`, `.mkv`, `.avi`
  - **Documents** - `.doc`, `.docx`, `.txt`
  - **Other** - All other file types
- **Folder Browser**: Select any directory using a native file dialog
- **Preview Mode**: View file counts by category before organizing
- **Status Feedback**: Real-time status updates

## Requirements

- Python 3.x
- tkinter (included with standard Python installation)

## Usage

1. Run the application:
   ```bash
   python gui.py
   ```

2. Click "Browse" to select a folder to analyze

3. Click "Preview Files" to see categorized file counts

4. The preview shows:
   - Total files found
   - Count per category (PDF, Image, Video, Document, Other)

## Example Output

```
Total Files : 15

PDF        : 3
Image      : 5
Video      : 2
Document   : 4
Other      : 1
```

## Project Structure

```
smart-file-organizer-GUI-Based/
├── gui.py          # Main GUI application
├── function.py     # File categorization logic
├── README.md       # This file
└── AUTHOR.md       # Author information
```

## Author

**B N Manish**

Software Developer with 7+ years of experience building SaaS, e-commerce, CRM, inventory management, and CMS platforms. Specializes in designing and developing complete solutions from scratch — admin panels, user-facing platforms, and backend architectures.

**Highlights:**
- Extensive experience with payment gateway integrations (Razorpay, Stripe, Cashfree, PayU, PayPal, Mollie) — including one-time, recurring, and charge-at-will flows
- Skilled in secure authentication, RBAC (Role-Based Access Control), Google reCAPTCHA, and WCAG accessibility implementation
- Hands-on experience with AI integrations, including ChatGPT APIs (Assistants, Threads, Runs, Messages, Chat Completion)
- Comfortable across Linux (Ubuntu) and Windows environments; strong with Git, GitHub, and GitLab

**Tech Stack:** PHP, Laravel, Yii2, CodeIgniter, JavaScript, ReactJs, TypeScript, Livewire, MySQL

[LinkedIn Profile](https://www.linkedin.com/in/bnmanish/)

## License

This project is open source and available under the MIT License.