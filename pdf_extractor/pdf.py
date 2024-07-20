from pypdf import PdfReader
import re
import os
from groq import Groq
from dotenv import load_dotenv
import groq 

load_dotenv()

groq_api_key = os.getenv("GROQ_API_KEY")
client = groq.Client(api_key=groq_api_key)

def extract_text_from_pdf(pdf_path):
    pdf_reader = PdfReader(pdf_path)
    text = ""
    for page_num in range(len(pdf_reader.pages)):
        page = pdf_reader.get_page(page_num)
        text += page.extract_text()
    return text

def segregate_sections(text):
    # Regex patterns to find sections
    section_a_pattern = re.compile(r'SECTION “A”\s*\[.*?\](.*?)(?=SECTION “B”|$)', re.DOTALL)
    section_b_pattern = re.compile(r'SECTION “B”\s*\[.*?\](.*?)(?=SECTION “C”|$)', re.DOTALL)

    # Find all matches
    section_a_match = section_a_pattern.search(text)
    section_b_match = section_b_pattern.search(text)

    section_a = section_a_match.group(1).strip() if section_a_match else ""
    section_b = section_b_match.group(1).strip() if section_b_match else ""

    return section_a, section_b

def extract_questions(section_text):
    # Split questions in Section A by the pattern of question numbers
    questions = re.split(r'\d+\.\s+', section_text)[1:]  # Split and remove the first empty element
    return questions

# # Main execution
# pdf_text = extract_text_from_pdf("example.pdf")
# section_a, section_b = segregate_sections(pdf_text)

# questions_section_a = extract_questions(section_a)
# questions_section_b = extract_questions(section_b)

# print("Section A Questions:")
# for i, question in enumerate(questions_section_a, start=1):
#     print(f"{i}. {question}\n")

# print("Section B Questions:")
# for i, question in enumerate(questions_section_b, start=1):
#     print(f"{i}. {question}\n")


def get_question(section, question_number, questions_section_a, questions_section_b):
    if section.lower() == 'a':
        return questions_section_a[question_number - 1] if 0 < question_number <= len(questions_section_a) else "Question not found."
    elif section.lower() == 'b':
        return questions_section_b[question_number - 1] if 0 < question_number <= len(questions_section_b) else "Question not found."
    else:
        return "Invalid section."

# section = input("Enter section (A/B): ")
# question_number = int(input("Enter question number: "))

# question = get_question(section, question_number, questions_section_a, questions_section_b)
# print(f"Question {question_number} from Section {section.upper()}: {question}")







def query_llm(question):
    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": question,
            }
        ],
        model="llama3-8b-8192",
    )
    return chat_completion.choices[0].message.content



# if question != "Question not found." and question != "Invalid section.":
#     print(f"Question {question_number} from Section {section.upper()}: {question}")
#     answer = query_llm(question)
#     print(f"Answer: {answer}")
# else:
#     print(question)

    # Function to save answers to a markdown file
def save_answers_to_markdown(filename, questions, answers):
    with open(filename, 'w') as f:
        for i, (question, answer) in enumerate(zip(questions, answers), start=1):
            f.write(f"### Question {i}\n")
            f.write(f"{question}\n\n")
            f.write(f"**Answer**: {answer}\n\n")

# Main execution
pdf_directory = "questions"  # Set the path to your directory containing PDFs
output_directory = "answers"  # Set the path to your output directory

if not os.path.exists(output_directory):
    os.makedirs(output_directory)

for pdf_file in os.listdir(pdf_directory):
    if pdf_file.endswith(".pdf"):
        pdf_path = os.path.join(pdf_directory, pdf_file)
        pdf_text = extract_text_from_pdf(pdf_path)
        section_a, section_b = segregate_sections(pdf_text)

        questions_section_a = extract_questions(section_a)
        questions_section_b = extract_questions(section_b)

        all_questions = questions_section_a + questions_section_b
        all_answers = [query_llm(question) for question in all_questions]

        output_filename = os.path.join(output_directory, f"{os.path.splitext(pdf_file)[0]}_answers.md")
        save_answers_to_markdown(output_filename, all_questions, all_answers)

        print(f"Processed and saved answers for {pdf_file}")

print("All PDFs processed.")
