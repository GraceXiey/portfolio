# Grace Xie's Portfolio


## **Intro**

I recently graduated with a Master’s degree from Northwestern University, where I honed my skills in data science and business analysis. My passion lies in leveraging data to uncover actionable insights and drive impactful decision-making.

Throughout my academic and professional journey, I’ve gained extensive experience working with cutting-edge tools and platforms, including Snowflake, GCP, and AWS. My most recent project involved building a chatbot powered by large language models (LLMs) to address healthcare patient inquiries for Northwestern Medicine, integrating natural language processing with real-world applications.

In addition, I’ve worked at Breakthru Beverage Group, where I developed a recommendation system using data mining techniques to create personalized product suggestions. My previous experience at UIUC's Rail Transportation and Engineering Center involved safety and risk analysis, which strengthened my ability to tackle complex problems with data-driven solutions.

I excel in data modeling, analysis, and strategy development, and I am passionate about transforming raw data into clear, actionable insights. My programming expertise, coupled with my experience working in collaborative environments, has prepared me to enhance efficiency and accuracy for businesses and communities alike.

<img width="516" alt="Screen Shot 2024-12-22 at 10 27 37 PM" src="https://github.com/user-attachments/assets/ee7dc9c5-37c0-4ad6-a384-ab249eafbbb2" />


Beyond my professional pursuits, I am a multilingual communicator fluent in English, Chinese, Cantonese, Japanese, and Spanish, which helps me connect with diverse teams and clients. In my free time, I enjoy volleyball, badminton, photography, and video production.

I’m eager to connect with fellow data science professionals and enthusiasts to explore how we can harness the power of data and cloud platforms to solve real-world challenges and drive innovation. Let’s work together to create impactful solutions!


## Project Outline

#### [RAG Based LLM Chatbot for Onocology Radiology Patient Queries](https://github.com/GraceXiey/portfolio/tree/main/Radiology-RAG-LLM-Chatbot)

This project developed a Retrieval-Augmented Generation (RAG) chatbot to bridge communication gaps between patients and clinicians in radiation oncology. Leveraging LLaMA3.1 models, the system delivers personalized, empathetic, and accurate responses to patient queries, enhancing understanding of treatment plans, emotional support, and accessibility.

Key Features:

Advanced Retrieval: High-performance vector similarity search via FAISS for precise information retrieval.

Dynamic Response Generation: Context-aware, nuanced answers powered by domain-specific LLMs.

Empathetic Design: Tailored conversational flows for addressing sensitive medical topics.

Streamlined Deployment: Built with FastAPI backend, FAISS integration, and Streamlit frontend for seamless interaction.

Database Design: Initiate a storage place for inqury patient's bio info and query for comparison and also score ratings to further improve the answer with professional physicians review.

Impact:

By integrating authoritative medical knowledge and AI capabilities, CancerRAG enhances patient satisfaction, reduces anxiety, and optimizes clinician-patient communication.

#### [Subscription Churn Rate Analysis](https://github.com/GraceXiey/portfolio/tree/main/Subscription-Churn-Rate-Analysis) 

This group project focused on developing business solutions for newspaper subscriptions, specifically analyzing factors influencing churn rates and strategies to enhance customer loyalty. Using R for exploratory data analysis and assumption testing, we examined the structural relationships of various attributes, refining the model by adding or excluding factors based on weighted results. We included our best prediction model and identified the key drivers of churn, such as post-trial frequency, and provided actionable marketing recommendations to improve retention.

#### [Flight Trend in USA Data Visualizations](https://github.com/GraceXiey/portfolio/tree/main/Tableau-Flight-Trend-Analysis)

We aimed to address flight delays in the U.S. to enhance efficiency and personalization for the Department of Transportation, with an emphasis on the impact of COVID-19 on domestic flights. We developed dynamic visualizations, including:

- Map graphs with bar charts showing average delay times by airline across cities.
- Pre- and post-COVID arrival delay comparisons by state.
- Time-series analyses of daily average delays nationwide.
- Flight path density maps centered on Chicago O'Hare International Airport.
  
These visualizations allowed for comparisons across timeframes, cities, holidays, and destinations. Key insights included identifying heavily delayed areas, the most efficient airlines by state, and notable patterns like Hawaii's heavy traffic but minimal delays.

#### [Restaurant Recommendation System](https://github.com/GraceXiey/portfolio/tree/main/Yelp-Restaurant-Recomendation-System)

This project developed a dual-purpose Restaurant Recommendation System:

For Customers: Personalized restaurant recommendations based on preferences, dining history, and location using a hybrid model combining Collaborative Filtering (KNN, KNNWithMeans, SVD) and Content-Based Filtering (BERT embeddings, TF-IDF).

For Restaurant Owners: Data-driven insights to craft targeted advertisements via association rule mining on user reviews.

We utilized a large-scale Yelp dataset (~1M entries) to train and test models. Evaluated system performance using Mean Squared Error (MSE) and Mean Absolute Error (MAE), aiming to minimize RMSE for enhanced prediction accuracy. We demonstrated the practical application of modern recommendation algorithms, improving customer dining experiences and optimizing marketing efforts for restaurants.

#### [Airbnb Price Prediction](https://github.com/GraceXiey/portfolio/tree/main/R-NYC-Leasing-Price)

This project analyzed factors influencing Airbnb pricing and developed a predictive model to assist hosts in setting optimal prices. Using adataset of 20,758 New York City listings, we employed machine learning techniques, including Linear Regression, Neural Networks, CART, and XGBoost. The XGBoost model demonstrated the best performance, achieving an R² of 0.755 and RMSE of 0.356.

Key findings identified private room types, number of bedrooms, and baths as significant pricing factors. Recommendations include incorporating granular neighborhood data and socioeconomic characteristics to refine predictions and enhance the model's applicability across diverse geographies.

#### [Deep Face Detection Deap Learning](https://github.com/GraceXiey/portfolio/tree/main/DL-fakeface)

We deployed a deep learning system for detecting fake faces and recognizing facial expressions, addressing challenges in domains like security, healthcare, and entertainment.

Fake Face Detection: The Xception model outperformed custom CNNs, achieving superior accuracy despite imbalanced datasets.

Facial Expression Recognition: A custom CNN outperformed pretrained models (VGG16, ResNet50) in identifying emotions such as happy, sad, angry, and neutral.

#### [AWS Amazon Review Sentiment Analysis](https://github.com/GraceXiey/portfolio/tree/main/AWS-Amazon-Sentiment-Analysis)

We developed a real-time sentiment analysis application to classify Amazon customer reviews as positive, neutral, or negative. Built using NLP models (Simple Neural Network, CNN, LSTM) with GloVe embeddings, it provides actionable feedback for both buyers and sellers. We also piplined web scrapping inside Streamlit for outputing the real-time result by simply entering the website link from the product page.

AWS Integration:

Deployed the system on AWS using S3 for data storage, EC2 for model training, ECS for container orchestration, and CloudWatch for monitoring.
Efficient pipeline for web scraping, data processing, and visualization.
The application showcases robust NLP capabilities with seamless deployment on AWS, delivering insights to enhance product quality and customer satisfaction.



