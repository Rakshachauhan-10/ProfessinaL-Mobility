import comtypes.client

def convert_ppt_to_images(ppt_file, output_folder):
    powerpoint = comtypes.client.CreateObject("D:\Professional Mobility\Extra_trial\Intermediate_Data_Science.pptx")
    powerpoint.Visible = 1

    presentation = powerpoint.Presentations.Open(ppt_file)
    
    for i, slide in enumerate(presentation.Slides):
        slide.Export(f"{output_folder}/slide_{i+1}.png", "PNG")

    presentation.Close()
    powerpoint.Quit()

convert_ppt_to_images('D:\Professional Mobility\Extra_trial\Intermediate_Data_Science.pptx', 'output_images')
