
"""
📄 PDF Merger Script using PyPDF (pypdf)

This script merges multiple PDF files into a single PDF file using the pypdf library.
Useful for combining chapters, reports, or scanned documents into one organized file.

Requirements:
- Python 3.x
- pypdf library → Install via: pip install pypdf

Author: AMAN KUMAR
GitHub: https://github.com/aman-20232703
"""

from pypdf import PdfWriter

# Initialize the PdfWriter (acts as a PDF container for writing and combining)
merger = PdfWriter()

# List of input PDF filenames to merge
pdf_files = ["file1.pdf", "file2.pdf", "file3.pdf"]

print("📂 Merging the following PDF files:")
for pdf in pdf_files:
    print(f"   ➕ {pdf}")
    merger.append(pdf)

# Output file name
output_file = "merged-pdf.pdf"

# Write the merged content into a new file
merger.write(output_file)
merger.close()

print("\n✅ Merge complete!")
print(f"📄 Output saved as: {output_file}")
print(" You can now upload or share your combined PDF.")


#Showing more merging options
input1 = open("document1.pdf", "rb")
input2 = open("document2.pdf", "rb")
input3 = open("document3.pdf", "rb")

# Add the first 3 pages of input1 document to output
merger.append(fileobj=input1, pages=(0, 3))

# Insert the first page of input2 into the output beginning after the second page
merger.merge(position=2, fileobj=input2, pages=(0, 1))

# Append entire input3 document to the end of the output document
merger.append(input3)

# Write to an output PDF document
output = open("document-output.pdf", "wb")
merger.write(output)

# Close file descriptors
merger.close()
output.close()

