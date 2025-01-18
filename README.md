# Resume Analysis Dashboard

A web application that analyzes developer resumes from GitHub repositories using CrewAI. The application allows filtering candidates by experience level (Junior, Mid-level, Senior) and specific keywords.

## Features

- Analysis of developer resumes from GitHub repositories
- Experience level filtering (Junior, Mid-level, Senior)
- Keyword-based filtering
- Modern, responsive UI
- Detailed candidate analysis including:
  - Years of experience
  - Technical skills
  - Project complexity
  - Leadership experience

## Prerequisites

- Python 3.8+
- GitHub Account and Personal Access Token
- OpenAI API Key
- Serper API Key (for CrewAI)
- A GitHub repository containing resumes to analyze

## Creating a Resume Repository

Before using this application, you need to have a GitHub repository containing the resumes you want to analyze. Here's how to set it up:

1. Create a new GitHub repository
2. Add resume files to the repository (supported formats: .md, .txt, .pdf)
3. Make sure the repository is accessible with your GitHub token
4. The resumes should contain relevant information such as:
   - Work experience
   - Technical skills
   - Project descriptions
   - Education
   - Leadership/mentoring experience

Example repository structure:
```
your-resume-repo/
├── junior-developer-resume.md
├── mid-level-developer-resume.md
├── senior-developer-resume.md
└── other-resumes.md
```

## Setup

1. Clone the repository:
```bash
git clone https://github.com/ianpilon/Resume-Analysis-Dashboard.git
cd Resume-Analysis-Dashboard
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Create a `.env` file in the root directory with your API keys:
```
OPENAI_API_KEY=your_openai_api_key
SERPER_API_KEY=your_serper_api_key
GITHUB_TOKEN=your_github_token
```

4. Run the application:
```bash
flask run --port=5002
```

5. Open your browser and navigate to:
```
http://localhost:5002
```

## Usage

1. Prepare your resume repository as described above
2. Select the desired experience level (Junior, Mid-level, or Senior)
3. Add any specific keywords you want to filter by (e.g., "full stack", "React")
4. Enter your resume repository URL (e.g., "https://github.com/username/resume-repo")
5. Click "Analyze Resumes"

## Important Notes

- Make sure your GitHub token has appropriate permissions to read repository contents
- Keep your API keys secure and never commit them to version control
- The application requires an active internet connection to access GitHub and OpenAI services
- The quality of analysis depends on the information available in the resumes
- Make sure resumes in your repository contain clear and structured information about experience, skills, and projects

## License

MIT License
