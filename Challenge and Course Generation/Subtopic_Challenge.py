import re
import csv
import integrated_function

topics = ['Artificial Intelligence']
levels = ['Beginner']

# subtopic_query = f"You are a subject matter expert providing detailed educational content. Your task is to Generate a list of subtopics for the topic {topic} and categorise the subtopics into the {level} level. These subtopics will form the foundation of a learning module. Please ensure that the subtopics are relevant and comprehensive."

# challenge_query = f"""Generate a real world based challenge on the subtopic {subtopic} related to {topic} of  {level} level. Structure the challenge according to the provided format, focusing on practical application and skill development.

# Challenge Format:

# - Name: Provide a concise and descriptive title for the challenge.

# - Objective: Clearly state the main goal or purpose of the challenge, highlighting what the participant will learn or accomplish.

# - Challenge Level: {level}

# - Description: Provide a detailed description of the challenge, including the context, scope, and any specific tasks or activities involved.

# - Milestone Evaluation: Outline key milestones that participants should achieve during the challenge, along with criteria for evaluating their progress.

# - Skills: List the specific skills that participants will develop or utilise during the challenge.

# - Challenge Guidelines: Provide guidelines or instructions that participants should follow, including any constraints or requirements.

# - Prerequisites: List any prerequisites that participants should meet before attempting the challenge.

# - Review Process: Describe the process for reviewing and assessing participants' work, including any feedback or scoring methods.

# Ensure that the challenge is aligned with the subtopic and is designed to facilitate skill growth and professional development.
# """

# LLama3
def extract_subtopics_as_sections(output_text):

    pattern = re.compile(r'(?:^|\n)([IVXLCDM]+\..+?(?=\n[IVXLCDM]+\.)|[IVXLCDM]+\..+)', re.DOTALL)

    sections = pattern.findall(output_text)

    sections = [section.strip() for section in sections if section.strip()]

    return sections

# Mistral
def extract_numbered_subtopics_as_sections(output_text):

    pattern = re.compile(r'(?:^|\n)(\d+\.\s[^\n]+(?:\n\s+-\s[^\n]+)*)', re.MULTILINE)

    sections = pattern.findall(output_text)

    sections = [section.strip() for section in sections if section.strip()]

    return sections

# Perplexity
# def extract_subtopics_with_bullets_v3(output_text):
   
#     pattern = re.compile(r'(\d+\.\s[^\n]+(?:\n\s*•\s.*)+)', re.MULTILINE)

#     matches = pattern.findall(output_text)

#     sections = [section.strip() for section in matches]

#     return sections

# Phind
# def extract_subtopics_with_bullets_v4(output_text):
    
#     pattern = re.compile(r'([A-Za-z\s&]+)\n((?:•\s[^\n]+\n)+)', re.MULTILINE)

#     matches = pattern.findall(output_text)

#     sections = []
#     for section_name, content in matches:
#         section = f"{section_name.strip()}\n{content.strip()}"
#         sections.append(section)

#     return sections

# LLama2
def extract_subtopics_v6(output_text):
  
    pattern = re.compile(r'(\d+\.\s[^\n]+(?:\n\s*\*\s[^\n]+)+)', re.MULTILINE)

    matches = pattern.findall(output_text)

    sections = [section.strip() for section in matches]

    return sections
for topic in topics:
  print(topic)
  for level in levels:
    print(level)

    subtopic_query = f"You are a subject matter expert providing detailed educational content. Your task is to Generate a list of subtopics for the topic {topic} and categorise the subtopics into the {level} level. These subtopics will form the foundation of a learning module. Please ensure that the subtopics are relevant and comprehensive."
    
    #fire subtopic query for all models
    model1_result_s = integrated_function.llama3_search(subtopic_query)
    model2_result_s = integrated_function.llama2_search(subtopic_query)
    model3_result_s = integrated_function.mistral_search(subtopic_query)
    # model4_result_s = integrated_function.phind_search(subtopic_query)
    # model5_result_s = integrated_function.perplexity_search(subtopic_query)

    model1_challenge_list = []
    model2_challenge_list = []
    model3_challenge_list = []
    # model4_challenge_list = []
    # model5_challenge_list = []

    # convert subtopics in list
    model1_list = extract_subtopics_as_sections(model1_result_s)
    print(model1_list)

    # generate challenges from the subtopics list
    for subtopic in model1_list:
      challenge_query = f"""Generate a real world based challenge on the subtopic {subtopic} related to {topic} of  {level} level. Structure the challenge according to the provided format, focusing on practical application and skill development.

        Challenge Format:

        - Name: Provide a concise and descriptive title for the challenge.

        - Objective: Clearly state the main goal or purpose of the challenge, highlighting what the participant will learn or accomplish.

        - Challenge Level: {level}

        - Description: Provide a detailed description of the challenge, including the context, scope, and any specific tasks or activities involved.

        - Milestone Evaluation: Outline key milestones that participants should achieve during the challenge, along with criteria for evaluating their progress.

        - Skills: List the specific skills that participants will develop or utilise during the challenge.

        - Challenge Guidelines: Provide guidelines or instructions that participants should follow, including any constraints or requirements.

        - Prerequisites: List any prerequisites that participants should meet before attempting the challenge.

        - Review Process: Describe the process for reviewing and assessing participants' work, including any feedback or scoring methods.

        Ensure that the challenge is aligned with the subtopic and is designed to facilitate skill growth and professional development.
        """
      model1_result_c = integrated_function.llama3_search(challenge_query)
      model1_challenge_list.append(model1_result_c)
      print(model1_result_c)


    model2_list = extract_subtopics_v6(model2_result_s)
    print(model2_list)

    for subtopic in model2_list:
      challenge_query = f"""Generate a real world based challenge on the subtopic {subtopic} related to {topic} of  {level} level. Structure the challenge according to the provided format, focusing on practical application and skill development.

        Challenge Format:

        - Name: Provide a concise and descriptive title for the challenge.

        - Objective: Clearly state the main goal or purpose of the challenge, highlighting what the participant will learn or accomplish.

        - Challenge Level: {level}

        - Description: Provide a detailed description of the challenge, including the context, scope, and any specific tasks or activities involved.

        - Milestone Evaluation: Outline key milestones that participants should achieve during the challenge, along with criteria for evaluating their progress.

        - Skills: List the specific skills that participants will develop or utilise during the challenge.

        - Challenge Guidelines: Provide guidelines or instructions that participants should follow, including any constraints or requirements.

        - Prerequisites: List any prerequisites that participants should meet before attempting the challenge.

        - Review Process: Describe the process for reviewing and assessing participants' work, including any feedback or scoring methods.

        Ensure that the challenge is aligned with the subtopic and is designed to facilitate skill growth and professional development.
        """
      model2_result_c = integrated_function.llama3_search(challenge_query)
      model2_challenge_list.append(model2_result_c)
      print(model2_result_c)


    model3_list = extract_numbered_subtopics_as_sections(model3_result_s)
    print(model3_list)

    for subtopic in model3_list:
      challenge_query = f"""Generate a real world based challenge on the subtopic {subtopic} related to {topic} of  {level} level. Structure the challenge according to the provided format, focusing on practical application and skill development.

        Challenge Format:

        - Name: Provide a concise and descriptive title for the challenge.

        - Objective: Clearly state the main goal or purpose of the challenge, highlighting what the participant will learn or accomplish.

        - Challenge Level: {level}

        - Description: Provide a detailed description of the challenge, including the context, scope, and any specific tasks or activities involved.

        - Milestone Evaluation: Outline key milestones that participants should achieve during the challenge, along with criteria for evaluating their progress.

        - Skills: List the specific skills that participants will develop or utilise during the challenge.

        - Challenge Guidelines: Provide guidelines or instructions that participants should follow, including any constraints or requirements.

        - Prerequisites: List any prerequisites that participants should meet before attempting the challenge.

        - Review Process: Describe the process for reviewing and assessing participants' work, including any feedback or scoring methods.

        Ensure that the challenge is aligned with the subtopic and is designed to facilitate skill growth and professional development.
        """
      model3_result_c = integrated_function.llama3_search(challenge_query)
      model3_challenge_list.append(model3_result_c)
      print(model3_result_c)


    # model4_list = extract_subtopics_with_bullets_v4(model4_result_s)
    # print(model4_list)

    # for subtopic in model4_list:
    #   challenge_query = f"""Generate a real world based challenge on the subtopic {subtopic} related to {topic} of  {level} level. Structure the challenge according to the provided format, focusing on practical application and skill development.

    #     Challenge Format:

    #     - Name: Provide a concise and descriptive title for the challenge.

    #     - Objective: Clearly state the main goal or purpose of the challenge, highlighting what the participant will learn or accomplish.

    #     - Challenge Level: {level}

    #     - Description: Provide a detailed description of the challenge, including the context, scope, and any specific tasks or activities involved.

    #     - Milestone Evaluation: Outline key milestones that participants should achieve during the challenge, along with criteria for evaluating their progress.

    #     - Skills: List the specific skills that participants will develop or utilise during the challenge.

    #     - Challenge Guidelines: Provide guidelines or instructions that participants should follow, including any constraints or requirements.

    #     - Prerequisites: List any prerequisites that participants should meet before attempting the challenge.

    #     - Review Process: Describe the process for reviewing and assessing participants' work, including any feedback or scoring methods.

    #     Ensure that the challenge is aligned with the subtopic and is designed to facilitate skill growth and professional development.
    #     """
    #   model4_result_c = integrated_function.llama3_search(challenge_query)
    #   model4_challenge_list.append(model4_result_c)
    #   print(model4_result_c)


    # model5_list = extract_subtopics_with_bullets_v3(model5_result_s)
    # print(model5_list)

    # for subtopic in model5_list:
    #   challenge_query = f"""Generate a real world based challenge on the subtopic {subtopic} related to {topic} of  {level} level. Structure the challenge according to the provided format, focusing on practical application and skill development.

    #     Challenge Format:

    #     - Name: Provide a concise and descriptive title for the challenge.

    #     - Objective: Clearly state the main goal or purpose of the challenge, highlighting what the participant will learn or accomplish.

    #     - Challenge Level: {level}

    #     - Description: Provide a detailed description of the challenge, including the context, scope, and any specific tasks or activities involved.

    #     - Milestone Evaluation: Outline key milestones that participants should achieve during the challenge, along with criteria for evaluating their progress.

    #     - Skills: List the specific skills that participants will develop or utilise during the challenge.

    #     - Challenge Guidelines: Provide guidelines or instructions that participants should follow, including any constraints or requirements.

    #     - Prerequisites: List any prerequisites that participants should meet before attempting the challenge.

    #     - Review Process: Describe the process for reviewing and assessing participants' work, including any feedback or scoring methods.

    #     Ensure that the challenge is aligned with the subtopic and is designed to facilitate skill growth and professional development.
    #     """
    #   model5_result_c = integrated_function.llama3_search(challenge_query)
    #   model5_challenge_list.append(model5_result_c)
    #   print(model5_result_c)

    # for subtopic in subtopics:
    #   model1_result_c = integrated_function.llama3_search(challenge_query)
    #   model2_result_c = integrated_function.llama2_search(challenge_query)
    #   model3_result_c = integrated_function.mistral_search(challenge_query)
    #   model4_result_c = integrated_function.phind_search(challenge_query)
    #   model5_result_c = integrated_function.perplexity_search(challenge_query)

    models = ['Llama3', 'Llama2', 'Mistral']
    for model in models:
        # if(model=='Phind'):
        #    for sub, chn in zip(model5_list, model5_challenge_list):
        #     result_challenge = [topic, level, model, sub, chn]
        #     with open("Tntra_Prof_Mob_Testcase_challenge.csv", 'a', newline='') as file:
        #         writer = csv.writer(file)
        #         writer.writerow(result_challenge)

        # if(model=='Perplexity'):
        #    for sub, chn in zip(model4_list, model4_challenge_list):
        #     result_challenge = [topic, level, model, sub, chn]
        #     with open("Tntra_Prof_Mob_Testcase_challenge.csv", 'a', newline='') as file:
        #         writer = csv.writer(file)
        #         writer.writerow(result_challenge)

        if(model=='Llama3'):
           for sub, chn in zip(model1_list, model1_challenge_list):
            result_challenge = [topic, level, model, sub, chn]
            with open("Tntra_Prof_Mob_Testcase_challenge.csv", 'a', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(result_challenge)

        if(model=='Llama2'):
           for sub, chn in zip(model2_list, model2_challenge_list):
            result_challenge = [topic, level, model, sub, chn]
            with open("Tntra_Prof_Mob_Testcase_challenge.csv", 'a', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(result_challenge)

        if(model=='Mistral'):
           for sub, chn in zip(model3_list, model3_challenge_list):
            result_challenge = [topic, level, model, sub, chn]
            with open("Tntra_Prof_Mob_Testcase_challenge.csv", 'a', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(result_challenge)