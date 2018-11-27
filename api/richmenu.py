from flask import jsonify
from linebot import (
    LineBotApi
)
from linebot.models import (
    URITemplateAction,
    RichMenu, RichMenuSize, RichMenuArea, RichMenuBounds,
    MessageAction,
    URIAction
)
line_bot_api = LineBotApi("{channel access token}")

def newRichMenu(token):
    headers = { 
        "Authorization": "Bearer "+str(token),
        "Content-Type": "application/json"
    }
    menu_to_create = RichMenu(
        size=RichMenuSize(width=2500, height=843),
        selected=False,
        name="menu",
        chat_bar_text="選單",
        areas=[
            RichMenuArea(
                bounds=RichMenuBounds(x=0,y=0,width=625, height=843),
                action=MessageAction(text="自我介紹")
            ),
            RichMenuArea(
                bounds=RichMenuBounds(x=625,y=0,width=625, height=843),
                action=MessageAction(text="簡歷")
            ),
            RichMenuArea(
                bounds=RichMenuBounds(x=1250,y=0,width=625, height=843),
                action=MessageAction(text="作品集")
            ),
            RichMenuArea(
                bounds=RichMenuBounds(x=1875,y=0,width=625, height=843),
                action=URIAction(uri="https://github.com/BryantTseng/Line_BOT_Flask")
            ),
            
        ]
    )
    RichMenu_id = line_bot_api.create_rich_menu(rich_menu=menu_to_create)
    print(RichMenu_id)
    
    return RichMenu_id
def uploadRichMenu(id):
    f = open("menu.png", "rb")
    line_bot_api.set_rich_menu_image(rich_menu_id=id, content_type="image/jpeg", content = f)
    line_bot_api.link_rich_menu_to_user(user_id="all", rich_menu_id = id)
    return 
