from flask import Flask, request, abort
from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,ImageSendMessage,LocationMessage,
    FollowEvent,UnfollowEvent,
    TemplateSendMessage, CarouselTemplate, CarouselColumn, MessageTemplateAction, URITemplateAction
)
from api import richmenu
import texts as ri_text
app = Flask(__name__)
line_bot_api = LineBotApi("{channel access token}")
handler = WebhookHandler("{channel secret}")
server_url = "{server url}"

@app.route("/newMenu", methods=["GET"])
def list():
    richmenu.uploadRichMenu(richmenu.newRichMenu("{channel access token}")
)
    return "!"
@app.route("/callback", methods=["POST"])
def callback():
    signature = request.headers['X-Line-Signature']
    body = request.get_data(as_text=True)
    app.logger.info("Request body: "+ body)
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)
    return "OK"
@handler.add(FollowEvent)
def handle_join(event):
    line_bot_api.reply_message(
       event.reply_token,
       TextSendMessage(text=ri_text.text_of_follow.follow_text)
       )
    print("Join event = ", FollowEvent)
@handler.add(MessageEvent, message = TextMessage)
def handle_message(event):
    if event.message.text=="自我介紹":
        line_bot_api.reply_message(
        event.reply_token,
        messages = [
            TextSendMessage(text=ri_text.text_of_richmenu.box1_text),
            LocationMessage(title="國立台灣科技大學", address="106台北市大安區基隆路四段43號", latitude="25.013016", longitude="121.540812")

        ]
        )
    elif event.message.text=="簡歷":
        line_bot_api.reply_message(
            event.reply_token,
            messages = [    TextSendMessage(text=ri_text.text_of_richmenu.box2_text),
                            ImageSendMessage(original_content_url=server_url+"CV_1.jpg", preview_image_url=server_url+"CV_1.jpg"),
                            ImageSendMessage(original_content_url=server_url+"CV_2.jpg", preview_image_url=server_url+"CV_2.jpg")
            ]
        )
    elif event.message.text=="NIC 簡介":
        line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=ri_text.text_of_carou.description_nic)
        )
    elif event.message.text=="EOF 簡介":
        line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=ri_text.text_of_carou.description_eof)
        )
    elif event.message.text=="AIS3 簡介":
        line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=ri_text.text_of_carou.description_ais3)
        )
    elif event.message.text=="roomii 簡介":
        line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=ri_text.text_of_carou.description_roomii)
        )
    elif event.message.text=="作品集":
        Carousel_template = TemplateSendMessage(
            alt_text="作品集",
            template=CarouselTemplate(
                columns=[
                    CarouselColumn(
                        thumbnail_image_url=server_url+"icon_NIC.png",
                        title="NIC",
                        text="Nokia CallCenter",
                        actions=[
                            MessageTemplateAction(
                                label="簡介",
                                text="NIC 簡介"
                            ),
                            URITemplateAction(
                                label="連結",
                                uri="https://nokiasupport.com/web"
                            )
                            
                        ]
                    ),
                    CarouselColumn(
                        thumbnail_image_url=server_url+"logo-eof2.png",
                        title="EOF",
                        text="資安搶旗競賽",
                        actions=[
                            MessageTemplateAction(
                                label="簡介",
                                text="EOF 簡介"
                            ),
                            URITemplateAction(
                                label="連結",
                                uri="https://ais3.org/eof"
                            )
                            
                        ]
                    ),
                    CarouselColumn(
                        thumbnail_image_url=server_url+"home-banner.png",
                        title="AIS 3",
                        text="暑期資安課程",
                        actions=[
                            MessageTemplateAction(
                                label="簡介",
                                text="AIS3 簡介"
                            ),
                             URITemplateAction(
                                label="連結",
                                uri="https://ais3.org"
                            )
                            
                        ]
                    ),
                    CarouselColumn(
                        thumbnail_image_url=server_url+"roomii.jpg",
                        title="roomii",
                        text="遠端智慧寵物互動機",
                        actions=[
                            MessageTemplateAction(
                                label="簡介",
                                text="roomii 簡介"
                            ),
                             URITemplateAction(
                                label="連結",
                                uri="https://www.youtube.com/watch?v=azWzHsz2J_k"
                            )
                            
                        ]
                    ),
                ]
            )
        )
        line_bot_api.reply_message(
        event.reply_token,
        Carousel_template
        )    
    else:
        line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text="抱歉, 你輸入的文字沒有相對應的指令")
        )
    

if __name__=="__main__":
    app.run()