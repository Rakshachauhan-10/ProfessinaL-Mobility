import re
import csv
import integrated_function
from Subtopic_Challenge import model3_list, model1_list , model2_list  

s_topics = ["Introduction to Artificial Intelligence", "History of AI", "Basic Terminology and Concepts", "Applications of AI in Daily Life", "Ethical Considerations in AI"]
levels = ['Basics', 'Intermediate', 'Advance']

subtopics_lists = [model1_list, model2_list, model3_list]
models = [
    integrated_function.llama3_search,
    integrated_function.llama2_search,
    integrated_function.mistral_search
]

results_list = []

# level = 'Basics'
for s_topics, model in zip(subtopics_lists, models):
    course_query = f"""
    You are an educational content expert tasked with creating a complete course based on the following subtopics:

    {s_topics}. Your goal is to generate a well-structured course that is necessary for me to understand the topic completely. 

    Please create a comprehensive course that incorporates these subtopics, ensuring that the course is relevant, comprehensive, and

    engaging for '{levels}'-level learners. Include learning objectives, key concepts,and practical applications methods

    for each subtopic.
    """

    # Execute the model with the generated course_query
    result = model(course_query)
    results_list.append(result)

# course_query1=f"""You are an educational content expert tasked with creating a complete course based on the following subtopics:

# {s_topics}. Your goal is to generate a well-structured course that is necessary for me to understand the topic completely. 

# Please create a comprehensive course that incorporates these subtopics, ensuring that the course is relevant, comprehensive, and

# engaging for '{level}'-level learners. Include learning objectives, key concepts, practical applications, and assessment methods

# for each subtopic."""

# model1_result_s = integrated_function.llama3_search(course_query1)
# model2_result_s = integrated_function.llama2_search(course_query1)
# model3_result_s = integrated_function.mistral_search(course_query1)

#Storage
models = ['Llama3', 'Llama2', 'Mistral']
for model in models:
    if model=='Llama3':
        course_generated = results_list[0]
        with open("course.csv", 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([model, course_generated])

    if model=='Llama2':
        course_generated = results_list[1]
        with open("course.csv", 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([model, course_generated])

    if model=='Mistral':
        course_generated = results_list[2]
        with open("course.csv", 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([model, course_generated])
    

