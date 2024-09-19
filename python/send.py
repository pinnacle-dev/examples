from rcs import (
    Pinnacle,
    RCSBasicMessage,
    RCSMediaMessage,
    Action,
    Card,
    Carousel,
    PayloadData,
    SMSMessage,
)
import datetime

pinn = Pinnacle(
    api_key=API_KEY,
    webhook_url=WEBHOOK_URL,
)


def send_test_message(message_type: str = "basic"):
    message = RCSBasicMessage("Hello, this is a test message!").with_quick_replies(
        [
            Action(
                title="URL",
            ).weburl("https://example.com"),
            Action(
                title="Call",
            ).call("+18888888888"),
            Action(
                title="Payload",
            ).postback("payload", "payload_value"),
            Action(
                title="Share Location",
            ).shareLocation(),
            Action(
                title="Calendar",
            ).calendar(
                title="Meeting",
                description="Discuss project updates",
                start_time=datetime.datetime.now(),
                end_time=datetime.datetime.now() + datetime.timedelta(hours=1),
            ),
        ]
    )
    if message_type == "media":
        message = RCSMediaMessage(
            media_type="file",
            media_url="https://www.trypinnacle.app/_next/image?url=%2Flogo.png&w=1920&q=75",
        ).with_quick_replies(
            [
                Action(
                    title="URL",
                ).weburl("https://example.com"),
                Action(
                    title="Call",
                ).call("+18888888888"),
                Action(
                    title="Payload",
                ).postback("payload", "payload_value"),
                Action(
                    title="Share Location",
                ).shareLocation(),
                Action(
                    title="Calendar",
                ).calendar(
                    title="Meeting",
                    description="Discuss project updates",
                    start_time=datetime.datetime.now(),
                    end_time=datetime.datetime.now() + datetime.timedelta(hours=1),
                ),
            ]
        )

    elif message_type == "card":
        message = (
            Card(
                title="Card Title",
                subtitle="Card Description",
                image_url="https://www.trypinnacle.app/_next/image?url=%2Flogo.png&w=1920&q=75",
            )
            .with_horizontal_style(
                width="medium",
                image_alignment="left",
            )
            .with_quick_replies(
                [
                    Action(
                        title="URL",
                    ).weburl("https://example.com"),
                    Action(
                        title="Call",
                    ).call("+18888888888"),
                    Action(
                        title="Payload",
                    ).postback("payload", "payload_value"),
                    Action(
                        title="Share Location",
                    ).shareLocation(),
                    Action(
                        title="Calendar",
                    ).calendar(
                        title="Meeting",
                        description="Discuss project updates",
                        start_time=datetime.datetime.now(),
                        end_time=datetime.datetime.now() + datetime.timedelta(hours=1),
                    ),
                ]
            )
            .with_buttons(
                [
                    Action(
                        title="URL",
                    ).weburl("https://example.com"),
                    Action(
                        title="Payload",
                    ).postback("payload", "payload_value"),
                    Action(
                        title="Share Location",
                    ).shareLocation(),
                    Action(
                        title="Calendar",
                    ).calendar(
                        title="Meeting",
                        description="Discuss project updates",
                        start_time=datetime.datetime.now(),
                        end_time=datetime.datetime.now() + datetime.timedelta(hours=1),
                    ),
                ]
            )
        )

    elif message_type == "carousel":
        card = (
            Card(
                title="Card Title",
                subtitle="Card Description",
                image_url="https://www.trypinnacle.app/_next/image?url=%2Flogo.png&w=1920&q=75",
            )
            .with_horizontal_style(
                width="medium",
                image_alignment="left",
            )
            .with_quick_replies(
                [
                    Action(
                        title="URL",
                    ).weburl("https://example.com"),
                    Action(
                        title="Call",
                    ).call("+18888888888"),
                    Action(
                        title="Payload",
                    ).postback("payload", "payload_value"),
                    Action(
                        title="Share Location",
                    ).shareLocation(),
                    Action(
                        title="Calendar",
                    ).calendar(
                        title="Meeting",
                        description="Discuss project updates",
                        start_time=datetime.datetime.now(),
                        end_time=datetime.datetime.now() + datetime.timedelta(hours=1),
                    ),
                ]
            )
            .with_buttons(
                [
                    Action(
                        title="URL",
                    ).weburl("https://example.com"),
                    Action(
                        title="Payload",
                    ).postback("payload", "payload_value"),
                    Action(
                        title="Share Location",
                    ).shareLocation(),
                    Action(
                        title="Calendar",
                    ).calendar(
                        title="Meeting",
                        description="Discuss project updates",
                        start_time=datetime.datetime.now(),
                        end_time=datetime.datetime.now() + datetime.timedelta(hours=1),
                    ),
                ]
            )
        )

        message = Carousel([card, card, card, card]).with_quick_replies(
            [
                Action(
                    title="URL",
                ).weburl("https://example.com"),
                Action(
                    title="Call",
                ).call("+18888888888"),
                Action(
                    title="Payload",
                ).postback("payload", "payload_value"),
                Action(
                    title="Share Location",
                ).shareLocation(),
                Action(
                    title="Calendar",
                ).calendar(
                    title="Meeting",
                    description="Discuss project updates",
                    start_time=datetime.datetime.now(),
                    end_time=datetime.datetime.now() + datetime.timedelta(hours=1),
                ),
            ]
        )

    elif message_type == "sms":
        message = SMSMessage(
            "Hello, this is a test SMS message!",
            "https://www.trypinnacle.app/_next/image?url=%2Flogo.png&w=1920&q=75",
        )
    pinn.send(
        message,
        "+18888888888",
    )


def check_rcs_status(phone_number: str):
    status = pinn.check_rcs_status(phone_number)
    print(f"RCS status for {phone_number}: {status}")


def receive_message(payload: PayloadData):
    print(f"Received message: {payload}")


send_test_message()
send_test_message("card")
check_rcs_status("+18888888888")

pinn.on_message(receive_message)
