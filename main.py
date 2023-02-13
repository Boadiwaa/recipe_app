# -*- coding: utf-8 -*-
"""
Created on Thu Jan 26 15:16:09 2023

@author: pauli
"""
import openai
import flet as ft
from flet import (
    theme,
    UserControl,
    Container,
    Page,
    Text,
    AppBar,
    icons,
    #margin,
    #View,
    IconButton,
    Row,
    #Image,
    ImageFit,
    alignment,
    Stack,
    MainAxisAlignment,
    CrossAxisAlignment,
    TextField,
    ElevatedButton,
    #MaterialState,
    colors,
    border_radius,
    Column)


def main(page: Page):
    search = TextField(label="Food Ingredient", hint_text="Please enter the main ingredient", helper_text="Example: Milk", border = "none",
                                    icon=icons.SEARCH)
    result = Row([Column([], horizontal_alignment=CrossAxisAlignment.CENTER)], alignment=MainAxisAlignment.CENTER) 
    pr = Row([ft.ProgressRing()], alignment= MainAxisAlignment.CENTER)
    page.title = "Something Sweet..."
    page.padding = 0
    page.theme = theme.Theme(
              font_family="Segoe Print")
    page.fonts = {
        "Pacifico": f"/Pacifico-Regular.ttf"
        }        
    page.bgcolor = "#E7ECF3"
    ic ="#EC6CA4"
    appbar = AppBar(
    leading=Row(controls = [IconButton(icons.CAKE, icon_size = 50, icon_color=ic), IconButton(icons.FASTFOOD, icon_size = 50, icon_color=ic),
        IconButton(icons.LOCAL_PIZZA, icon_size = 50, icon_color=ic)
        ]), #cake_outlined #cookie_outlined #outdoor_grill_outlined emoji_food_beverage_outlined lunch_dining_outlined fastfood_outlined
    leading_width=100,
  title=Text(f"Something Sweet...",size=30, text_align="start", font_family="Pacifico", color = "#A3BCD0"),#"Segoe Print"
  center_title=True,
  toolbar_height=80,
     bgcolor="#EED2D4" , 
     actions=[
        IconButton(icons.LUNCH_DINING, icon_size = 50, icon_color=ic),
        IconButton(icons.COOKIE, icon_size = 50, icon_color=ic),
        IconButton(icons.EMOJI_FOOD_BEVERAGE, icon_size = 50, icon_color=ic)])
    

    def generate_prompt(recipe_titles):
       return """Suggest a recipe title based on the food item inputted, then acting as a cookbook 
              give the full recipe for the title suggested, include ingredients and instructions
   
              Example:
   
              Food: {}
              Titles:""".format(
                      recipe_titles.capitalize()
                      )
    
        
        
    def refresh():
        pr.controls.clear()
        page.update()
        
    def ai():
        openai.api_key =  "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"
        response = openai.Completion.create(
        model="text-davinci-003",
                        prompt=generate_prompt(search.value),
                        temperature=0.95,
                        max_tokens = 4000
                        )
        response = response.choices[0].text
        result.controls.append(Text(response))
        page.scroll = ft.ScrollMode.ALWAYS
        page.update()
        refresh()
        
    
    def button_clicked(e):
        
        page.add(pr)
        ai()
    #apikey  = pickle.load(f)
       
        #result.controls.clear()
        
    def clear(e):
    
         result.controls.clear()
         page.update()
         
   
    b = ElevatedButton(text="Generate recipe", 
                              on_click= button_clicked, 
                              data = search.value)
    c = ElevatedButton(text="Clear results", 
                              on_click= clear)
    buttons = Row([b, c], alignment=MainAxisAlignment.CENTER)
    

# Control for the image  and the layout for the subtitle and the image   
    image = Row(
        [
            Container(
                image_src=f"/sweets.jpg",
                width=600,
                height=200,              
                image_fit=ImageFit.FILL,
                alignment= alignment.center,
                image_opacity = 0.25)],
        alignment=MainAxisAlignment.CENTER)
    layout = Stack([image,
               Column([Row(
                   [
                       Text(
                           "Generate different recipes from just ONE ingredient!",
                           color="grey",
                           size=15,
                           italic=True,
                           
                       )
                   ],
                   alignment=MainAxisAlignment.CENTER,
                   vertical_alignment=CrossAxisAlignment.END
               ),
                Row([Container(
                            width=500,
                            bgcolor=colors.WHITE,
                            border_radius=border_radius.all(20),
                            padding=20,
                            content=Column(
                                controls=[
                                    Row(controls=[search], alignment= "center"),
                                     ]
                                ),
                          alignment= alignment.center  )
                ], alignment=MainAxisAlignment.CENTER )
          
       ]
        ) ])
    outline = Column(spacing=0, controls=[layout,Column([Row( alignment=MainAxisAlignment.CENTER),
                                                         Row( alignment=MainAxisAlignment.CENTER)]),buttons,result],
                     horizontal_alignment=CrossAxisAlignment.CENTER) # further structuring of the page in terms of appearance of elements.
    page.add(appbar,outline)
 
    
ft.app(port=8080,target=main,assets_dir="assets")#, view=ft.WEB_BROWSER)#, web_renderer="html")     
        
         
             
         
         
         
             



   

   
    
        
           
        
        
        
             
        
      
        