from crewai import Agent, Task, Crew, Process
from github import Github
from dotenv import load_dotenv
import os
import base64
import chardet

# Load environment variables
load_dotenv()

class GithubResumeTools:
    def __init__(self, github_token):
        self.github = Github(github_token)
    
    def get_repository_content(self, repo_url):
        """Get all resume files from a repository"""
        try:
            # Extract owner and repo name from URL
            _, _, _, owner, repo_name = repo_url.rstrip('/').split('/')
            
            # Get the repository
            repo = self.github.get_repo(f"{owner}/{repo_name}")
            
            # Get all files in the repository
            contents = repo.get_contents("")
            resume_contents = []
            
            while contents:
                file_content = contents.pop(0)
                if file_content.type == "dir":
                    contents.extend(repo.get_contents(file_content.path))
                else:
                    # Only process text-based files for now
                    if file_content.name.lower().endswith(('.txt', '.md')):
                        try:
                            # Get the raw content
                            raw_content = base64.b64decode(file_content.content)
                            
                            # Detect the encoding
                            encoding_result = chardet.detect(raw_content)
                            encoding = encoding_result['encoding'] or 'utf-8'
                            
                            # Decode the content with the detected encoding
                            content = raw_content.decode(encoding)
                            
                            resume_contents.append({
                                'name': file_content.name,
                                'content': content,
                                'path': file_content.path
                            })
                        except Exception as e:
                            print(f"Skipping {file_content.name}: {str(e)}")
                            continue
            
            if not resume_contents:
                return "No readable resume files found. Please ensure the repository contains .txt or .md files."
            
            return resume_contents
        except Exception as e:
            return f"Error accessing repository: {str(e)}"

def create_resume_analyzer_agent():
    # Create an agent specialized in analyzing resumes
    analyzer = Agent(
        role='Technical Recruiter',
        goal='Analyze developer resumes and identify candidates based on specific criteria',
        backstory="""You are an experienced technical recruiter with a strong background in software development.
        You excel at evaluating technical skills, project complexity, and determining experience levels.""",
        allow_delegation=False
    )
    return analyzer

def analyze_resumes(repo_url, experience_level='mid', keywords=None):
    # Initialize tools with GitHub token
    github_token = os.getenv('GITHUB_TOKEN')
    if not github_token:
        return "Error: GitHub token not found in environment variables"
    
    tools = GithubResumeTools(github_token)
    analyzer = create_resume_analyzer_agent()
    
    # Get repository content first
    resumes = tools.get_repository_content(repo_url)
    
    if isinstance(resumes, str):
        return resumes  # Return error message if any
    
    # Format resumes for the task
    formatted_resumes = "\n\n".join([
        f"Resume: {r['name']}\n{r['content']}" 
        for r in resumes
    ])
    
    # Create experience level criteria
    experience_criteria = {
        'junior': {
            'years': '0-2',
            'description': 'entry-level to 2 years of experience, basic technical skills, learning-focused'
        },
        'mid': {
            'years': '2-5',
            'description': 'solid technical foundation, moderate project complexity, some mentoring'
        },
        'senior': {
            'years': '5+',
            'description': 'extensive experience, complex projects, significant leadership'
        }
    }[experience_level]
    
    # Build keyword filter description
    keyword_filter = ""
    if keywords and len(keywords) > 0:
        keyword_filter = f"\nAdditionally, prioritize candidates with experience in: {', '.join(keywords)}"
    
    # Create a task for resume analysis with the actual resumes
    analysis_task = Task(
        description=f"""Analyze these resumes and identify {experience_level} developers.
        
        Target Criteria:
        - Years of Experience: {experience_criteria['years']} years
        - Experience Level Description: {experience_criteria['description']}{keyword_filter}
        
        Here are the resumes to analyze:
        
        {formatted_resumes}
        
        Provide a detailed analysis including:
        1. Summary of analysis process
        2. List of identified {experience_level} developers with reasoning
        3. Brief explanation for other candidates
        
        For each candidate, evaluate:
        - Years of experience
        - Technical skills and their depth
        - Project complexity and responsibilities
        - Leadership or mentoring experience
        """,
        agent=analyzer,
        expected_output=f"A detailed analysis report identifying {experience_level} developers from the provided resumes"
    )
    
    crew = Crew(
        agents=[analyzer],
        tasks=[analysis_task],
        process=Process.sequential
    )
    
    result = crew.kickoff()
    return result

if __name__ == "__main__":
    # Example usage
    repo_url = "https://github.com/username/resume-repo"
    result = analyze_resumes(repo_url)
    print(result)