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

1. Select the desired experience level (Junior, Mid-level, or Senior)
2. Add any specific keywords you want to filter by (e.g., "full stack", "React")
3. Enter the GitHub repository URL containing the resumes
4. Click "Analyze Resumes"

## Important Notes

- Make sure your GitHub token has appropriate permissions to read repository contents
- Keep your API keys secure and never commit them to version control
- The application requires an active internet connection to access GitHub and OpenAI services

## License

MIT License
