from fpdf import FPDF

# Collect input
name, email, phone, linkedin = input("Name, Email, Phone, LinkedIn: ").split(", ")
education, university, grad_year = input("Education, University, Graduation Year: ").split(", ")
work_experience = input("Work Experience: ")
skills = input("Skills (comma separated): ")

# Generate PDF
pdf = FPDF()
pdf.add_page()
pdf.set_font('Arial', 'B', 16)
pdf.cell(200, 10, txt="Curriculum Vitae", ln=True, align='C')
pdf.ln(10)

pdf.set_font('Arial', 'B', 12)
pdf.cell(200, 10, txt="Personal Information", ln=True)
pdf.set_font('Arial', '', 12)
pdf.multi_cell(0, 10, f"Name: {name}\nEmail: {email}\nPhone: {phone}\nLinkedIn: {linkedin}")
pdf.ln(10)

pdf.set_font('Arial', 'B', 12)
pdf.cell(200, 10, txt="Education", ln=True)
pdf.set_font('Arial', '', 12)
pdf.multi_cell(0, 10, f"{education}\n{university}, {grad_year}")
pdf.ln(10)

pdf.set_font('Arial', 'B', 12)
pdf.cell(200, 10, txt="Work Experience", ln=True)
pdf.set_font('Arial', '', 12)
pdf.multi_cell(0, 10, work_experience)
pdf.ln(10)

pdf.set_font('Arial', 'B', 12)
pdf.cell(200, 10, txt="Skills", ln=True)
pdf.set_font('Arial', '', 12)
pdf.multi_cell(0, 10, skills)

# Output PDF
pdf.output('cv_short.pdf')

print("CV created!")
