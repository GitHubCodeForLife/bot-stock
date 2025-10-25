from app.shareData import ShareData
from app.model.models import db
from datetime import datetime
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String, Integer, create_engine

class NotificationLog(db.Model):
    log_id : Mapped[int] = mapped_column(Integer, primary_key=True)
    platform : Mapped[str] = mapped_column(String(255))
    channel : Mapped[str] = mapped_column(String(255))
    message : Mapped[str] = mapped_column(String(255))
    send_time : Mapped[datetime] = mapped_column()
    stock_code : Mapped[str] = mapped_column(String(255))
    type : Mapped[str] = mapped_column(String(255))  # e.g., "price_alert", "news_update"

def add_notification_log(platform, channel, message, stock_code):
    with ShareData.app.app_context():
        log = NotificationLog(
            platform=platform,
            channel=channel,
            message=message,
            send_time=datetime.now(),
            stock_code=stock_code,
            type="price_alert"
        )
        db.session.add(log)
        db.session.commit()

def is_sent_notif_today(platform, channel, stock_code):
    with ShareData.app.app_context():
        today = datetime.now().date()
        log = NotificationLog.query.filter_by(
            platform=platform,
            channel=channel,
            stock_code=stock_code,
            type="price_alert"
        ).filter(db.func.date(NotificationLog.send_time) == today).first()
        return log is not None