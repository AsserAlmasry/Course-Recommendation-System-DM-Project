# Course-Recommendation-System-DM-Project
Advanced Data Mining Techniques to organize Coursera courses


The project leverages clustering algorithms, cosine similarity, and text preprocessing to analyze course data and recommend courses tailored to user preferences.

Through visualization techniques and KMeans clustering, the project successfully demonstrates an efficient way to suggest courses, enhancing the overall user experience.

➢ Process:

1. Data Loading: Importing course data for analysis.

2. Text Preprocessing: Applying tokenization and stemming to clean and normalize textual data. 

3. Feature Engineering: Combining tokens to create a unified representation of course content. 

4. Vectorization: Converting textual data into numerical vectors using CountVectorizer. 

5. Cosine Similarity Calculation: Computing similarity between courses to identify related ones. 

6. KMeans Clustering: Grouping courses into clusters to enhance recommendation accuracy. 

7. Visualization: Using plots and heatmaps to evaluate data distribution and clustering results. 

8. Recommendation: Generating recommendations based on the similarity matrix and clustering outcomes. 


➢ Concepts of Data Mining Used: 

1. Clustering: Grouping similar courses using KMeans clustering. 

2. Cosine Similarity: Measuring similarity between courses based on their vectorized representations. 

3. Text Preprocessing: Tokenizing and stemming textual data to standardize it for analysis. 

4. Vectorization: Using CountVectorizer to transform text into numerical data. 

5. Data Visualization: Applying heatmaps, word clouds, and pairplots for insights into data structure and relationships. 


➢ Resources Used: 

• Programming Language: Python 
• Libraries: Pandas, NLTK, Scikit-learn, Matplotlib, Seaborn, WordCloud 
• Tools: Jupyter Notebook, Streamlit for visualization and deployment 
• Data Source: Coursera course dataset (CSV file containing course names, 
descriptions, and skills) 


➢ Dataset: The dataset used in this project is a CSV file named "Coursera.csv" containing the following columns: 

➢ Course Name: The title of the course. 
➢ Description: A brief overview of the course content. 
➢ Skills: Key skills taught in the course. 
