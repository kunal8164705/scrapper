

from tika import parser

# Parse the file
file_path ="/Users/shtlpmac002/Documents/backup_8_oct/Kunal-Photo.png"
"/Users/shtlpmac002/Documents/backup_8_oct/kmportaldata/all_data/i-consult- Residential status of SWF under section 6(4) of the Act and Article 4 of DTAA.docm"
"/Users/shtlpmac002/Downloads/file-sample_100kB.rtf"
"/Users/shtlpmac002/Downloads/pg74540-images.epub"
"/Users/shtlpmac002/Documents/weaviate_vector_db/data_for_indexing/final_data_for_indexing.zip"
"/Users/shtlpmac002/Documents/weaviate_vector_db/data_for_indexing/final_data_for_indexing/GAP International Sourcing (India) Pvt_Ltd_Copy of Ruling_news alert_other reference material_AY 2013_14.zip"
"/Users/shtlpmac002/Documents/project_marvel/crawl4ai_test/scrapper.py" 
"/Users/shtlpmac002/Documents/weaviate_vector_db/Set off and carry forward of business losses u s 71 and 72_.json"
"/Users/shtlpmac002/Downloads/AI Search - UAT Observations.xlsx"
"/Users/shtlpmac002/Documents/project_marvel/sharepoint_data/Allowability of depreciation on intangible assets to A Co & taxability in the hands of F Co on sale of overseas business.doc"
# "/Users/shtlpmac002/Documents/project_marvel/sharepoint_data/202106- Introduction to MLI and Select Articles.pptx"
# 'example.pdf'
parsed = parser.from_file(file_path)

# Extract text
text = parsed['content']

print(text)