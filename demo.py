from gardient import color_text_cleangreen

LOGO = r"""
████████╗███████╗███████╗████████╗
╚══██╔══╝██╔════╝██╔════╝╚══██╔══╝
   ██║   █████╗  ███████╗   ██║   
   ██║   ██╔══╝  ╚════██║   ██║   
   ██║   ███████╗███████║   ██║   
   ╚═╝   ╚══════╝╚══════╝   ╚═╝   
                                  
"""

def main():

    print(color_text_cleangreen(LOGO))
    
    sample_text = "Welcome here is a quick demo to check how the color can be applied🌿"
    colored = color_text_cleangreen(sample_text)
    print(colored)

if __name__ == "__main__":
    main()
